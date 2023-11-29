import streamlit as st
import cv2
import os
from PIL import Image
import numpy as np

def crop_image_opencv(image, crop_height):
    # Convert PIL image to OpenCV format
    open_cv_image = np.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

    # Get image dimensions
    height, width = open_cv_image.shape[:2]

    # Set coordinates to crop image
    top = crop_height
    bottom = height

    # Crop image
    cropped_image = open_cv_image[top:bottom, 0:width]

    return cropped_image

def save_image(image, folder_path, filename):
    output_filename = f"cropped_{filename}"
    output_path = os.path.join(folder_path, output_filename)

    # Convert OpenCV image to PIL format
    image_pil = Image.fromarray(image[:, :, ::-1])  # Convert BGR to RGB
    image_pil.save(output_path)
    return output_path

# Streamlit app layout
st.title("Image Cropping Tool")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
crop_height = st.number_input("Enter the crop height", min_value=0, value=25)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    if st.button('Crop Image'):
        cropped_image = crop_image_opencv(image, crop_height)
        st.image(cropped_image, channels="BGR", use_column_width=True)
        save_image(cropped_image, os.getcwd(), uploaded_file.name)
        st.success("Image cropped and saved successfully!")
