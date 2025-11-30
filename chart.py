import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic support efficiency data - IT fastest, HR slowest
np.random.seed(42)
departments = ['Sales', 'IT', 'HR', 'Finance']
data = []
for dept in departments:
    if dept == 'IT':
        times = np.random.normal(2.5, 0.8, 200)
    elif dept == 'Sales':
        times = np.random.normal(4.0, 1.2, 200)
    elif dept == 'HR':
        times = np.random.normal(6.0, 1.5, 200)
    else:
        times = np.random.normal(5.0, 1.0, 200)
    times = np.maximum(times, 0)
    for t in times:
        data.append({'Department': dept, 'Resolution_Time_Hours': t})

df = pd.DataFrame(data)

# Exact Seaborn styling - NO manual resizing
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.2)

# 8x8 inches @ 64 DPI = exactly 512x512 pixels
plt.figure(figsize=(8, 8))

# PURE sns.violinplot - no ax= or subplots interference
sns.violinplot(data=df, x='Department', y='Resolution_Time_Hours', palette='Set2')

plt.title('Support Ticket Resolution Time by Department (Hours)')
plt.xlabel('Department')
plt.ylabel('Resolution Time (Hours)')
plt.xticks(rotation=45)

# Critical: tight_layout BEFORE savefig, minimal padding
plt.tight_layout(pad=0.2)
plt.savefig('chart.png', dpi=64, bbox_inches='tight', pad_inches=0.1, 
            facecolor='white', edgecolor='none')
plt.close()

print("Generated chart.png - Verify: PIL.Image.open('chart.png').size == (512, 512)")
