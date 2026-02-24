"""
Generate charts for the Australia Economic Outlook report.
Wilson's Multi-Asset Research — February 2026
"""
import sys
sys.path.insert(0, '/home/user/Macro-Strategist-1.0')

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from wilson_charts import BRAND, wilson_style

OUTDIR = '/home/user/Macro-Strategist-1.0/reports'

# Load chart data
with open(f'{OUTDIR}/chart_data/2026-02-23-australia-macro-outlook-economic.json') as f:
    data = json.load(f)

# ═══════════════════════════════════════════════════════════════
# CHART 1: Australia GDP Growth — Quarterly (q/q) and Year-on-Year
# ═══════════════════════════════════════════════════════════════
fig, ax1 = plt.subplots(figsize=(8, 4.5))
d = data['charts']['chart_gdp_growth']['data']
x = np.arange(len(d['labels']))
width = 0.35

bars = ax1.bar(x - width/2, d['values'], width, color=BRAND['navy'], label='QoQ Growth (%)', edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, d['values']):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 0.03, f'{val:.1f}%',
             ha='center', va='bottom', fontsize=9, fontweight='bold', color=BRAND['dark_text'], fontfamily='serif')

ax2 = ax1.twinx()
ax2.plot(x, d['yoy_values'], color=BRAND['accent'], linewidth=2.5, marker='o', markersize=7, label='YoY Growth (%)')
for xi, val in zip(x, d['yoy_values']):
    ax2.text(xi + 0.05, val + 0.1, f'{val:.1f}%', ha='left', va='bottom', fontsize=8,
             color=BRAND['accent'], fontfamily='serif', fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels(d['labels'], fontsize=9, fontfamily='serif')
ax1.set_ylim(0, 1.0)
ax2.set_ylim(0, 3.0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color(BRAND['accent'])
ax2.tick_params(axis='y', colors=BRAND['accent'], labelsize=8)
for label in ax2.get_yticklabels():
    label.set_fontfamily('serif')
ax2.set_ylabel('YoY Growth (%)', fontsize=9, color=BRAND['accent'], fontfamily='serif')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=8, frameon=False, loc='upper left')

wilson_style(ax1, title='Australia Real GDP Growth (2024-2025)',
             ylabel='QoQ Growth (%)',
             source='ABS National Accounts, as of Sep Q 2025')
plt.tight_layout()
plt.savefig(f'{OUTDIR}/au_chart_gdp_growth.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 2: Inflation — Headline CPI vs Trimmed Mean + RBA Forecasts
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))
d = data['charts']['chart_inflation']['data']

# Actual data
x_actual = np.arange(len(d['labels']))
ax.plot(x_actual, d['headline'], color=BRAND['navy'], linewidth=2.5, marker='o', markersize=6, label='Headline CPI (actual)')
ax.plot(x_actual, d['trimmed_mean'], color=BRAND['accent'], linewidth=2.5, marker='s', markersize=6, label='Trimmed Mean (actual)')

# Forecasts
n_actual = len(d['labels'])
x_forecast = np.arange(n_actual, n_actual + len(d['forecast_labels']))
ax.plot(x_forecast, d['forecast_headline'], color=BRAND['navy'], linewidth=2, marker='o', markersize=5,
        linestyle='--', alpha=0.7, label='Headline CPI (RBA f/c)')
ax.plot(x_forecast, d['forecast_trimmed'], color=BRAND['accent'], linewidth=2, marker='s', markersize=5,
        linestyle='--', alpha=0.7, label='Trimmed Mean (RBA f/c)')

# Target band
all_x = np.concatenate([x_actual, x_forecast])
ax.fill_between([all_x[0] - 0.5, all_x[-1] + 0.5], 2.0, 3.0, alpha=0.12, color=BRAND['bull'], label='RBA Target Band (2-3%)')
ax.axhline(y=2.5, color=BRAND['bull'], linewidth=0.8, linestyle=':', alpha=0.5)

# Vertical line separating actual from forecast
ax.axvline(x=n_actual - 0.5, color=BRAND['mid_grey'], linewidth=1, linestyle=':', alpha=0.7)
ax.text(n_actual - 0.3, 4.35, 'Forecast \u2192', fontsize=8, color=BRAND['mid_grey'], fontfamily='serif', style='italic')

all_labels = d['labels'] + d['forecast_labels']
ax.set_xticks(np.arange(len(all_labels)))
ax.set_xticklabels(all_labels, fontsize=7.5, rotation=30, ha='right')
ax.legend(fontsize=7.5, frameon=False, loc='upper right', ncol=2)
wilson_style(ax, title='Australia Inflation: Actual and RBA Forecasts (Year-Ended, %)',
             ylabel='% Year-over-Year',
             source='ABS CPI, RBA SMP February 2026')
ax.set_ylim(1.5, 4.8)
ax.set_xlim(-0.5, len(all_labels) - 0.5)
plt.tight_layout()
plt.savefig(f'{OUTDIR}/au_chart_inflation.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 3: RBA Cash Rate Path — Actual + Market-Implied
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
d = data['charts']['chart_rba_rate']['data']

n_actual = d['actual_count']
x_all = np.arange(len(d['labels']))

# Actual (step)
ax.step(x_all[:n_actual], d['values'][:n_actual], where='post', color=BRAND['navy'], linewidth=2.5, label='Actual Cash Rate')
ax.plot(x_all[:n_actual], d['values'][:n_actual], 'o', color=BRAND['navy'], markersize=6)

# Market-implied (dashed)
ax.plot(x_all[n_actual-1:], d['values'][n_actual-1:], color=BRAND['gold'], linewidth=2.2, linestyle='--',
        marker='D', markersize=6, label='Market-Implied Path')

# Annotate key points
for i, (label, val) in enumerate(zip(d['labels'], d['values'])):
    offset_y = 0.07 if i % 2 == 0 else -0.12
    ax.text(i, val + offset_y, f'{val:.2f}%', ha='center', va='bottom' if offset_y > 0 else 'top',
            fontsize=8, fontweight='bold', color=BRAND['dark_text'], fontfamily='serif')

ax.axvline(x=n_actual - 0.5, color=BRAND['mid_grey'], linewidth=1, linestyle=':', alpha=0.7)
ax.text(n_actual + 0.1, 3.45, 'Market\npricing', fontsize=7.5, color=BRAND['mid_grey'], fontfamily='serif', style='italic')

ax.set_xticks(x_all)
ax.set_xticklabels(d['labels'], fontsize=8)
ax.legend(fontsize=8, frameon=False, loc='lower left')
wilson_style(ax, title='RBA Cash Rate: Actual and Market-Implied Path',
             ylabel='Cash Rate (%)',
             source='RBA, ASX Rate Tracker, as of Feb 2026')
ax.set_ylim(3.3, 4.5)
plt.tight_layout()
plt.savefig(f'{OUTDIR}/au_chart_rba_rate.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 4: Australian Yield Curve — Current vs 3m ago vs 1y ago
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
d = data['charts']['chart_yield_curve']['data']

x = np.arange(len(d['tenors']))
ax.plot(x, d['current'], color=BRAND['navy'], linewidth=2.5, marker='o', markersize=7, label='Current (20 Feb 2026)')
ax.plot(x, d['3m_ago'], color=BRAND['accent'], linewidth=2, marker='s', markersize=6, label='3 Months Ago (~Nov 2025)')
ax.plot(x, d['1y_ago'], color=BRAND['gold'], linewidth=2, marker='^', markersize=6, label='1 Year Ago (~Feb 2025)')

for i, (c, m3, m12) in enumerate(zip(d['current'], d['3m_ago'], d['1y_ago'])):
    ax.text(i, c + 0.04, f'{c:.2f}', ha='center', va='bottom', fontsize=8, fontweight='bold',
            color=BRAND['navy'], fontfamily='serif')

ax.set_xticks(x)
ax.set_xticklabels(d['tenors'], fontsize=10, fontweight='bold')
ax.legend(fontsize=8, frameon=False, loc='lower right')
wilson_style(ax, title='Australian Government Bond Yield Curve',
             ylabel='Yield (%)',
             source='Trading Economics, CEIC, as of 20 Feb 2026')
ax.set_ylim(3.5, 5.2)
plt.tight_layout()
plt.savefig(f'{OUTDIR}/au_chart_yield_curve.pdf', bbox_inches='tight', dpi=150)
plt.close()

# ═══════════════════════════════════════════════════════════════
# CHART 5: Consumer Sentiment
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))
d = data['charts']['chart_consumer_sentiment']['data']

x = np.arange(len(d['labels']))
colors = [BRAND['bull'] if v >= 100 else BRAND['bear'] for v in d['values']]
ax.bar(x, d['values'], color=colors, width=0.6, edgecolor='white', linewidth=0.5)
ax.axhline(y=100, color=BRAND['mid_grey'], linewidth=1.5, linestyle='--', alpha=0.8)
ax.text(len(x) - 0.5, 101.5, 'Neutral (100)', fontsize=8, color=BRAND['mid_grey'], ha='right', fontfamily='serif')

for i, val in enumerate(d['values']):
    ax.text(i, val + 1, f'{val:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold',
            color=BRAND['dark_text'], fontfamily='serif')

ax.set_xticks(x)
ax.set_xticklabels(d['labels'], fontsize=8.5)
wilson_style(ax, title='Westpac-Melbourne Institute Consumer Sentiment Index',
             ylabel='Index Level',
             source='Westpac IQ, as of Feb 2026')
ax.set_ylim(75, 115)
plt.tight_layout()
plt.savefig(f'{OUTDIR}/au_chart_consumer_sentiment.pdf', bbox_inches='tight', dpi=150)
plt.close()

print("All Australian charts generated successfully.")
