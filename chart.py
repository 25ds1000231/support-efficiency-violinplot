# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


def generate_synthetic_data(n_samples=500):
    np.random.seed(42)

    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })
    return df


def create_violinplot(df):
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # create any size figure – we will resize later
    plt.figure(figsize=(6, 6))

    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0
    )

    plt.title("Support Resolution Time by Tier")
    plt.xlabel("Support Tier")
    plt.ylabel("Resolution Time (hours)")

    # save temporary image
    temp_file = "chart_temp.png"
    plt.savefig(temp_file, dpi=100)
    plt.close()

    # force resize to EXACTLY 512×512
    img = Image.open(temp_file)
    img = img.resize((512, 512), Image.LANCZOS)
    img.save("chart.png")


def main():
    df = generate_synthetic_data()
    create_violinplot(df)
    print("chart.png generated successfully – 512x512")


if __name__ == "__main__":
    main()
