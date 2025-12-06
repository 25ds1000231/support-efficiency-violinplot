import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Seaborn Best Practices: Set Style and Context ---
# Set a professional style for the background grid
sns.set_style("whitegrid")
# Set context for presentation-ready text sizes (better for executives/boards)
sns.set_context("talk") 

# --- 2. Data Generation: Create realistic synthetic data ---
np.random.seed(42) # For reproducibility

# Define the support channels
channels = ['Email', 'Live Chat', 'Phone']
data_points = 500 

# Generate data reflecting typical response time efficiency (in minutes):
# Email: High mean, high variability
email_times = np.random.normal(loc=120, scale=40, size=data_points)
# Live Chat: Moderate mean, low variability
chat_times = np.random.normal(loc=15, scale=5, size=data_points)
# Phone: Low mean, very low variability (fastest)
phone_times = np.random.normal(loc=5, scale=2, size=data_points)

# Combine the data into a single DataFrame
df_email = pd.DataFrame({'Response Time (Minutes)': email_times, 'Support Channel': 'Email'})
df_chat = pd.DataFrame({'Response Time (Minutes)': chat_times, 'Support Channel': 'Live Chat'})
df_phone = pd.DataFrame({'Response Time (Minutes)': phone_times, 'Support Channel': 'Phone'})

df = pd.concat([df_email, df_chat, df_phone])

# Ensure all response times are non-negative (clip at 0)
df['Response Time (Minutes)'] = df['Response Time (Minutes)'].clip(lower=0)

# Filter out extreme synthetic outliers for cleaner visualization
df = df[df['Response Time (Minutes)'] < 300]


# --- 3. Create Violinplot and Set Figure Size ---
# Set figure size to 8 inches by 8 inches. 
# At dpi=64, this equals 8 * 64 = 512 pixels.
plt.figure(figsize=(8, 8)) 

# Create the violin plot
sns.violinplot(
    x='Support Channel', 
    y='Response Time (Minutes)', 
    data=df, 
    # Use a color palette optimized for professional reporting
    palette="viridis", 
    # Show median and interquartile range (IQR) for statistical rigor
    inner="quartile",
    linewidth=1 
)

# --- 4. Style the Chart: Titles, Labels, and Ticks ---
plt.title(
    "Customer Support Response Time Distribution by Channel", 
    fontsize=18, 
    weight='bold',
    pad=20 # Add padding to the title to prevent clipping
)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (Minutes)", fontsize=14)

# Set custom y-axis ticks for better readability and focus
plt.yticks(np.arange(0, 301, 50)) 
plt.ylim(0, 250) # Set a limit to focus on the main data distribution

# --- 5. Critical Fix for 512x512 Pixel Accuracy ---
# Manually adjust subplot parameters to eliminate internal margins (whitespace).
plt.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.1) 


# --- 6. Save Chart: Exactly 512x512 pixels ---
plt.savefig(
    'chart.png', 
    dpi=64, 
    # Instructed to use bbox_inches='tight'. 
    # Combined with pad_inches=0.0, this is the most reliable method for exact size.
    bbox_inches='tight',
    pad_inches=0.0 # Crucial: ensures no margin is added to the output image.
) 

plt.close() # Close the figure to free up memory
print("chart.png created successfully and should now be exactly 512x512 pixels.")
