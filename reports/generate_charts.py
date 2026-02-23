"""
Generate charts for the US Economic Outlook report.
Wilson's Multi-Asset Research — February 2026
"""
import sys
sys.path.insert(0, '/home/user/Macro-Strategist-1.0')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from wilson_charts import BRAND, wilson_style

# ═══════════════════════════════════════════════════════════════
# CHART 1: US GDP Growth — Quarterly Annualised (2024–2025)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
quarters = ['Q1\n2024', 'Q2\n2024', 'Q3\n2024', 'Q4\n2024', 'Q1\n2025', 'Q2\n2025', 'Q3\n2025', 'Q4\n2025']
gdp_growth = [1.6, 3.0, 3.1, 2.4, -0.3, 2.4, 4.4, 1.4]
colors = [BRAND['bull'] if g > 0 else BRAND['bear'] for g in gdp_growth]
bars = ax.bar(quarters, gdp_growth, color=colors, width=0.6, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, gdp_growth):
    ypos = val + 0.15 if val >= 0 else val - 0.3
    ax.text(bar.get_x() + bar.get_width()/2, ypos, f'{val:.1f}%',
            ha='center', va='bottom' if val >= 0 else 'top', fontsize=9,
            fontweight='bold', color=BRAND['dark_text'], fontfamily='serif')
ax.axhline(y=0, color=BRAND['mid_grey'], linewidth=0.8)
ax.axhline(y=2.0, color=BRAND['gold'], linewidth=1, linestyle='--', alpha=0.7)
ax.text(7.5, 2.15, 'Trend (~2%)', fontsize=7, color=BRAND['gold'], ha='right', fontfamily='serif')
wilson_style(ax, title='US Real GDP Growth (Quarterly Annualised, %)',
             ylabel='% QoQ Annualised',
             source='BEA, as of 20 Feb 2026')
ax.set_ylim(-1.5, 5.5)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-1.0/reports/chart_gdp_growth.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 2: Inflation — CPI YoY and Core PCE YoY
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
months = ['Jan\n25', 'Feb\n25', 'Mar\n25', 'Apr\n25', 'May\n25', 'Jun\n25',
          'Jul\n25', 'Aug\n25', 'Sep\n25', 'Oct\n25', 'Nov\n25', 'Dec\n25', 'Jan\n26']
# CPI YoY approximate trajectory based on sourced data
cpi_yoy = [3.0, 2.8, 2.4, 2.3, 2.5, 2.6, 2.9, 2.5, 2.4, None, None, 2.7, 2.4]
# Core PCE YoY approximate trajectory
core_pce = [2.8, 2.8, 2.6, 2.6, 2.6, 2.6, 2.7, 2.6, 2.7, None, None, 3.0, None]

# Filter out None values for plotting
cpi_x = [i for i, v in enumerate(cpi_yoy) if v is not None]
cpi_y = [v for v in cpi_yoy if v is not None]
pce_x = [i for i, v in enumerate(core_pce) if v is not None]
pce_y = [v for v in core_pce if v is not None]

ax.plot(cpi_x, cpi_y, color=BRAND['navy'], linewidth=2.2, marker='o', markersize=5, label='CPI YoY')
ax.plot(pce_x, pce_y, color=BRAND['accent'], linewidth=2.2, marker='s', markersize=5, label='Core PCE YoY')
ax.axhline(y=2.0, color=BRAND['bear'], linewidth=1, linestyle='--', alpha=0.7)
ax.text(12.3, 2.05, 'Fed Target (2%)', fontsize=7, color=BRAND['bear'], fontfamily='serif')

# Shade the shutdown data gap
ax.axvspan(9, 10.8, alpha=0.15, color=BRAND['mid_grey'])
ax.text(9.9, 3.35, 'Shutdown\ndata gap', fontsize=7, ha='center', color=BRAND['mid_grey'],
        fontfamily='serif', style='italic')

ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, fontsize=7)
ax.legend(fontsize=8, frameon=False, loc='upper right')
wilson_style(ax, title='US Inflation: CPI YoY vs Core PCE YoY (%)',
             ylabel='% Year-over-Year',
             source='BLS, BEA, as of Feb 2026')
ax.set_ylim(1.5, 3.8)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-1.0/reports/chart_inflation.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 3: Fed Funds Rate Path and Market Expectations
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
# Actual Fed Funds rate (upper bound of range)
dates_actual = ['Sep\n24', 'Nov\n24', 'Dec\n24', 'Jan\n25', 'Mar\n25', 'May\n25',
                'Jul\n25', 'Sep\n25', 'Dec\n25', 'Feb\n26']
rates_actual = [5.50, 5.00, 4.75, 4.50, 4.25, 4.00, 4.00, 3.75, 3.75, 3.75]
# Dec 2025 dot plot median projection
dates_dot = ['Feb\n26', 'Jun\n26', 'Dec\n26', 'Jun\n27', 'Dec\n27']
rates_dot = [3.75, 3.625, 3.50, 3.375, 3.25]
# Market pricing (2 cuts by year-end)
dates_mkt = ['Feb\n26', 'Jun\n26', 'Dec\n26']
rates_mkt = [3.75, 3.50, 3.25]

x_actual = list(range(len(dates_actual)))
x_dot = [len(dates_actual)-1 + i for i in range(len(dates_dot))]
x_mkt = [len(dates_actual)-1, len(dates_actual)-1 + 1, len(dates_actual)-1 + 2]

ax.step(x_actual, rates_actual, where='post', color=BRAND['navy'], linewidth=2.5, label='Actual Fed Funds (upper)')
ax.plot(x_dot, rates_dot, color=BRAND['gold'], linewidth=2, linestyle='--', marker='D',
        markersize=5, label='Dec 2025 Dot Plot Median')
ax.plot(x_mkt, rates_mkt, color=BRAND['accent'], linewidth=2, linestyle=':', marker='^',
        markersize=5, label='Market Pricing (Feb 26)')

all_labels = dates_actual + dates_dot[1:]
ax.set_xticks(range(len(all_labels)))
ax.set_xticklabels(all_labels, fontsize=7)
ax.legend(fontsize=7.5, frameon=False, loc='upper right')
wilson_style(ax, title='Federal Funds Rate: Actual, Dot Plot, and Market Expectations',
             ylabel='Fed Funds Rate (%)',
             source='Federal Reserve, CME FedWatch, as of Feb 2026')
ax.set_ylim(2.8, 5.8)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-1.0/reports/chart_fed_rate.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 4: US Macro Dashboard — Key Indicators Snapshot
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 5))

indicators = [
    'GDP Growth\n(Q4 2025 QoQ Ann.)',
    'CPI YoY\n(Jan 2026)',
    'Core PCE YoY\n(Dec 2025)',
    'Unemployment\n(Jan 2026)',
    'ISM Mfg PMI\n(Jan 2026)',
    'Consumer\nSentiment (Feb)',
    'Fed Funds Rate\n(Current)',
    'HY OAS\n(Feb 2026)'
]
values = [1.4, 2.4, 3.0, 4.3, 52.6, 56.6, 3.625, 2.86]
# Contextual targets/benchmarks for comparison
benchmarks = [2.0, 2.0, 2.0, 4.0, 50.0, 84.0, 3.5, 3.5]  # approximate norms/targets
# Normalise as ratio to benchmark for visual
ratios = [v/b if b != 0 else 0 for v, b in zip(values, benchmarks)]

# Use horizontal bar chart
y_pos = np.arange(len(indicators))
colors_bar = []
for i, (v, b) in enumerate(zip(values, benchmarks)):
    if i == 0:  # GDP: green if above trend
        colors_bar.append(BRAND['bear'] if v < b else BRAND['bull'])
    elif i in [1, 2]:  # Inflation: red if above target
        colors_bar.append(BRAND['bear'] if v > b else BRAND['bull'])
    elif i == 3:  # Unemployment: amber if elevated
        colors_bar.append(BRAND['amber'] if v > b else BRAND['bull'])
    elif i == 4:  # ISM: green if above 50
        colors_bar.append(BRAND['bull'] if v > 50 else BRAND['bear'])
    elif i == 5:  # Sentiment: red if well below average
        colors_bar.append(BRAND['bear'] if v < 70 else BRAND['amber'])
    elif i == 6:  # Fed rate: neutral
        colors_bar.append(BRAND['navy'])
    else:  # HY OAS: green if tight
        colors_bar.append(BRAND['bull'] if v < b else BRAND['amber'])

bars = ax.barh(y_pos, values, color=colors_bar, height=0.55, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}', ha='left', va='center', fontsize=9,
            fontweight='bold', color=BRAND['dark_text'], fontfamily='serif')

ax.set_yticks(y_pos)
ax.set_yticklabels(indicators, fontsize=8)
ax.invert_yaxis()
wilson_style(ax, title='US Macro Dashboard: Key Indicators at a Glance',
             xlabel='',
             source='BEA, BLS, ISM, U. Michigan, Federal Reserve, ICE BofA — as of late Feb 2026')
ax.set_xlim(0, max(values) * 1.2)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-1.0/reports/chart_dashboard.pdf', bbox_inches='tight', dpi=150)
plt.close()

print("All charts generated successfully.")
