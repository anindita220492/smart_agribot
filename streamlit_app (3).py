

#!pip install streamlit --quiet

import streamlit as st
import json
from google.oauth2 import service_account
import vertexai
from vertexai.language_models import ChatModel

from utils.gemini_app import ask_gemini
from utils.disease_classifier import detect_disease
from utils.weather_api import get_weather

PROJECT_ID = st.secrets["PROJECT_ID"]
WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]
GCP_SERVICE_ACCOUNT = st.secrets["GCP_SERVICE_ACCOUNT"]

credentials = service_account.Credentials.from_service_account_info(GCP_SERVICE_ACCOUNT)
vertexai.init(project=PROJECT_ID, location="us-central1", credentials=credentials)

st.set_page_config(page_title="Smart AgriBot", layout="wide")
st.title("🌾 Smart AgriBot: AI Assistant for Small Farmers")

tab1, tab2, tab3 = st.tabs(["💬 Ask AgriBot", "🧪 Diagnose Disease", "🌦️ Weather Info"])

with tab1:
    query = st.text_input("Ask your agricultural question (in any language):")
    if st.button("Get Answer") and query:
        response = ask_gemini(query, project_id=PROJECT_ID)
        st.success(response)

with tab2:
    st.write("Upload an image of a diseased plant leaf:")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        result = detect_disease(uploaded_image)
        st.info(f"Disease Diagnosis: {result}")
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

with tab3:
    city = st.text_input("Enter your city/village:")
    if st.button("Check Weather") and city:
        weather, temp = get_weather(city, api_key=WEATHER_API_KEY)
        st.write(f"🌤️ Weather: {weather}")
        st.write(f"🌡️ Temperature: {temp}°C")
