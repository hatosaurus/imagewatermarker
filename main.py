from PIL import Image

input_image_path = "raw_images/Sea_Dragon_.jpg"
watermark_image_path = "watermark/jessicaschmidt_watermark.png"
output_image_path = "watermarked_images/BIRD_GREEN_WATERMARKED.jpg"

base_image = Image.open(input_image_path) #open base image
watermark = Image.open(watermark_image_path) #open water mark
watermark = watermark.resize(base_image.size)

width, height = base_image.size

width_of_watermark, height_of_watermark = watermark.size
position = (int(width/2-width_of_watermark/2), int(height/2-height_of_watermark/2))

transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
transparent.paste(base_image, (0, 0))
transparent.paste(watermark, position, mask=watermark)
transparent.convert('RGB').save(output_image_path)