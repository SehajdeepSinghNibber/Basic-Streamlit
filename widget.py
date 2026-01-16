import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)

option = ["Python","Javacript","C++","Java"]

choice = st.selectbox("Choose your favourite programming language:",option)

st.write(f"You selected {choice}")
st.write(f"Your age is {age}")

if name:
    st.write(f"Hello {name}")
    
data = {
    "Name":["John","Jane","Jack","Jill"],
    "Age":[28,23,32,29],
    "City":["New York","Boston","Los Angles","Houstan"]
}

df=pd.DataFrame(data)
df.to_csv("Sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df.pd.read_csv(uploaded_file)
    st.write(df)