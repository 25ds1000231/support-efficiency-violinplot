# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    np.random.seed(42)

    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })

    sns.set_style("whitegrid")
    sns.set_context("talk")

    # EXACT target pixels:
    plt.figure(figsize=(8, 8), dpi=64)

    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0,
    )

    plt.title("Support Resolution Time Distribution by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # Force layout not to resize final pixels
    plt.tight_layout(pad=0)

    # MUST remove bbox_inches otherwise it shrinks!
    plt.savefig("chart.png", dpi=64, pad_inches=0)
    plt.close()


if __name__ == "__main__":
    main()
