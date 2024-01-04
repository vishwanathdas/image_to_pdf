import os
from PIL import Image

def image_to_pdf(image_path):
    # Get the last part of the path, i.e., picture.png
    file_name = os.path.split(image_path)[-1]

    # Replace the image format extension with pdf
    new_file = os.path.join(
        os.path.splitext(image_path)[0] + ".pdf"
    )  # Corrected the logic to change the extension

    # Pillow instance of the desired picture
    image_file = Image.open(image_path)
    parsed_image = image_file.convert("RGB")
    parsed_image.save(new_file)
    return new_file  # Return the new file path

if __name__ == "__main__":
    image_path = input("Enter image file path: ")
    converted_file = image_to_pdf(image_path)
    print(f"Image converted to PDF. Saved as: {converted_file}")
