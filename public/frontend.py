import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Custom CSS for styling
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #333;
        padding: 10px;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(45deg, #00ff99, #00ccff);
        border: none;
        border-radius: 50px;
        color: white;
        padding: 10px 20px;
        font-size: 20px;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #00ccff, #00ff99);
        box-shadow: 0 0 20px rgba(0, 255, 255, 1);
    }
    .stImage>img {
        border-radius: 10px;
        border: 2px solid #333;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.title("Ethereal Visions AI Image Generation")

# Sleek Text Input
prompt = st.text_input("Enter your vision:", "")

# Neon Glow Button
if st.button("Generate Vision"):
    if prompt:
        # Make a request to your backend API (replace URL with your API Gateway endpoint)
        api_url = "https://cixege29k6.execute-api.eu-north-1.amazonaws.com/production/generate-image"
        response = requests.post(api_url, json={"prompt": prompt})

        if response.status_code == 200:
            # Get the image URL from the response
            image_url = response.json().get("image_url")
            
            if image_url:
                # Fetch and display the image
                image_response = requests.get(image_url)
                image = Image.open(BytesIO(image_response.content))
                st.image(image, caption="Generated Vision", use_column_width=True)
            else:
                st.error("Image generation failed. Please try again.")
        else:
            st.error("Failed to communicate with the API. Please try again later.")
    else:
        st.warning("Please enter a prompt before clicking 'Generate Vision'.")
