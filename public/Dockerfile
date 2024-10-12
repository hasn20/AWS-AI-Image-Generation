# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the public directory into the container at /app
COPY . /app

# Install any Python packages that are listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches and use frontend.py
CMD ["streamlit", "run", "frontend.py"]