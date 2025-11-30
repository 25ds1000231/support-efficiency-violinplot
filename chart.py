# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def main():
    # -------------------------
    # 1. Generate synthetic data
    # -------------------------
    np.random.seed(42)

    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })

    # -------------------------
    # 2. Plot (any size is OK)
    # -------------------------
    sns.set_style("whitegrid")
    sns.set_context("talk")

    plt.figure(figsize=(6, 6))   # size doesn't matter anymore

    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0
    )

    plt.title("Support Resolution Time Distribution by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # Save temporary image
    tmp_file = "chart_temp.png"
    plt.savefig(tmp_file, dpi=100)
    plt.close()

    # -------------------------
    # 3. FORCE EXACT SIZE 512×512
    # -------------------------
    img = Image.open(tmp_file)
    img = img.resize((512, 512), Image.LANCZOS)
    img.save("chart.png")

    print("Generated chart.png (512x512) successfully.")

if __name__ == "__main__":
    main()
