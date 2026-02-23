#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════
# Wilson's Multi-Asset Research — Report Builder
# Usage: bash scripts/build_report.sh reports/2026-02-23-topic-equity.tex
# ══════════════════════════════════════════════════════════════

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: bash scripts/build_report.sh <path-to-tex-file>"
    exit 1
fi

TEX_FILE="$1"
TEX_DIR="$(dirname "$TEX_FILE")"
TEX_NAME="$(basename "$TEX_FILE" .tex)"
MAX_RETRIES=3

# Ensure the .cls is findable (copy to build dir if not there)
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
if [ ! -f "$TEX_DIR/wilson-report.cls" ]; then
    if [ -f "$SCRIPT_DIR/wilson-report.cls" ]; then
        cp "$SCRIPT_DIR/wilson-report.cls" "$TEX_DIR/"
    else
        echo "ERROR: wilson-report.cls not found in $TEX_DIR or $SCRIPT_DIR"
        exit 1
    fi
fi

echo "══════════════════════════════════════════"
echo "Building: $TEX_FILE"
echo "══════════════════════════════════════════"

cd "$TEX_DIR"

# Two-pass compilation with retry logic
for attempt in $(seq 1 $MAX_RETRIES); do
    echo ""
    echo "── Pass 1 (attempt $attempt/$MAX_RETRIES) ──"
    if xelatex -interaction=nonstopmode "$TEX_NAME.tex" > /dev/null 2>&1; then
        echo "Pass 1: OK"
    else
        echo "Pass 1: Errors detected"
        # Extract the first error from the log
        if [ -f "$TEX_NAME.log" ]; then
            echo ""
            echo "── First error from log: ──"
            grep -A 3 "^!" "$TEX_NAME.log" | head -8
            echo ""
        fi

        if [ "$attempt" -lt "$MAX_RETRIES" ]; then
            echo "Retrying..."
            continue
        else
            echo ""
            echo "FAILED after $MAX_RETRIES attempts."
            echo "Full log: $TEX_DIR/$TEX_NAME.log"
            echo "Delivering .tex file — manual fix required."
            exit 1
        fi
    fi

    echo "── Pass 2 (page references) ──"
    if xelatex -interaction=nonstopmode "$TEX_NAME.tex" > /dev/null 2>&1; then
        echo "Pass 2: OK"
    else
        echo "Pass 2: Warnings (likely non-fatal — checking output)"
    fi

    # Verify PDF was created
    if [ -f "$TEX_NAME.pdf" ]; then
        PAGES=$(pdfinfo "$TEX_NAME.pdf" 2>/dev/null | grep "^Pages:" | awk '{print $2}' || echo "?")
        SIZE=$(du -h "$TEX_NAME.pdf" | awk '{print $1}')
        echo ""
        echo "══════════════════════════════════════════"
        echo "SUCCESS: $TEX_NAME.pdf ($PAGES pages, $SIZE)"
        echo "══════════════════════════════════════════"

        # Clean up aux files
        rm -f "$TEX_NAME.aux" "$TEX_NAME.log" "$TEX_NAME.out" "$TEX_NAME.toc" "$TEX_NAME.fls" "$TEX_NAME.fdb_latexmk"

        exit 0
    else
        echo "ERROR: PDF not generated despite no xelatex errors."
        if [ "$attempt" -lt "$MAX_RETRIES" ]; then
            echo "Retrying..."
        fi
    fi
done

echo "FAILED: Could not produce PDF after $MAX_RETRIES attempts."
exit 1
