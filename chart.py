import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
from PIL import Image

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------
# Data Generation (Realistic)
# ------------------------------

np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

email_times = np.random.lognormal(mean=np.log(35), sigma=0.4, size=250)
chat_times = np.random.gamma(shape=4, scale=3, size=250)
phone_times = np.random.normal(loc=22, scale=6, size=250)
phone_times += np.abs(np.random.normal(0, 4, size=250)) * 0.3
fast_auto = np.random.normal(loc=10, scale=3, size=150)
slow_human = np.random.normal(loc=45, scale=12, size=100)
social_times = np.concatenate([fast_auto, slow_human])

df = pd.DataFrame({
    "Channel": np.repeat(channels, 250),
    "ResponseTime": np.concatenate([
        email_times, chat_times, phone_times, social_times
    ])
})

df["ResponseTime"] = df["ResponseTime"].clip(lower=0)

# ------------------------------
# Seaborn Styling
# ------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")

# ------------------------------
# Create Violin Plot
# ------------------------------

g = sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    cut=0,
    bw=0.25,
    linewidth=1.2,
)

plt.title(
    "Customer Support Response Time Distribution by Channel",
    fontsize=18, fontweight="bold"
)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# ------------------------------
# Adjust Figure Size for EXACT 512x512
# ------------------------------

fig = g.figure
fig.set_size_inches(5.12, 5.12)  # 5.12 inches × 100 dpi = 512 px

# ------------------------------
# Save Chart
# ------------------------------

plt.savefig("seaborn_relplot_512x512.png", dpi=100, bbox_inches='tight')
plt.show()

print("Chart saved as seaborn_relplot_512x512.png (exac
