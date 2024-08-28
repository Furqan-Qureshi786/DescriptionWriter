import google.generativeai as genai
import os
import streamlit as st

# Function to generate product description
def generate_product_description(product_details):
    # Create a generative model instance
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Generate content using the product details
    response = model.generate_content([product_details])
    return response.text

# Create a container for the tile
with st.container():
    # Add a background color to the container (optional)
    st.markdown(
        """
        <style>
        .tile {
            background-color: #2c2c2c;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="tile">', unsafe_allow_html=True)

    # Title and description inside the tile
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

    st.markdown('</div>', unsafe_allow_html=True)
