# chart.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Seaborn Best Practices: Set Style and Context ---
# Set a professional style (e.g., 'whitegrid' for better readability)
sns.set_style("whitegrid")
# Set context for presentation-ready text size
sns.set_context("talk") # 'talk' or 'poster' is great for presentations

# --- 2. Data Generation: Create realistic synthetic data ---
np.random.seed(42) # For reproducibility

# Define the support channels and their typical response time distributions (in minutes)
channels = ['Email', 'Live Chat', 'Phone']
data_points = 500 # Total number of response times

# Generate data for each channel reflecting typical efficiency:
# Phone is usually fastest, Live Chat moderate, Email slowest/most variable
email_times = np.random.normal(loc=120, scale=40, size=data_points)
chat_times = np.random.normal(loc=15, scale=5, size=data_points)
phone_times = np.random.normal(loc=5, scale=2, size=data_points)

# Combine the data into a single DataFrame
df_email = pd.DataFrame({'Response Time (Minutes)': email_times, 'Support Channel': 'Email'})
df_chat = pd.DataFrame({'Response Time (Minutes)': chat_times, 'Support Channel': 'Live Chat'})
df_phone = pd.DataFrame({'Response Time (Minutes)': phone_times, 'Support Channel': 'Phone'})

df = pd.concat([df_email, df_chat, df_phone])

# Ensure all response times are non-negative
df['Response Time (Minutes)'] = df['Response Time (Minutes)'].apply(lambda x: max(0, x))

# Filter out extreme outliers for cleaner visualization (e.g., email times > 300 mins)
df = df[df['Response Time (Minutes)'] < 300]


# --- 3. Create Violinplot and Set Figure Size ---
# Set figure size for the required 512x512 pixel output. 
# At default DPI (100), 5.12x5.12 inches would work. To use dpi=64, we need:
# 512 pixels / 64 dpi = 8 inches.
plt.figure(figsize=(8, 8)) 

# Create the violin plot
# 'hue' is not needed here. Use 'x' for channel and 'y' for time.
# 'palette' for professional colors. 'inner="quartile"' shows the median and IQR.
sns.violinplot(
    x='Support Channel', 
    y='Response Time (Minutes)', 
    data=df, 
    palette="viridis", # A good professional, sequential palette
    inner="quartile",
    linewidth=1 # Thicker lines for better appearance
)

# --- 4. Style the Chart: Titles, Labels, and Ticks ---
plt.title(
    "Customer Support Response Time Distribution by Channel", 
    fontsize=18, 
    weight='bold'
)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (Minutes)", fontsize=14)

# Set specific y-axis limits to focus on the key distribution
# plt.ylim(0, 300) 

# --- 5. Save Chart: Exactly 512x512 pixels ---
# dpi=64 and figsize=(8, 8) ensures 8*64 = 512 pixels.
# bbox_inches='tight' often crops white space, which can interfere with exact pixel size. 
# A more reliable way for exact size is to manually set the figure size and save without 'tight',
# but the requirement states to use 'bbox_inches='tight'. We will follow the instruction:
plt.savefig(
    'chart.png', 
    dpi=64, 
    bbox_inches='tight' # Following instruction, though it might cause a slight deviation if content is too large
) 

plt.close() # Close the figure to free up memory
print("chart.png created successfully with target 512x512 pixel dimensions.")
