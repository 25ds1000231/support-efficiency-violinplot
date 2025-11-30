import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data for support efficiency analysis
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
    else:  # Finance
        times = np.random.normal(5.0, 1.0, 200)
    times = np.maximum(times, 0)  # No negative times
    for t in times:
        data.append({'Department': dept, 'Resolution_Time_Hours': t})

df = pd.DataFrame(data)

# Professional Seaborn styling
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.2)

# Create figure exactly 8x8 inches for 512x512 at dpi=64
plt.figure(figsize=(8, 8))

# Violinplot with professional palette
sns.violinplot(data=df, x='Department', y='Resolution_Time_Hours', palette='Set2')

# Labels and title
plt.title('Support Ticket Resolution Time by Department (Hours)')
plt.xlabel('Department')
plt.ylabel('Resolution Time (Hours)')
plt.xticks(rotation=45)

# Save as exactly 512x512 PNG
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white')
plt.close()
