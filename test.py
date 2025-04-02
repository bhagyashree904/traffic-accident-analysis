import streamlit as st
import folium
from folium.plugins import HeatMap
import pandas as pd

# Load data
accident_data = pd.read_csv("C:/Users/bhagy/Downloads/Road Accident Data.csv")

# Streamlit layout
st.title("Traffic Accident Risk Analysis")

# Create Map
map_center = [37.7749, -122.4194]
m = folium.Map(location=map_center, zoom_start=12)
heat_data = [[row['Latitude'], row['Longitude']] for index, row in accident_data.iterrows()]
HeatMap(heat_data).add_to(m)

# Display map
st.write("### High-Risk Areas Heatmap")
st.components.v1.html(m._repr_html_(), height=600)

# Show real-time data
st.write("### Real-Time Accident Data")
st.dataframe(accident_data.head())
