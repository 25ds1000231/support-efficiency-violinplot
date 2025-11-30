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
    
    # Create figure - size doesn't matter, we'll resize later
    fig, ax = plt.subplots(figsize=(8, 8))
    
    sns.violinplot(
        data=df,
        x="Tier",
        y="Resolution_Time",
        palette="Set2",
        inner="quartile",
        cut=0,
        ax=ax
    )
    
    ax.set_title("Support Resolution Time by Tier")
    ax.set_xlabel("Support Tier")
    ax.set_ylabel("Resolution Time (hours)")
    
    # Save to temporary file first
    plt.tight_layout()
    plt.savefig("temp_chart.png", dpi=100, bbox_inches='tight')
    plt.close()
    
    # Now use PIL to resize to EXACTLY 512x512
    img = Image.open("temp_chart.png")
    
    # Resize to exact dimensions
    img_resized = img.resize((512, 512), Image.LANCZOS)
    
    # Save final image
    img_resized.save("chart.png")
    
    # Clean up temp file
    import os
    os.remove("temp_chart.png")
    
    print("Chart saved successfully as chart.png (512x512 pixels)")
    
    # Verify dimensions
    final_img = Image.open("chart.png")
    print(f"Final dimensions: {final_img.size[0]} x {final_img.size[1]} pixels")

if __name__ == "__main__":
    main()
