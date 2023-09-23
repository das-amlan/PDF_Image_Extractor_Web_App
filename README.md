# PDF Image Extractor Web App
This is a simple web app built with Flask that allows users to upload a PDF file, extract images from the PDF, and display the images in the web app.

## Getting Started
To run the web app, you need to have Python 3 and Flask installed on your system. You can install Flask using pip:
```
pip install Flask
```

After installing Flask, clone this repository to your local machine:
```
git clone https://github.com/your_username/pdf-image-extractor.git
```

## Running the Web App
To run the web app, navigate to the project directory and run the pdfExtract.py script:
```
cd pdf-image-extractor
python pdfExtract.py
```

This will start the Flask development server on `http://localhost:5000/`. You can access the web app by opening this URL in your web browser.

## Uploading a PDF File
To extract images from a PDF file, click the "Upload PDF" button on the home page. This will take you to the `upload_pdf.html` page, where you can select a PDF file to upload.

## Extracting Images from the PDF
After uploading a PDF file, the web app will extract images from each page of the PDF using the `PyMuPDF` library. The `extract_images_from_page` function in `pdfExtract.py` is responsible for extracting images from the PDF.

## Displaying Extracted Images
Once the images are extracted, they are saved to the images folder with unique filenames using `uuid.uuid4()`. The `display_images.html` template in the templates folder displays the extracted images using the url_for function.

## Conclusion
That's it! You now have a simple web app that can extract images from a PDF file and display them in the browser. You can further customize and improve the app according to your requirements.

I hope this helps!
