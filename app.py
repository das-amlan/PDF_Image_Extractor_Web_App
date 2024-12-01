import streamlit as st
from utils import extract_images_from_pdf
from io import BytesIO

def main():
    st.title("PDF Image Extractor")

    # File uploader for PDFs
    pdf_file = st.file_uploader("Upload a PDF file to extract images", type="pdf")
    if pdf_file is not None:
        # Save uploaded PDF temporarily in memory
        pdf_path = pdf_file.name
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())

        # Extract images
        extracted_images = extract_images_from_pdf(pdf_path)

        if extracted_images:
            st.subheader("Extracted Images")
            for i, img in enumerate(extracted_images):
                # Display extracted images
                st.image(img, caption=f"Image {i+1}", use_container_width=True)

                # Download link for each image
                img_buffer = BytesIO()
                img.save(img_buffer, format="PNG")
                img_buffer.seek(0)

                st.download_button(
                    label=f"Download Image {i+1}",
                    data=img_buffer,
                    file_name=f"image_{i+1}.png",
                    mime="image/png"
                )
        else:
            st.warning("No images found in the PDF.")

if __name__ == "__main__":
    main()