from PIL import ImageTk, Image
import pillow_avif

def pil_image_resizer(pil_image, max_width=500):
    if max_width is None:
        max_width = 500
    # Get current dimensions
    width, height = pil_image.size

    # If the image is wider than max_width, resize it proportionally
    if width > max_width:
        # Calculate the scaling ratio
        ratio = max_width / width
        new_height = int(height * ratio)
        # Resize using a high-quality filter (LANCZOS is recommended for downsampling)
        pil_image = pil_image.resize((max_width, new_height), Image.LANCZOS)
    return pil_image

def open_image(img_path, max_width=None):
    return pil_image_resizer(Image.open(img_path), max_width)

def HelperImageTk(img_path, max_width=None):
    return ImageTk.PhotoImage(open_image(img_path, max_width))
