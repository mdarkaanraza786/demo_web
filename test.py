import streamlit as st
import pandas as pd

def app():
    name=st.text_input("Enter your name:")
    fname=st.text_input("Enter your father name:")
    address=st.text_area("Enter the home address")
    classdata=st.selectbox("Select the class:",(1,2,3,4,5,6,7,8,9,10))

    button=st.button("Save")

    if button:
        data = {
        "Name": [{name}],
        "Father Name": [{fname}],
        "Address": [{address}],
        "Class": [{classdata}]
        }
    
    
        # Convert dictionary to DataFrame
        df = pd.DataFrame(data)
        st.write("My details--------------")
        st.dataframe(df)  # Scrollable & sortable table   
        # Create some sample data
