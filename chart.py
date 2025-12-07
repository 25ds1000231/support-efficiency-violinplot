import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8)

# Generate realistic synthetic support response time data (minutes)
np.random.seed(42)
channels = ['Email', 'Chat', 'Phone', 'Social', 'Ticket']
n_samples = 400

data = []
for channel in channels:
    if channel == 'Email':
        times = np.random.exponential(100, n_samples//5) + 40
    elif channel == 'Chat':
        times = np.random.exponential(5, n_samples//5) + 3
    elif channel == 'Phone':
        times = np.random.exponential(20, n_samples//5) + 12
    elif channel == 'Social':
        times = np.random.exponential(70, n_samples//5) + 30
    else:  # Ticket
        times = np.random.exponential(200, n_samples//5) + 150
    
    times = np.clip(times, 0, 1200)
    for time in times:
        data.append({'Channel': channel, 'Response_Time_Minutes': time})

df = pd.DataFrame(data)

# Create figure EXACTLY for 512x512 output
plt.figure(figsize=(8, 8))

# CRITICAL: Direct sns.violinplot() call - no ax parameter, no subplots
sns.violinplot(data=df, x='Channel', y='Response_Time_Minutes', 
               palette='Set2', inner='box')

# Executive presentation styling
plt.title('Customer Support Response Times by Channel\n(Minutes to First Response)', 
          fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Response Time (Minutes)', fontsize=14, fontweight='bold')
plt.xlabel('Support Channel', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Tight layout for clean edges
plt.tight_layout(pad=1.5)

# Save EXACTLY 512x512 pixels: 8in × 64dpi = 512px
plt.savefig('chart.png', dpi=64, bbox_inches='tight', pad_inches=0.1, 
            facecolor='white', edgecolor='none')
plt.close()
