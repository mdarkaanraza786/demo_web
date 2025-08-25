import streamlit as st
from PIL import Image


def app():
    st.title("Welcome to my Home Page")
    # Load the image
    img = Image.open("Arkaan.jpg")  # Replace with your image file path

    # Display the image
    st.image(img)  
