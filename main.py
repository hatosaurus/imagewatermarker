from PIL import Image as PILImage, UnidentifiedImageError
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

watermark_image_path = "watermark/jessicaschmidt_watermark.png"
folder_dir = "raw_images"

# TKinter setup
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()


def add_watermark(raw_image, watermark_image, output_path):
    base_image = PILImage.open(raw_image)
    watermark = PILImage.open(watermark_image)
    # Get base parameters to apply to watermark
    width, height = base_image.size
    # Apply width for both parameters to keep watermark a square
    watermark = watermark.resize((width, width))
    # Find the new size of the watermark
    width_of_watermark, height_of_watermark = watermark.size
    # Centers the watermark on the image
    position = (int(width / 2 - width_of_watermark / 2), int(height / 2 - height_of_watermark / 2))
    # Create new image called transparent, it is the size of our base image
    transparent = PILImage.new('RGBA', (width, height), (0, 0, 0, 0))
    # Paste the base image in at a specific size
    transparent.paste(base_image, (0, 0))
    # Paste the watermark in at a specific size
    transparent.paste(watermark, position, mask=watermark)
    transparent.convert('RGB').save(output_path)
    print(f"Watermarking complete for {raw_image}.")
    return


def find_directory():
    root.directory = filedialog.askdirectory()
    return root.directory


def convert_folder():
    folder = find_directory()
    for image in os.listdir(folder):
        try:
            image_path = f"{folder}/{image}"
            output_path = f"watermarked_images/{image}"
            add_watermark(image_path, watermark_image_path, output_path)
        except PermissionError:
            pass
        except UnidentifiedImageError:
            pass
        except FileNotFoundError:
            pass


ttk.Label(frame, text="Image Converter").grid(column=2, row=0)
ttk.Button(frame, text="Convert Folder", command=convert_folder).grid(column=1, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=3, row=1)
ttk.Button(frame, text="Select Folder to Convert", command=find_directory)


root.mainloop()