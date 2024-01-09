from PIL import Image as PILImage

watermark_image_path = "watermark/jessicaschmidt_watermark.png"


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



