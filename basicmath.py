import streamlit as st

def product():
    num1=st.number_input("Please enter first number")
    num2=st.number_input("Please enter second number")
    st.write("Product:::", num1 * num2)

def sum():
    num1=st.number_input("Please enter first number")
    num2=st.number_input("Please enter second number")
    st.write("Sum:::", (num1 + num2)) 

def subtract():
    num1=st.number_input("Please enter big number")
    num2=st.number_input("Please enter small number")
    st.write("Subtraction:::", (num1 - num2)) 