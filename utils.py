import fitz  # PyMuPDF
from PIL import Image
import io
import os

def extract_images_from_pdf(pdf_path):
    """
    Extract images from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: List of PIL.Image objects representing extracted images.
    """
    extracted_images = []

    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            images = page.get_images(full=True)

            # Extract and process each image
            for img in images:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]

                # Convert bytes to a PIL Image
                img = Image.open(io.BytesIO(image_bytes))
                extracted_images.append(img)

    return extracted_images

def clear_temp_files(directory):
    """
    Clear all files in a directory.

    Args:
        directory (str): Path to the directory.
    """
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        os.remove(file_path)
    os.rmdir(directory)
