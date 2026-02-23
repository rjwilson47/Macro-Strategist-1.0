# Wilson's Multi-Asset Research

An AI-powered investment research system that produces institutional-grade PDF briefings using Claude Code.

## What it does

You give it a topic (or ask "what's interesting?") and it searches for live market data, builds charts, and compiles a branded PDF report with sourced analysis, scenario probabilities, and actionable trade expressions. Every data point is sourced from web search — nothing is fabricated. It prioritises intellectual honesty over narrative coherence.

## Files

| File | What it is |
|---|---|
| `CLAUDE.md` | **The main prompt**
| `wilson-report.cls` | LaTeX document class (all branding, colours, commands) |
| `wilson_latex_template.tex` | Report content skeleton — copy per report |
| `wilson_charts.py` | Chart styling helper (colours, fonts, formatting) |
| `scripts/build_report.sh` | Build script — handles compilation, retries, error reporting |
| `wilson_preferences.md` | Your standing instructions — edit over time |
| `wilson_house_view.md` | Persistent macro view with conviction changelog |
| `wilson_watchlist.md` | Companies and themes being tracked with catalyst dates |
| `QUESTIONS.md` | Open questions pipeline — accumulated from reports |
| `log/_index.md` | Research log index — audit trail of all reports produced |
| `wilson_test_plan.md` | 7 stress tests to run before relying on it |

Place all files in the same directory in your Claude Code project. Reports go in `reports/`, charts in `figures/`, log entries in `log/`.

## How to use it

**Direct request (asset-class entry):** "Run a report on European defence equities"
→ Full branded PDF (5-10 pages, charts, scenarios, indicators to watch)

**Direct request (theme-first entry):** "What are the investment implications of GLP-1 drugs?"
→ Maps theme to affected assets/sectors/geographies automatically → Full report

**Company deep-dive:** "Deep dive on Rheinmetall"
→ Business model, financials, Damodaran-style DCF (bear/base/bull), reverse DCF, thematic relevance

**Secular / long-term:** "What's the 5-10 year structural case for energy transition?"
→ Same format, but shifts emphasis to structural drivers, demographics, technology curves, multi-year scenarios

**Open-ended:** "What's interesting right now?" or "Check in"
→ Scans across macro, themes, industries, countries, companies, factors → Theme Radar (3-5 cards) → you pick → full report

**Revision:** Upload a previous .tex file + "raise the bull case probability to 40%"
→ Surgical edit and recompile

## Report structure (every report)

1. **Executive Summary** — 4-line formula: View → Evidence → Risk → Expression
2. **Macro Context** — cycle, inflation, policy, risks
3. **Core Analysis** — valuation, earnings, sentiment, flows, charts
4. **Scenario Analysis** — bull/base/bear with probability-weighted returns
5. **Cross-Asset Implications** — what it means beyond the primary asset class
6. **Risks to the View** — specific, steelmanned counter-arguments
7. **Key Indicators to Watch** — what data would change the call, with thresholds and dates
8. **Actionable Conclusions** — direction + conviction + instruments + hedges + falsification criteria
9. **Open Questions** — 2-3 questions for future investigation
10. **Sources** — with clickable URLs

## Key guardrails

- Every number must be sourced from web search (never fabricated)
- Evidence quality tagged: **Measured** (hard data) → **Inferred** (logical extrapolation) → **Speculative** (hypothesis)
- Source tiers: Tier 1 (primary) → Tier 2 (secondary) → Tier 3 (signal detection only)
- Actively searches for disconfirming evidence; steelmans the opposing view
- Falsification criteria: every report states what would prove the thesis wrong
- AI-generated hypotheses separated into a clearly labelled appendix
- Stale data flagged automatically
- House view updated after every report with dated evidence (append, never overwrite)

## Investment horizons

- **Tactical** (1-3 months) — short-term catalysts
- **Strategic** (12 months) — the default
- **Secular** (3-10 years) — structural, long-horizon views

## Output

PDFs named: `YYYY-MM-DD-[topic]-[asset-class].pdf`

Asset class tags: `equity`, `fixed-income`, `multi-asset`, `economic`, `commodities`, `fx`, `thematic`, `company`, `secular`
