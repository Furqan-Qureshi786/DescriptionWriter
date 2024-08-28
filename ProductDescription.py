import google.generativeai as genai
import os
import streamlit as st

# Function to generate product description
def generate_product_description(product_details):
    # Initialize the Gemini model instance
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    # Generate content using the product details
    response = model.generate_content([product_details])
    
    return response.text

# Streamlit interface
st.title("Product Description Writer")
st.write("Enter product details below to generate a compelling product description:")

# Text input for product details
product_details = st.text_area("Product Details", placeholder="Enter product features, specifications, etc.")

if st.button("Generate Description"):
    if product_details.strip() != "":
        # Generate and display the product description
        description = generate_product_description(product_details)
        st.write("### Generated Product Description:")
        st.write(description)
    else:
        st.write("Please enter product details to generate a description.")

# Custom CSS for the tile and background
st.markdown("""
    <style>
        body {
            background-color: black;
        }
        .tile {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
            padding: 20px;
            width: 80%;
            margin: auto;
        }
        .streamlit-button {
            border-radius: 10px;
        }
        .tile-content {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

# Add content inside the tile
st.markdown('<div class="tile">', unsafe_allow_html=True)
st.write('<div class="tile-content">', unsafe_allow_html=True)

# Streamlit content goes here (input and output)
st.title("Product Description Writer")
st.write("Enter product details below to generate a compelling product description:")

product_details = st.text_area("Product Details", placeholder="Enter product features, specifications, etc.")

if st.button("Generate Description"):
    if product_details.strip() != "":
        description = generate_product_description(product_details)
        st.write("### Generated Product Description:")
        st.write(description)
    else:
        st.write("Please enter product details to generate a description.")

st.write('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
