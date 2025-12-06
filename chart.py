import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Seaborn Best Practices: Set Style and Context ---
sns.set_style("whitegrid")
sns.set_context("talk") 

# --- 2. Data Generation: Create realistic synthetic data ---
np.random.seed(42) # For reproducibility

channels = ['Email', 'Live Chat', 'Phone']
data_points = 500 

# Generate data reflecting typical response time efficiency (in minutes):
email_times = np.random.normal(loc=120, scale=40, size=data_points)
chat_times = np.random.normal(loc=15, scale=5, size=data_points)
phone_times = np.random.normal(loc=5, scale=2, size=data_points)

# Combine the data into a single DataFrame
df_email = pd.DataFrame({'Response Time (Minutes)': email_times, 'Support Channel': 'Email'})
df_chat = pd.DataFrame({'Response Time (Minutes)': chat_times, 'Support Channel': 'Live Chat'})
df_phone = pd.DataFrame({'Response Time (Minutes)': phone_times, 'Support Channel': 'Phone'})

df = pd.concat([df_email, df_chat, df_phone])

# Ensure all response times are non-negative
df['Response Time (Minutes)'] = df['Response Time (Minutes)'].clip(lower=0)

# Filter out extreme synthetic outliers for cleaner visualization
df = df[df['Response Time (Minutes)'] < 300]


# --- 3. Create Violinplot and Set Figure Size ---
# Set figure size to 8 inches by 8 inches. 
# At dpi=64, this exactly equals 8 * 64 = 512 pixels.
plt.figure(figsize=(8, 8)) 

# Create the violin plot
sns.violinplot(
    x='Support Channel', 
    y='Response Time (Minutes)', 
    data=df, 
    palette="viridis", 
    inner="quartile",
    linewidth=1 
)

# --- 4. Style the Chart: Titles, Labels, and Ticks ---
plt.title(
    "Customer Support Response Time Distribution by Channel", 
    fontsize=18, 
    weight='bold',
    pad=20 
)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (Minutes)", fontsize=14)

# Set custom y-axis limits for better focus
plt.ylim(0, 250) 

# --- 5. Critical Fix for 512x512 Pixel Accuracy ---
# Manually adjust subplot parameters to eliminate internal margins (whitespace) 
# that are often added by Matplotlib, which prevent exact sizing.
# The values below are optimized to fill the 8x8 figure area.
plt.subplots_adjust(left=0.10, right=0.95, top=0.90, bottom=0.10) 


# --- 6. Save Chart: Exactly 512x512 pixels ---
# Save using the precise dpi and setting pad_inches=0.0 to strip any remaining external padding.
# The problematic bbox_inches='tight' parameter is explicitly excluded for this attempt.
plt.savefig(
    'chart.png', 
    dpi=64, 
    pad_inches=0.0 # Ensures no margin is added to the image file itself
) 

plt.close() 
print("chart.png created successfully. Please verify it is exactly 512x512 pixels.")
