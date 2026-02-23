#!/usr/bin/env bash
# Build a Wilson's report: two-pass xelatex with error detection and retry
# Usage: bash scripts/build_report.sh reports/my-report.tex

set -euo pipefail

TEX_FILE="${1:?Usage: $0 <tex-file>}"
DIR="$(dirname "$TEX_FILE")"
BASE="$(basename "$TEX_FILE" .tex)"
MAX_ATTEMPTS=3

cd "$DIR"

for attempt in $(seq 1 $MAX_ATTEMPTS); do
  echo "=== Compilation attempt $attempt / $MAX_ATTEMPTS ==="
  # First pass
  if xelatex -interaction=nonstopmode -halt-on-error "$BASE.tex" > /dev/null 2>&1; then
    # Second pass (for page refs)
    if xelatex -interaction=nonstopmode -halt-on-error "$BASE.tex" > /dev/null 2>&1; then
      echo "SUCCESS: $DIR/$BASE.pdf"
      exit 0
    fi
  fi
  echo "Attempt $attempt failed."
  if [ "$attempt" -lt "$MAX_ATTEMPTS" ]; then
    echo "Retrying..."
  fi
done

echo "=== FAILED after $MAX_ATTEMPTS attempts ==="
echo "Error from log:"
grep -A2 "^!" "$BASE.log" 2>/dev/null || tail -30 "$BASE.log"
echo ""
echo "TEX file delivered at: $DIR/$BASE.tex"
exit 1
