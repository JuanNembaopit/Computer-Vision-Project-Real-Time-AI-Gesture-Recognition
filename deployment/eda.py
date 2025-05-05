import streamlit as st
from PIL import Image

# List of uploaded image filenames
uploaded_images = [
    "41HC0VBlHSRhi0AG.png",
    "4ZVOE4DxJDxaysrR.png",
    "6AcmgOHcOvQfp1iW.png",
    "7fRLxoheLluOwCkp.png",
    "9zfyVkUcku0qc4Gu.png",
    "BtUfOjTzw9EEvNHO.png",
    "asi6ZQCskd51eHm1.png",
    "cDveaur4dR2ZCCo8.png",
    "iDKbsfPFabN9bUKT.png"
]

def display_uploaded_images():
    st.header("📸 Sample Images from the Dataset")
    st.markdown(
        "Here are some sample images illustrating the diversity of hand gestures and backgrounds in the Rock-Paper-Scissors dataset."
    )
    # Display images in a 3x3 grid
    rows = 3
    cols = 3
    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            idx = row * cols + col
            if idx < len(uploaded_images):
                img = Image.open(uploaded_images[idx])
                with columns[col]:
                    st.image(
                        img,
                        caption=uploaded_images[idx],
                        use_container_width=True
                    )

def run():
    st.title("📊 Exploratory Data Analysis (EDA)")
    st.markdown("---")

    # Project description
    st.header("📝 About the Project")
    st.markdown("""
**Rock-Paper-Scissors Classifier** is a deep learning model designed to recognize hand gestures for the classic game *Rock-Paper-Scissors*. The model leverages a **Convolutional Neural Network (CNN)** to classify images into three categories: **rock**, **paper**, and **scissors**.
**Project Objectives:**
- Enable the development of interactive, AI-powered applications.
- Enhance the gaming experience through real-time gesture recognition.
**Problem Statement:**
- Automate the recognition of hand gestures in Rock-Paper-Scissors.
**Target Users:**
- AI game application developers.
- Researchers exploring CNN applications in image classification.
- Educators demonstrating real-world AI projects.
**Model Highlights:**
- Achieves high accuracy (99%+) on validation and test datasets.
- Robust to variations in hand color, lighting, and backgrounds.
    """)

    # Dataset description
    st.header("📂 Dataset")
    st.markdown("""
The dataset is sourced from [Kaggle: Rock-Paper-Scissors](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors).
**Dataset Details:**
- Total images: 2,188  
    - Rock: 726 images  
    - Paper: 710 images  
    - Scissors: 752 images  
- Image format: RGB, 300x300 pixels
The dataset is split into:
- **Training**: 70%
- **Validation**: 15%
- **Test**: 15%
Images feature diverse hand gestures against green backgrounds.
    """)

    # Display uploaded images
    display_uploaded_images()

if __name__ == '__main__':
    run()
