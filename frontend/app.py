# streamlit_app.py
# streamlit_app.py
import streamlit as st
import requests
import os
import altair as alt
import pandas as pd
import json

# Base URL for FastAPI backend
API_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Page config
st.set_page_config(
    page_title="Smart City Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling (colors, fonts, effects)
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], [class^="css-"], * {
        background-color: #fff !important;
        color: #000 !important;
        font-family: 'Microsoft YaHei UI', Tahoma, Geneva, Verdana, Crewniverse !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #ffe !important;
    }
    .main-title {
        font-size: 3em;
        text-align: center;
        color: #fff !important;
        padding: 20px;
        background: linear-gradient(to right, #833ab4, #fd1d1d, #fcb045);
        border-radius: 20px;
        margin: 1rem auto;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease-in-out;
    }
    .scroll-container {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        gap: 1.5rem;
        padding: 2rem;
    }
    .feature-card {
        min-width: 80%;
        scroll-snap-align: start;
        background: linear-gradient(to bottom right, #6faddb, #ff6eff);
        border: 2px solid #eaeaea;
        border-radius: 30px;
        padding: 2rem;
        color: #000 !important;
        animation: floatUp 0.8s ease;
        transition: transform 0.4s ease-in-out, box-shadow 0.4s ease-in-out;
    }
    .feature-card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    .stButton>button {
        background: linear-gradient(135deg, #fcb045, #fcb045);
        color: #fcb045 !important;
        padding: 8px 16px;
        font-size: 0.9rem;
        border-radius: 12px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffffff);
    }
    input, textarea, .stTextInput input, .stTextArea textarea, .stSelectbox div, .stMultiSelect div {
        color: #000 !important;
        background-color: #fff !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# The rest of your Streamlit app remains unchanged...
# You can keep your existing layout, logic, and API calls.

# Title
st.markdown('<div class="main-title">ｗ𝐄ɕ𝕆𝐌𝐄 т𝕆 тＨ𝐄 ѕ𝐌ⓐⓡт ɕเтＹ ⓐѕѕเѕтⓐ几т</div>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📂 Navigate")
page = st.sidebar.selectbox("Select Feature", ["Home","Updates", "Chat", "Text Correction", "Eco Tip", "Forecast", "Policy", "Weather","Feedback"])

# Main content header
st.title("service")

# Feature container scroll area
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

# Features (Unchanged logic)
# ... (rest of the logic stays same)

# Close scroll container
st.markdown('</div>', unsafe_allow_html=True)


# Define each feature
if page == "Home":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)

    # Ensure the full URL is a valid direct image link
    image_url = (
        "https://images.unsplash.com/photo-1507090960745-b32f65d3113a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )

    # Display the image
    st.image(image_url, use_container_width=True)

    # Add text
    st.markdown("### Breathtaking Cityscapes")
    st.write("Explore the beauty of city environments with stunning visuals from around the world.")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Chat":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("💬 Chat Assistant")
    msg = st.text_input("Enter your message:")
    if st.button("Send") and msg:
        with st.spinner("Awaiting response..."):
            res = requests.post(f"{API_URL}/chat", json={"prompt": msg})
            st.success(res.json().get("response", "No response"))
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Text Correction":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("✍️ AI Text Correction")
    user_text = st.text_area("Enter text to correct")

    if st.button("Correct Text") and user_text:
        with st.spinner("Correcting using AI..."):
            try:
                res = requests.post(f"{API_URL}/text-correction", json={"text": user_text})  # ✅ Matches Prompt model
                data = res.json()
                corrected = data.get("corrected_text", "No correction available.")
                st.markdown("✅ **Corrected Text:**")
                st.success(corrected)
            except Exception as e:
                st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Eco Tip":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("🌿 Eco Tip")
    if st.button("Get Tip"):
        with st.spinner("Fetching tip..."):
            res = requests.get(f"{API_URL}/eco-tips")
            tip = res.json().get("tip", "No tip available")
            st.image("https://plus.unsplash.com/premium_photo-1663054675276-2ee41c543e4d?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)
            st.image("https://images.unsplash.com/photo-1564316706689-e56f4979877a?q=80&w=435&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",use_container_width=True)
            st.image("https://plus.unsplash.com/premium_photo-1682309652843-ed4eb60d473e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODF8fGVjbyUyMHRpcHN8ZW58MHx8MHx8fDA%3D",use_container_width=True)
            st.image("https://plus.unsplash.com/premium_photo-1664283229354-15322f237c29?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzY0fHxlY28lMjB0aXBzfGVufDB8fDB8fHww",use_container_width=True)

            st.success(tip)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Forecast":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("📈 KPI Forecasting")
    vals = st.text_input("Recent values (comma-separated):")
    if st.button("Forecast") and vals:
        try:
            data = [float(x) for x in vals.split(",")]
            df = pd.DataFrame({"period": list(range(1, len(data)+1)), "value": data})
            with st.spinner("Forecasting..."):
                res = requests.post(f"{API_URL}/forecast-kpi", json={"data": data})
                forecast = res.json().get("forecast_next_3_periods", [])
            # Plot input values
            chart1 = alt.Chart(df).mark_line(point=True).encode(x="period", y="value").properties(title="Historical KPI")
            st.altair_chart(chart1, use_container_width=True)
            # Plot forecast
            df2 = pd.DataFrame({"period": list(range(len(data)+1, len(data)+1+len(forecast))), "value": forecast})
            chart2 = alt.Chart(df2).mark_bar().encode(x="period", y="value").properties(title="Forecasted KPI")
            st.altair_chart(chart2, use_container_width=True)
        except:
            st.error("Invalid input. Use numbers separated by commas.")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Feedback":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("✉️ Submit Feedback")
    name = st.text_input("Your Name:")
    fb = st.text_area("Your feedback:")
    if st.button("Submit") and fb and name:
        with st.spinner("Submitting..."):
            res = requests.post(f"{API_URL}/submit-feedback", json={"user_id": name, "message": fb})
            st.success("Feedback submitted!")
    st.subheader("🗂️ All Feedback")
    try:
        res = requests.get(f"{API_URL}/feedback")
        for entry in res.json():
            st.markdown(f"**{entry['user_id']}**: {entry['message']}")
    except:
        st.error("Could not load feedback.")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Policy":
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("📃 Policy Summary")
    query = st.text_input("Query keyword:")
    text = st.text_area("Policy text:")
    if st.button("Summarize") and query and text:
        with st.spinner("Summarizing..."):
            res = requests.post(f"{API_URL}/policy-summary", json={"query": query, "policy_text": text})
            st.write(res.json().get("summary", "No summary"))
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Weather":
    st.subheader("⛅ Weather Info")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather") and city:
        try:
            res = requests.get(f"{API_URL}/weather", params={"city": city})
            data = res.json().get("weather", {})
            description = data.get("description", "No weather info available.")
            temperature = data.get("temp", None)
            st.markdown(f"**🌤️ Description:** {description}")
            if temperature is not None:
                st.markdown(f"**🌡️ Temperature:** {temperature}°C")
                st.image("https://plus.unsplash.com/premium_vector-1719419318571-56170f1faeaf?q=80&w=967&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",use_container_width=True)
        except Exception as e:
            st.error(f"Error fetching weather: {e}")

elif page == "Updates":
    st.subheader("📢 City Updates")
    st.image("https://plus.unsplash.com/premium_vector-1721803443495-05e308079127?q=80&w=580&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",use_container_width=True)
    city = st.text_input("Enter city name:")

    if st.button("Get Updates") and city:
        try:
            res = requests.get(f"{API_URL}/updates", params={"city": city})
            data = res.json().get("updates", {})
            description = data.get("description", "No update available.")
            temperature = data.get("temp", None)

            st.markdown(f"**📝 Description:** {description}")
            if temperature is not None:
                st.markdown(f"**🌡️ Temperature:** {temperature}°C")
                
        except Exception as e:
            st.error(f"Error fetching updates: {e}")

# Close scroll container
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)