import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic support efficiency data
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

# Professional styling with minimal padding for exact dimensions
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.2)
fig, ax = plt.subplots(figsize=(8, 8))

# Violinplot
sns.violinplot(data=df, x='Department', y='Resolution_Time_Hours', 
               palette='Set2', ax=ax)

# Labels and tight layout
ax.set_title('Support Ticket Resolution Time by Department (Hours)')
ax.set_xlabel('Department')
ax.set_ylabel('Resolution Time (Hours)')
ax.tick_params(axis='x', rotation=45)

plt.tight_layout(pad=0.5)
plt.savefig('chart.png', dpi=64, bbox_inches='tight', pad_inches=0, 
            facecolor='white', edgecolor='none')
plt.close()
