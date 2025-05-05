import streamlit as st
import prediction
import eda

# Page Configuration
st.set_page_config(
    page_title='Rock-Paper-Scissors AI',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS Styling
st.markdown("""
    <style>
    :root {
        --primary-color: #FF6B6B;
        --secondary-color: #4ECDC4;
    }
    
    .main-title {
        font-family: 'Arial Rounded MT Bold', sans-serif;
        color: var(--primary-color);
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .nav-button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.5rem 2rem !important;
        transition: transform 0.3s ease !important;
    }
    
    .nav-button:hover {
        transform: scale(1.05);
    }
    
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: #f0f2f6;
        padding: 1rem;
        text-align: center;
        border-top: 2px solid var(--primary-color);
    }
    </style>
""", unsafe_allow_html=True)

# Main App Layout
def main():
    st.markdown('<h1 class="main-title">🎮 Rock-Paper-Scissors AI Challenge</h1>', unsafe_allow_html=True)
    
    # Navigation Tabs
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        menu_choice = st.radio(
            "Select Mode:",
            ["📊 EDA", "🎮 Play with AI"],
            horizontal=True,
            label_visibility="hidden"
        )
    
    st.markdown("---")
    
    # Page Routing
    if menu_choice == "📊 EDA":
        eda.run()
    else:
        prediction.run()
    
    # Custom Footer
    st.markdown("""
    <div class="footer">
        <p style="margin:0; font-size:0.9rem;">
            👨💻 Created by <strong>Juan Nembaopit</strong> 
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
