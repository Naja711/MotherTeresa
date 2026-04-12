import os
from PIL import Image

def compress_images():
    # Target files: everything ending in .jpeg (renamed ones and logo/principal)
    files = [f for f in os.listdir('.') if f.lower().endswith('.jpeg')]
    
    max_size = (1920, 1920) # Max 1080p width/height
    quality = 75 # Standard web quality
    
    print(f"Starting compression of {len(files)} files...\n")
    
    total_reduction = 0
    
    for filename in files:
        file_path = filename
        initial_size = os.path.getsize(file_path)
        
        try:
            with Image.open(file_path) as img:
                # Convert to RGB (in case of RGBA)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                # Resize if larger than max_size
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Save compressed version
                img.save(file_path, "JPEG", quality=quality, optimize=True)
                
            final_size = os.path.getsize(file_path)
            reduction = initial_size - final_size
            total_reduction += reduction
            
            print(f"{filename}: {initial_size/1024/1024:.2f}MB -> {final_size/1024/1024:.2f}MB (Reduced {reduction/1024/1024:.2f}MB)")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"\nOptimization complete!")
    print(f"Total Disk Space Saved: {total_reduction/1024/1024:.2f}MB")

if __name__ == "__main__":
    compress_images()
