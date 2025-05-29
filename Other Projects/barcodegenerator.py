import os
import barcode
from barcode.writer import ImageWriter

def generate_instagram_barcode():
    # Instagram handle and URL
    username = "ireachentertainment"
    url = f"https://instagram.com/{username}"

    # Define path to Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_filename = os.path.join(downloads_folder, "ireach_barcode")

    # Generate and save barcode
    code128 = barcode.get('code128', url, writer=ImageWriter())
    saved_path = code128.save(output_filename)

    print(f"✅ Barcode saved at: {saved_path}.png")