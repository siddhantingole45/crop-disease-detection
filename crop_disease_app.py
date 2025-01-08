import streamlit as st
import random

# Function to simulate disease and cure
def get_random_disease_and_cure():
    diseases = [
        ("Blight", "Use fungicides and remove infected plants."),
        ("Powdery Mildew", "Apply sulfur-based fungicides."),
        ("Rust", "Use resistant crop varieties and fungicides."),
        ("Leaf Spot", "Avoid overhead watering and use copper fungicides."),
        ("Wilt", "Improve soil drainage and use resistant crop varieties."),
    ]
    return random.choice(diseases)

# Apply custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Streamlit app
st.title("Crop Disease Detector")
st.write("Upload an image of your crop with a disease, and we'll identify the disease and suggest a cure!")

# File uploader
uploaded_file = st.file_uploader("📂 Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("🔍 Processing the image...")

    # Simulate processing
    disease, cure = get_random_disease_and_cure()

    # Display result
    st.subheader("🚨 Disease Detected")
    st.write(f"**Disease:** {disease}")
    st.write(f"**Cure/Treatment:** {cure}")
else:
    st.write("Please upload an image to get started.")
