import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


db=firestore.client()
doc_ref=db.collection('registrationCollection').document()


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
        "Name": {name},
        "FatherName": {fname},
        "Address": {address},
        "Class": {classdata}
        }       
        
        doc_ref.set(data)
        printALL()
        
        
def printALL():
   docs = db.collection("registrationCollection").stream()
   data = [doc.to_dict() for doc in docs]
   df = pd.DataFrame(data)
   st.dataframe(df)
   