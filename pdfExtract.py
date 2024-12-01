# Import necessary modules
from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import io
from PIL import Image
import fitz

# Create a Flask app instance
app = Flask(__name__)

# Set the upload and image folders
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['IMAGE_FOLDER'] = 'images'

# Define a function to extract images from a PDF page
def extract_images_from_page(pdf_path, page_num):
    doc = fitz.open(pdf_path)  # Open the PDF file using fitz
    page = doc.load_page(page_num) # Load the page and get all images on the page
    images = page.get_images(full=True)
    extracted_images = []

    # Loop through each image and extract it
    for img in images:
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        # Save the image bytes to a PIL.Image object
        img = Image.open(io.BytesIO(image_bytes))
        extracted_images.append(img)

    return extracted_images

# Define a Flask route for uploading a PDF file
@app.route('/', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST': # Get the uploaded PDF file and save it to the upload folder
        pdf = request.files['pdf']
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename)
        pdf.save(pdf_path)

         # Extract images from each page of the PDF and save them to the image folder
        with fitz.open(pdf_path) as doc:
            for page_num in range(doc.page_count):
                images = extract_images_from_page(pdf_path, page_num)
                for img in images:
                    img_path = os.path.join(app.config['IMAGE_FOLDER'], f"{uuid.uuid4()}.png")
                    img.save(img_path)

        # Render the display_images.html template and pass the list of image filenames
        return render_template('display_images.html', images=os.listdir(app.config['IMAGE_FOLDER']))
    
    # Render the upload_pdf.html template if the request method is GET
    return render_template('upload_pdf.html')

# Define a Flask route for serving images
@app.route('/images/<path:path>')
def serve_image(path):
    return send_from_directory(app.config['IMAGE_FOLDER'], path)

#  Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)