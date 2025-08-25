import streamlit as st
import test ,home,about
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Option Menu Example", layout="wide")

# Horizontal menu
selected = option_menu(
    None, ["Home", "About", "TestMe"],  # Menu items
    icons=["house", "info-circle", "gear-fill"],    # Icons
    menu_icon="cast", 
    default_index=0,
    orientation="horizontal"             
    # 👈 Horizontal Menu
)

# Page content
if selected == "Home":   
    home.app()
        
elif selected == "About":    
    about.app()
    
elif selected == "TestMe":    
    test.app()
    test.printALL()
    


    
  