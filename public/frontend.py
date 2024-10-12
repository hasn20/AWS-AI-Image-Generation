import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main background styling */
    .main {
        background-color: #1a1a1a;
        color: #f0f0f0;
    }

    /* Centering title and making it pop */
    h1 {
        color: #0ff;
        font-size: 3em;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 20px #0ff, 0 0 30px #0ff;
        margin-bottom: 30px;
    }

    /* Text input customization */
    .stTextInput > div > div > input {
        background-color: #333;
        color: #0ff;
        border: 2px solid #0ff;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        font-family: 'Roboto', sans-serif;
    }

    /* Generate button with neon hover effect */
    .stButton > button {
        background-color: #0ff;
        color: #333;
        border: 2px solid #0ff;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        font-family: 'Orbitron', sans-serif;
        transition: 0.3s ease;
        text-shadow: 0 0 10px #0ff;
    }
    .stButton > button:hover {
        background-color: #333;
        color: #0ff;
        border: 2px solid #0ff;
        box-shadow: 0 0 20px #0ff, 0 0 30px #0ff;
        cursor: pointer;
    }

    /* Footer styling */
    footer {
        text-align: center;
        color: #0ff;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
    }

    /* Customize container margins */
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }

    /* Add animations for interactive elements */
    @keyframes glow {
        0% {
            box-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #00f;
        }
        50% {
            box-shadow: 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #00f, 0 0 80px #00f;
        }
        100% {
            box-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #00f;
        }
    }

    /* Image container for generated images */
    .stImage {
        animation: glow 1.5s infinite ease-in-out;
        margin-top: 30px;
    }
    </style>

    <!-- Linking external fonts for futuristic design -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&family=Roboto&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# Main app
def main():
    st.title("AI Image Generator")

    st.write("Enter your prompt and see it transform into a stunning AI-generated image!")

    # Text input for prompt
    prompt = st.text_input("Enter your image description:", "")

    # Generate button
    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                try:
                    # API call (replace with your actual API endpoint)
                    api_url = "https://toahtdud0g.execute-api.us-east-1.amazonaws.com/prod/generate-image"
                    response = requests.post(api_url, json={"prompt": prompt}, timeout=30)

                    if response.status_code == 200:
                        response_data = response.json()
                        image_url = response_data.get("image_url")

                        if image_url:
                            image_response = requests.get(image_url)
                            image = Image.open(BytesIO(image_response.content))
                            st.image(image, caption="Generated Image", use_column_width=True)
                        else:
                            st.error("No image URL in the response. Please try again.")
                    else:
                        st.error(f"API request failed. Status code: {response.status_code}")

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a description before generating an image.")

    # Footer
    st.markdown("---")
    st.markdown("<footer>Created by AI Image Generator | Transform your ideas into stunning visuals</footer>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
