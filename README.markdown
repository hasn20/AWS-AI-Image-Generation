# AI Image Generator

A sleek, futuristic web application built with Streamlit that transforms text prompts into stunning AI-generated images. This project integrates a custom-styled interface with a neon aesthetic, powered by an external API for image generation.

## Features
- **Text-to-Image Generation**: Enter a descriptive prompt to generate high-quality images via an external API.
- **Futuristic UI**: Custom CSS with neon glow effects and modern typography using Orbitron and Roboto fonts.
- **Docker Support**: Easily deploy the application using a lightweight Docker container.
- **Responsive Design**: Optimized for a seamless user experience with interactive elements.

## Prerequisites
- **Docker** (optional, for containerized deployment)
- **Python 3.9+** (for local development)
- **Git** (to clone the repository)

## Installation

### Option 1: Run with Docker
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t ai-image-generator .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -p 8501:8501 ai-image-generator
   ```

4. Access the application at `http://localhost:8501` in your web browser.

### Option 2: Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run frontend.py
   ```

5. Access the application at `http://localhost:8501` in your web browser.

## Project Structure
```
ai-image-generator/
├── Dockerfile           # Docker configuration for containerized deployment
├── frontend.py          # Main Streamlit application script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Dependencies
The project relies on the following Python packages (listed in `requirements.txt`):
- `streamlit`: Web framework for the application
- `Pillow`: Image processing library
- `requests`: For making API calls

## Usage
1. Open the application in your browser (`http://localhost:8501`).
2. Enter a descriptive prompt in the text input field (e.g., "A futuristic city at night with neon lights").
3. Click the **Generate Image** button.
4. Wait for the API to process the request and display the generated image.
5. If an error occurs, check the prompt or API connectivity.

## API Integration
The application sends prompts to an external API endpoint for image generation:
- **Endpoint**: `https://toahtdud0g.execute-api.us-east-1.amazonaws.com/prod/generate-image`
- Replace this URL with your own API endpoint if needed.

## Customization
- **Styling**: Modify the CSS in `frontend.py` to adjust the neon glow effects, fonts, or layout.
- **API**: Update the `api_url` in `frontend.py` to integrate with a different image generation service.
- **Port**: Change the exposed port in the `Dockerfile` or container run command if needed.

## Troubleshooting
- **API Errors**: Ensure the API endpoint is accessible and supports the expected JSON format (`{"prompt": "your-description"}`).
- **Docker Issues**: Verify Docker is running and the port `8501` is not in use.
- **Dependency Issues**: Ensure all packages in `requirements.txt` are installed correctly.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
