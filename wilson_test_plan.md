# Wilson's Multi-Asset Research — Test Plan

*Run these 7 reports in order to stress-test different parts of the prompt. After each test, note any issues and update the prompt or preferences file accordingly.*

---

## Test 1: Pure Macro Report
**Prompt:** "Run a macro outlook for the US economy over the next 12 months."
**Tests:** Module A depth without equity crutch, data freshness, GDP/inflation/employment sourcing, Fed policy analysis.
**Watch for:** Does it lean too heavily on equities? Can it produce a strong report without a stock market angle? Does the scenario analysis work for macro variables?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 2: Tactical Trade Idea (Short Format)
**Prompt:** "Give me a 3-5 page tactical trade idea on copper."
**Tests:** Concise format, commodities Module D, short horizon, search budget discipline (should be 8-12 searches).
**Watch for:** Does it stay concise or bloat? Does it use commodity-specific analysis (supply/demand, contango/backwardation, positioning)? Clear entry/exit framework?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 3: Cross-Asset Relative Value
**Prompt:** "Compare US equities vs US Treasuries vs gold on a risk-adjusted basis. Where is the best risk-adjusted return opportunity right now?"
**Tests:** Module H (Cross-Asset Synthesis), relative valuation across asset classes, correlation regime, ERP calculation, multi-asset scenario table.
**Watch for:** Genuine apples-to-apples comparison? Handles different return drivers? Actionable conclusion (not just "diversify")?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 4: EM-Focused Report (Data Scarcity)
**Prompt:** "Run a report on Indian equities — valuation, earnings cycle, and flows."
**Tests:** Data scarcity handling, Rule 8 escalation logic, EM-specific analysis, currency overlay, evidence quality tagging.
**Watch for:** Handles missing data gracefully? Properly incorporates FX dimension? Uses escalation logic? Evidence quality tags on Inferred vs Measured claims?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 5: Data-Scarce Thematic
**Prompt:** "Analyse the investment implications of nuclear fusion breakthroughs. What assets and sectors would benefit?"
**Tests:** Thematic Module G with thin data, AI hypothesis appendix usage, assumptions stress-test, evidence quality tagging (should be heavily Speculative/Inferred).
**Watch for:** Leans on AI hypothesis appendix? Clearly separates Measured vs Inferred vs Speculative? Avoids fabricating valuation data for early-stage companies? Open Questions section adds value?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 6: Company Deep Dive
**Prompt:** "Deep dive on Rheinmetall — how does it fit the European defence rearmament thesis?"
**Tests:** Module I (Company Analysis), Damodaran-style DCF, reverse DCF, competitive position, thematic linkage, falsification criteria.
**Watch for:** Does the DCF use explicit, stated assumptions? Does the reverse DCF reveal what's priced in? Does it link back to the broader thesis? Are risks ranked by probability × impact? Does it avoid giving a buy/sell recommendation?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Test 7: Secular Outlook
**Prompt:** "What's the 5-10 year structural case for energy transition? Which asset classes and sectors benefit?"
**Tests:** Secular horizon, structural drivers over current valuations, technology adoption curves, multi-year scenario trees, evidence quality (should be more Inferred/Speculative at this horizon).
**Watch for:** Does it shift emphasis away from current valuations toward structural drivers? Does the scenario tree work for multi-year outcomes? Does it acknowledge the uncertainty inherent in long-horizon views? Is the evidence quality tagging honest about what's Measured vs Inferred at this timescale?

**Result:** _[fill in after running]_
**Issues found:** _[fill in]_
**Prompt changes made:** _[fill in]_

---

## Post-Test Checklist

After running all 7 tests, assess:

- [ ] Did the error handling work when LaTeX compilation had issues?
- [ ] Did the tiered search budget hold (cheaper reports used fewer searches)?
- [ ] Did the disconfirming evidence rule produce genuine steelmanned counter-arguments?
- [ ] Did the house view file get updated after each report (appended, not overwritten)?
- [ ] Did the conviction changelog capture any shifts?
- [ ] Did cross-theme linkages get noted in the house view?
- [ ] Did the output naming convention produce consistent filenames?
- [ ] Were citation URLs included in the Sources section?
- [ ] Did the data freshness convention (prior close reference) work consistently?
- [ ] Were evidence quality tags (Measured/Inferred/Speculative) used consistently?
- [ ] Did source tiers (Tier 1/2/3) get referenced appropriately?
- [ ] Did the falsification criteria add genuine value (not just restating risks)?
- [ ] Did the Open Questions section produce investigable questions?
- [ ] Were any preferences added to wilson_preferences.md during testing?
- [ ] Did the Core Principles hold across all report types?
