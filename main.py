from converter import *
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import UnidentifiedImageError
import os


root = Tk()
root.title("Image Watermarking")
root.geometry("400x250")
frame = ttk.Frame(root, padding=10)
frame.grid()


frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

chosen_directory = ""


def find_directory():
    global chosen_directory
    root.directory = filedialog.askdirectory()
    chosen_directory = root.directory
    return chosen_directory


def convert_folder():
    folder = chosen_directory
    if folder == "":
        messagebox.showerror("Error", "Select a folder.")
    output_path = "watermarked_images"
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
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


ttk.Label(frame, text="Image Watermarking").grid(column=1, row=0, columnspan=1)
ttk.Button(frame, text="Select Folder", command=find_directory).grid(column=0, row=2)
ttk.Button(frame, text="Watermark All", command=convert_folder).grid(column=2, row=2)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=3)

root.mainloop()