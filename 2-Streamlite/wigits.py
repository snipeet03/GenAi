import streamlit as st 
import pandas as pd 

st.title('Streamlit Text Input ')

## Input Box 
name = st.text_input('Enter your name : ')
if name:
    st.write(f'Hello {name}')


## Slider 
age= st.slider("Select yor age : " , 0, 100, 25)
if age:
    st.write(f'Your age is {age}')


## Select Box 
options = ["Python ", "Java" , "JavaScripts"] 
choice = st.selectbox("Choose your fav language ", options)
if choice:
    st.write(f"Yout selected {choice}")


## Dataframe 
data = {
    "Name " : [ "navneet", "rohan" , 'jeff'], 
    "lastName" : ['Lonare', 'lande', 'Bezoz']
}
df=pd.DataFrame(data)
st.write(df)
df.to_csv('sampledata.csv')

## upload a file 
uploaded_file=st.file_uploader("Choose a file ", type='csv')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)