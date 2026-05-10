import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────

months  = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [4500, 5200, 4800, 6100, 5900, 7200]

components = ['Sensors', 'Motors', 'PLCs']
units      = [120, 85, 40]

# ─────────────────────────────────────────────
# CHART 1: LINE PLOT — Revenue Trend
# ─────────────────────────────────────────────

plt.figure(figsize=(10, 5))

plt.plot(months, revenue,
         color='forestgreen',
         marker='*',
         linewidth=2.5,
         label='Revenue (RM)')

peak_value = max(revenue)
peak_index = revenue.index(peak_value)
peak_month = months[peak_index]


plt.annotate(
    'Maximum Performance',
    xy=(peak_index, peak_value),         
    xytext=(peak_index - 1.5, peak_value - 600),  
    arrowprops=dict(arrowstyle='->', color='red', lw=2),
    fontsize=11,
    color='red',
    fontweight='bold'
)

plt.title('Revenue Trend — 6 Months', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Revenue (RM)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('revenue_trend.png')
plt.show()

print(f"Peak Month: {peak_month} → RM {peak_value}")

# ─────────────────────────────────────────────
# CHART 2: BAR CHART — Units Sold
# ─────────────────────────────────────────────

plt.figure(figsize=(8, 5))

bars = plt.bar(components, units,
               color=['steelblue', 'orange', 'tomato'],
               width=0.5)


for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 1.5,
             str(int(bar.get_height())),
             ha='center', fontweight='bold')


plt.title('Units Sold by Component', fontsize=14, fontweight='bold')
plt.xlabel('Component')
plt.ylabel('Units Sold')
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('units_sold.png')
plt.show()

print("\n=== DAY 9 COMPLETE ===")
print("Line Plot   → revenue_trend.png")
print("Bar Chart   → units_sold.png")