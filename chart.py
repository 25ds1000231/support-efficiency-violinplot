# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def main():
    np.random.seed(42)

    df = pd.DataFrame({
        "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
        "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
    })

    sns.set_style("whitegrid")
    sns.set_context("talk")

    # Any size is fine temporarily
    fig, ax = plt.subplots(figsize=(6, 6))

    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0
    )

    ax.set_title("Support Resolution Time by Tier")
    ax.set_xlabel("Support Tier")
    ax.set_ylabel("Resolution Time (hours)")

    fig.canvas.draw()

    # Convert to a Pillow image
    img = Image.frombytes(
        "RGB",
        fig.canvas.get_width_height(),
        fig.canvas.tostring_rgb()
    )

    plt.close(fig)

    # NOW we force the final size EXACTLY
    img = img.resize((512, 512), Image.LANCZOS)
    img.save("chart.png")

if __name__ == "__main__":
    main()
