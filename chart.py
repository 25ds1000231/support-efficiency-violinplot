import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style and context for presentations
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Generate realistic synthetic data for support response times (minutes)
np.random.seed(42)
channels = ['Email', 'Chat', 'Phone', 'Social', 'Ticket']
n_samples = 500

data = []
for channel in channels:
    if channel == 'Email':
        # Longer tail for email responses
        times = np.random.exponential(120, n_samples//5) + np.random.normal(60, 20, n_samples//5)
    elif channel == 'Chat':
        # Fastest responses
        times = np.random.exponential(8, n_samples//5) + np.random.normal(5, 2, n_samples//5)
    elif channel == 'Phone':
        # Moderate with some outliers
        times = np.random.exponential(25, n_samples//5) + np.random.normal(15, 8, n_samples//5)
    elif channel == 'Social':
        # Variable social media responses
        times = np.random.exponential(90, n_samples//5) + np.random.normal(45, 25, n_samples//5)
    else:  # Ticket
        # Longest processing
        times = np.random.exponential(240, n_samples//5) + np.random.normal(180, 60, n_samples//5)
    
    times = np.clip(times, 0, 1440)  # Clip to 24 hours max
    for time in times:
        data.append({'Channel': channel, 'Response_Time_Minutes': time})

df = pd.DataFrame(data)

# Create figure exactly 512x512 pixels (8x8 inches at 64 DPI)
fig, ax = plt.subplots(figsize=(8, 8))

# Create violinplot with professional color palette
sns.violinplot(data=df, x='Channel', y='Response_Time_Minutes', 
               palette='Set2', ax=ax, inner='quartile')

# Customize for executive presentation
ax.set_title('Customer Support Response Time Distribution by Channel\n(Minutes)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Response Time (Minutes)', fontsize=12, fontweight='bold')
ax.set_xlabel('Support Channel', fontsize=12, fontweight='bold')

# Rotate x labels for readability
plt.xticks(rotation=45)

# Add value annotations on violins
medians = df.groupby('Channel')['Response_Time_Minutes'].median()
for i, channel in enumerate(channels):
    ax.text(i, medians[channel] + 10, f'Med: {medians[channel]:.0f}min', 
            ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()

# Save EXACTLY 512x512 pixels (8in * 64dpi = 512px)
plt.savefig('chart.png', dpi=64, bbox_inches='tight', pad_inches=0.1)
plt.close()
