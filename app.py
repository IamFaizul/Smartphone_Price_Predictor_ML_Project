import streamlit as st
import pickle
import numpy as np
import re

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
st.title("Smartphone Price Predictor")

# Brand
brand = st.selectbox('Brand',df['Brand'].unique())

# Processor
processor = st.selectbox('Processor',df['Processor'].unique())

# RAM
ram = st.selectbox('RAM',df['RAM(GB)'].unique())

# ROM
rom = st.selectbox('ROM',df['ROM(GB)'].unique())

# Battery
battery = st.selectbox('Battery',df['Battery(mAh)'].unique())

# Primary_Rear_Camera(MP)
primary_rear_camera = st.selectbox('Primary_Rear_Camera',df['Primary_Rear_Camera(MP)'].unique())

# Secondary_Rear_Camera1(MP)
secondary_rear_camera1 = st.selectbox('Secondary_Rear_Camera1',df['Secondary_Rear_Camera1(MP)'].unique())

# Secondary_Rear_Camera2(MP)
secondary_rear_camera2 = st.selectbox('Secondary_Rear_Camera2',df['Secondary_Rear_Camera2(MP)'].unique())

# Front_Camera
front_camera = st.selectbox('Front_camera',df['Front_Camera(MP)'].unique())

# Display
display = st.selectbox('Display',df['Display(inches)'].unique())

# OS
os = st.selectbox('OS',df['OS'].unique())

# screen size
screen_size = st.number_input('Screen Size')

import re


# resolution
resolution = st.selectbox('Screen Resolution', ['480×800', '640×1136', '720×1280', '750×1334', '1080×1920', '1440×2560'])

if st.button("Predict Price"):
    # Remove non-numeric characters from resolution
    resolution_numeric = re.sub(r'[^\d×]', '', resolution)

    # Query
    X_res = int(resolution_numeric.split('×')[0])
    Y_res = int(resolution_numeric.split('×')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    query = np.array([brand, processor, ram, rom, battery, primary_rear_camera, secondary_rear_camera1, secondary_rear_camera2, front_camera, display, ppi, os])
    query = query.reshape(1, 12)  # Reshape the query array

    predicted_price = pipe.predict(query)[0]  # Make the prediction

    st.title("The predicted price of this configuration is " + str(int(np.exp(predicted_price)))+" Rupees")