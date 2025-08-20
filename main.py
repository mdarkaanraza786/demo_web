import streamlit as st

st.title('Welcome to Arkaan,s first website')
name=st.text_input("Enter your name:")
fname=st.text_input("Enter your father name:")
address=st.text_area("Enter the home address")
classdata=st.selectbox("Select the calss:",(1,2,3,4,5,6,7,8,9,10))

button=st.button("Save")

if button:
    st.markdown(f"""
                Name: {name}
                Father Name: {fname}
                Address: {address}
                Class: {classdata}""")