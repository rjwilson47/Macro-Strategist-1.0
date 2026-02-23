"""
Wilson's Multi-Asset Research — Matplotlib Brand Template
Import this module or copy the BRAND dict and wilson_style() function into chart scripts.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Wilson's brand colours
BRAND = {
    'navy': '#1B2A4A',
    'accent': '#2E86AB',
    'gold': '#D4A843',
    'light_grey': '#F2F4F7',
    'mid_grey': '#6B7280',
    'dark_text': '#1F2937',
    'bull': '#059669',
    'bear': '#DC2626',
    'amber': '#D97706',
}

def wilson_style(ax, title='', xlabel='', ylabel='', source=''):
    """Apply Wilson's brand styling to a matplotlib axis."""
    ax.set_facecolor('white')
    ax.figure.set_facecolor('white')
    ax.set_title(title, fontsize=12, fontweight='bold', color=BRAND['navy'], pad=12, fontfamily='serif')
    ax.set_xlabel(xlabel, fontsize=9, color=BRAND['dark_text'], fontfamily='serif')
    ax.set_ylabel(ylabel, fontsize=9, color=BRAND['dark_text'], fontfamily='serif')
    ax.tick_params(colors=BRAND['dark_text'], labelsize=8)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontfamily('serif')
    ax.grid(True, alpha=0.3, color=BRAND['mid_grey'], linestyle='-', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(BRAND['mid_grey'])
    ax.spines['bottom'].set_color(BRAND['mid_grey'])
    if source:
        ax.figure.text(0.95, 0.01, f'Source: {source}',
                       ha='right', fontsize=6.5, color=BRAND['mid_grey'], style='italic', fontfamily='serif')

# Example usage:
# fig, ax = plt.subplots(figsize=(8, 4.5))
# ax.bar(['A', 'B', 'C'], [10, 20, 15], color=BRAND['navy'])
# wilson_style(ax, title='Example Chart', ylabel='Value', source='FactSet, Feb 2026')
# plt.tight_layout()
# plt.savefig('chart.pdf', bbox_inches='tight', dpi=150)
# plt.close()
