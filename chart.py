# chart.py
# Email: 25ds1000231@ds.study.iitm.ac.in
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import sys

def main():
    print("Starting chart generation...")
    
    try:
        np.random.seed(42)
        df = pd.DataFrame({
            "Tier": np.random.choice(["Tier 1", "Tier 2", "Tier 3"], 500),
            "Resolution_Time": np.random.lognormal(mean=1.5, sigma=0.5, size=500)
        })
        
        print("Data created successfully")
        
        sns.set_style("whitegrid")
        sns.set_context("talk")
        
        # Create figure
        fig, ax = plt.subplots(figsize=(8, 8))
        
        print("Creating violin plot...")
        
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
        
        plt.tight_layout()
        
        print("Saving temporary chart...")
        
        # Save to temporary file
        plt.savefig("temp_chart.png", dpi=100)
        plt.close()
        
        print("Opening image with PIL...")
        
        # Open with PIL and FORCE resize to 512x512
        img = Image.open("temp_chart.png")
        original_size = img.size
        print(f"Original temp image size: {original_size[0]} x {original_size[1]}")
        
        # Resize using different method based on PIL version
        print("Resizing to 512x512...")
        try:
            img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
        except AttributeError:
            try:
                img_512 = img.resize((512, 512), Image.LANCZOS)
            except:
                img_512 = img.resize((512, 512), 1)
        
        print(f"Resized image size in memory: {img_512.size[0]} x {img_512.size[1]}")
        
        # Save the resized image
        print("Saving final chart.png...")
        img_512.save("chart.png", "PNG")
        
        # Close images
        img.close()
        img_512.close()
        
        # Delete temp file
        import os
        if os.path.exists("temp_chart.png"):
            os.remove("temp_chart.png")
            print("Temp file deleted")
        
        # Verify final size
        print("Verifying saved file...")
        with Image.open("chart.png") as verify:
            w, h = verify.size
            print(f"\n{'='*50}")
            print(f"Chart saved as chart.png")
            print(f"Dimensions: {w} x {h} pixels")
            print(f"{'='*50}")
            
            if w == 512 and h == 512:
                print("SUCCESS: Image is exactly 512x512 pixels!")
                return 0
            else:
                print(f"WARNING: Image is {w}x{h}, not 512x512")
                return 1
                
    except Exception as e:
        print(f"\nERROR occurred: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
