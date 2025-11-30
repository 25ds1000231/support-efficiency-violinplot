import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Support efficiency data
np.random.seed(42)
departments = ['Sales', 'IT', 'HR', 'Finance']
data = []
for dept in departments:
    if dept == 'IT': times = np.random.normal(2.5, 0.8, 200)
    elif dept == 'Sales': times = np.random.normal(4.0, 1.2, 200)
    elif dept == 'HR': times = np.random.normal(6.0, 1.5, 200)
    else: times = np.random.normal(5.0, 1.0, 200)
    times = np.maximum(times, 0)
    for t in times: data.append({'Department': dept, 'Resolution_Time_Hours': t})

df = pd.DataFrame(data)

# FIXED: Manual margins, NO tight/bbox_inches
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.1)
fig = plt.figure(figsize=(8, 8), dpi=64)  # Lock DPI at figure creation

sns.violinplot(data=df, x='Department', y='Resolution_Time_Hours', palette='Set2')
plt.title('Support Ticket Resolution Time by Department (Hours)', pad=15)
plt.xlabel('Department')
plt.ylabel('Resolution Time (Hours)')
plt.xticks(rotation=45)

# PRECISE margins = EXACT 512x512
plt.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.18)
plt.savefig('chart.png', pad_inches=0, facecolor='white')  # NO bbox_inches='tight'!
plt.close()

# FORCE VERIFY 512x512
img = Image.open('chart.png')
if img.size != (512, 512):
    img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_resized.save('chart.png')
    print(f"RESIZED to 512x512: {img_resized.size}")
else:
    print(f"PERFECT 512x512: {img.size}")
