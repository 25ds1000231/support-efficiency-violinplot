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
    
    # Set figure size to EXACTLY 512 pixels (512/100 DPI = 5.12 inches)
    fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)
    
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
    
    # DON'T use tight_layout or bbox_inches - they change dimensions!
    # Save directly without any bbox adjustments
    plt.savefig("chart.png", dpi=100)
    plt.close()
    
    # Now verify and force resize if needed
    img = Image.open("chart.png")
    width, height = img.size
    
    print(f"Initial save dimensions: {width} x {height} pixels")
    
    if width != 512 or height != 512:
        print(f"Resizing from {width}x{height} to 512x512...")
        # Force exact size
        img = img.resize((512, 512), Image.LANCZOS if hasattr(Image, 'LANCZOS') else 1)
        img.save("chart.png")
        print("Resized and saved!")
    
    # Final verification
    final_img = Image.open("chart.png")
    print(f"FINAL dimensions: {final_img.size[0]} x {final_img.size[1]} pixels")

if __name__ == "__main__":
    main()
