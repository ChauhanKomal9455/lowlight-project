import streamlit as st
import numpy as np
from PIL import Image
import cv2

from enhance import enhance_image, adjust_gamma

st.set_page_config(page_title="Low-Light Enhancer", layout="wide")

st.title("Low-Light Image Enhancement App")

st.write("Upload a dark image and enhance it instantly.")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img, use_column_width=True)

    # Controls
    st.sidebar.header("Adjust Settings")
    gamma = st.sidebar.slider("Brightness (Gamma)", 0.5, 3.0, 1.5)

    # Process image
    enhanced = adjust_gamma(img, gamma)
    enhanced = enhance_image(enhanced)

    with col2:
        st.subheader("Enhanced Image")
        st.image(enhanced, use_column_width=True)

    # Download option
    result = Image.fromarray(enhanced)
    result.save("enhanced.png")

    with open("enhanced.png", "rb") as file:
        st.download_button(
            label="Download Enhanced Image",
            data=file,
            file_name="enhanced.png",
            mime="image/png"
        )