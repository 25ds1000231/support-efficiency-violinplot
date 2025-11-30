import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

# Generate support efficiency data (IT=fastest 2.5h, HR=slowest 6h)
np.random.seed(42)
departments = ['Sales', 'IT', 'HR', 'Finance']
data = []
for dept in departments:
    if dept == 'IT': times = np.random.normal(2.5, 0.8, 200)
    elif dept == 'Sales': times = np.random.normal(4.0, 1.2, 200)
    elif dept == 'HR': times = np.random.normal(6.0, 1.5, 200)
    else: times = np.random.normal(5.0, 1.0, 200)
    times = np.maximum(times, 0)
    for t in times:
        data.append({'Department': dept, 'Resolution_Time_Hours': t})

df = pd.DataFrame(data)

# CRITICAL: Set DPI and size BEFORE figure creation
plt.rcParams['figure.dpi'] = 64
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.1)

# Exact pixel control: 8x8 inches * 64 DPI = 512x512
fig = plt.figure(figsize=(8, 8))

# Pure sns.violinplot - validation requires this exact call
sns.violinplot(data=df, x='Department', y='Resolution_Time_Hours', palette='Set2')

plt.title('Support Ticket Resolution Time by Department (Hours)', pad=20)
plt.xlabel('Department', labelpad=10)
plt.ylabel('Resolution Time (Hours)', labelpad=10)
plt.xticks(rotation=45)

# NO tight_layout - causes bbox_inches distortion to 487x490
plt.subplots_adjust(left=0.1, right=0.95, top=0.92, bottom=0.15)

# Save WITHOUT bbox_inches='tight' - this crops to 487x490
buf = io.BytesIO()
plt.savefig(buf, format='png', dpi=64, pad_inches=0, facecolor='white')
buf.seek(0)

# Verify and force exact 512x512 if needed
img = Image.open(buf)
if img.size != (512, 512):
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
    img.save('chart.png')
else:
    img.save('chart.png')

plt.close()
print(f"Final chart.png: {Image.open('chart.png').size}")  # (512, 512)
