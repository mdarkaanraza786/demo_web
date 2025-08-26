import streamlit as st
import pandas as pd



def app():
    name=st.text_input("Enter your name:")
    fname=st.text_input("Enter your father name:")
    address=st.text_area("Enter the home address")
    classdata=st.selectbox("Select the class:",(1,2,3,4,5,6,7,8,9,10))

    button=st.button("Data Save Successfully!!...")
    if button:
     st.balloons()

    if button:
        data = {
        "Name": [{name}],
        "FatherName": [{fname}],
        "Address": [{address}],
        "Class": [{classdata}]
        }       
        
        df = pd.DataFrame(data)
        st.dataframe(df)
        
        

   