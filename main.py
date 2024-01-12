from converter import *
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import UnidentifiedImageError, Image, ImageTk
import os

root = Tk()
root.title("Image Watermark")
root.geometry("550x350")

frame = ttk.Frame(root, padding=10)
frame.grid(sticky="nsew")

frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

root.grid_rowconfigure((0, 1, 2, 3), weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

chosen_directory = ""
watermark_image = ""


def find_directory():
    global chosen_directory
    root.directory = filedialog.askdirectory()
    chosen_directory = root.directory
    return chosen_directory


def convert_folder():
    folder = chosen_directory
    watermark = watermark_image
    if folder == "":
        messagebox.showerror("Error", "Select a folder.")
        return
    if watermark == "":
        messagebox.showerror("Error", "Select a watermark image.")
        return
    output_path = "watermarked_images"
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    for image in os.listdir(folder):
        try:
            image_path = f"{folder}/{image}"
            output_path = f"watermarked_images/{image}"
            add_watermark(image_path, watermark_image, output_path)
        except PermissionError:
            pass
        except UnidentifiedImageError:
            pass
        except FileNotFoundError:
            pass


def choose_watermark():
    global watermark_image
    watermark_image = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png")]
    )
    return watermark_image


logo = Image.open("logo/watermark_logo.png")
logo_render = ImageTk.PhotoImage(logo)

logo = ttk.Label(frame, image=logo_render)
logo.grid(column=1, row=0, columnspan=2, sticky="nsew")

select_folder = ttk.Button(frame, text="Select Folder", command=find_directory)
select_folder.grid(column=1, row=2, columnspan=1, sticky="nsew")

select_watermark = ttk.Button(frame, text="Select Watermark", command=choose_watermark)
select_watermark.grid(column=2, row=2, columnspan=1, sticky="nsew")

watermark_all = ttk.Button(frame, text="Watermark All", command=convert_folder)
watermark_all.grid(column=1, row=3, columnspan=2, sticky="nsew")

quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
quit_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

root.mainloop()
