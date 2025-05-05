import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Konfigurasi model
CLASS_MAP = {
    0: {'name': 'paper', 'emoji': '📄', 'color': '#00D154'},
    1: {'name': 'rock', 'emoji': '🪨', 'color': '#00D154'},
    2: {'name': 'scissors', 'emoji': '✂️', 'color': '#00D154'}
}

def initialize_model():
    @st.cache_resource
    def load_saved_model():
        model = tf.keras.models.load_model('best_model.h5')
        return model
    return load_saved_model()

def process_image(uploaded_file):
    try:
        img = Image.open(uploaded_file).convert('RGB')
        img = img.resize((150, 150))
        img_array = np.array(img) / 255.0
        return np.expand_dims(img_array, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return None

def display_prediction_result(prediction):
    class_idx = np.argmax(prediction)
    confidence = np.max(prediction)
    class_info = CLASS_MAP[class_idx]
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; border-radius: 15px; 
                background: {class_info['color']}10; border: 2px solid {class_info['color']};
                margin: 1rem 0;">
        <div style="font-size: 5rem; color: {class_info['color']};">
            {class_info['emoji']}
        </div>
        <h3 style="color: {class_info['color']}; margin: 0.5rem 0;">
            {class_info['name'].capitalize()}
        </h3>
        <div style="font-size: 1.2rem; color: #666;">
            Confidence: {confidence:.2%}
        </div>
    </div>
    """, unsafe_allow_html=True)

def prediction_interface():
    st.markdown("## 🎮 Rock Paper Scissor Shot!")
    st.markdown("Upload a photo of your hand gesture and the AI will tell you which gesture you're showing")
    
    uploaded_file = st.file_uploader(
        "Choose a hand image",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if uploaded_file is not None:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(uploaded_file, use_container_width=True)
        
        with col2:
            if st.button('🤖 Analyze Gesture', use_container_width=True):
                with st.spinner('AI is analyzing your gesture...'):
                    try:
                        model = initialize_model()
                        img_array = process_image(uploaded_file)
                        
                        if img_array is not None:
                            prediction = model.predict(img_array)
                            display_prediction_result(prediction)
                            
                    except Exception as e:
                        st.error(f"Prediction failed: {str(e)}")

def run():
    prediction_interface()

if __name__ == '__main__':
    run()
