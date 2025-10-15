import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache the data loading function to speed up app reloads
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load data
df, target_name = load_data()

# Train the model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar for user input
st.sidebar.title('Input Features')

sepal_length = st.sidebar.slider(
    'Sepal Length (cm)',
    float(df.iloc[:, 0].min()),
    float(df.iloc[:, 0].max()),
    float(df.iloc[:, 0].mean())
)

sepal_width = st.sidebar.slider(
    'Sepal Width (cm)',
    float(df.iloc[:, 1].min()),
    float(df.iloc[:, 1].max()),
    float(df.iloc[:, 1].mean())
)

petal_length = st.sidebar.slider(
    'Petal Length (cm)',
    float(df.iloc[:, 2].min()),
    float(df.iloc[:, 2].max()),
    float(df.iloc[:, 2].mean())
)

petal_width = st.sidebar.slider(
    'Petal Width (cm)',
    float(df.iloc[:, 3].min()),
    float(df.iloc[:, 3].max()),
    float(df.iloc[:, 3].mean())
)

# Input data for prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Make prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

# Display result
st.subheader("Prediction Result")
st.write(f"The predicted species is: **{predicted_species}** 🌸")

# Optionally, show the input values
st.write("### Input Features:")
st.write(pd.DataFrame(input_data, columns=df.columns[:-1]))
