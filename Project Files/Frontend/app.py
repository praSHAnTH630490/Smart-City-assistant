
import os
import requests
import streamlit as st
import pandas as pd
import altair as alt
from dotenv import load_dotenv

# ============================================================
# ENVIRONMENT CONFIGURATION
# ============================================================

load_dotenv()

API_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000"
).rstrip("/")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart City Assistant",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewBlockContainer"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    [data-testid="stSidebar"] {
        background-color: #ffffee !important;
    }

    .main-title {
        font-size: 3em;
        text-align: center;
        color: #ffffff !important;
        padding: 20px;
        background: linear-gradient(
            to right,
            #833ab4,
            #fd1d1d,
            #fcb045
        );
        border-radius: 20px;
        margin: 1rem auto;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    }

    .feature-card {
        background: linear-gradient(
            to bottom right,
            #6faddb,
            #ff6eff
        );
        border: 2px solid #eaeaea;
        border-radius: 30px;
        padding: 2rem;
        margin-bottom: 20px;
        color: #000000 !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.10);
    }

    .feature-card h1,
    .feature-card h2,
    .feature-card h3,
    .feature-card p {
        color: #000000 !important;
    }

    .stButton > button {
        background: linear-gradient(
            135deg,
            #fcb045,
            #ff8a00
        );
        color: #000000 !important;
        padding: 8px 16px;
        border-radius: 12px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        background: #ffffff !important;
    }

    input,
    textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# API HELPER FUNCTIONS
# ============================================================

def post_request(endpoint, payload, timeout=90):
    """Send POST request to FastAPI backend."""

    try:
        response = requests.post(
            f"{API_URL}{endpoint}",
            json=payload,
            timeout=timeout
        )
        return response

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Cannot connect to the FastAPI backend. "
            "Make sure Uvicorn is running on "
            "http://127.0.0.1:8000"
        )

    except requests.exceptions.Timeout:
        st.error(
            "⏳ Backend request timed out."
        )

    except requests.exceptions.RequestException as e:
        st.error(
            f"❌ Request error: {e}"
        )

    return None


def get_request(endpoint, params=None, timeout=90):
    """Send GET request to FastAPI backend."""

    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            params=params,
            timeout=timeout
        )
        return response

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Cannot connect to the FastAPI backend. "
            "Make sure Uvicorn is running on "
            "http://127.0.0.1:8000"
        )

    except requests.exceptions.Timeout:
        st.error(
            "⏳ Backend request timed out."
        )

    except requests.exceptions.RequestException as e:
        st.error(
            f"❌ Request error: {e}"
        )

    return None


def display_api_error(response):
    """Display backend error."""

    try:
        data = response.json()
        detail = data.get(
            "detail",
            "Unknown backend error."
        )
    except Exception:
        detail = response.text or "Unknown backend error."

    st.error(
        f"Backend Error ({response.status_code}): {detail}"
    )


# ============================================================
# MAIN TITLE
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🏙️ WELCOME TO THE SMART CITY ASSISTANT
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("📂 Navigate")

page = st.sidebar.selectbox(
    "Select Feature",
    [
        "Home",
        "Updates",
        "Chat",
        "Text Correction",
        "Eco Tip",
        "Forecast",
        "Policy",
        "Weather",
        "Feedback"
    ]
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title("Smart City Services")


# ============================================================
# HOME
# ============================================================

if page == "Home":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    image_url = (
        "https://images.unsplash.com/"
        "photo-1507090960745-b32f65d3113a"
        "?q=80&w=1470&auto=format&fit=crop"
    )

    st.image(
        image_url,
        width="stretch"
    )

    st.markdown(
        "### 🌆 Breathtaking Cityscapes"
    )

    st.write(
        "Explore the beauty of city environments "
        "with stunning visuals from around the world."
    )

    st.write(
        "Use the navigation menu to access "
        "AI-powered smart city services."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CHAT ASSISTANT
# ============================================================

elif page == "Chat":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("💬 AI Chat Assistant")

    msg = st.text_area(
        "Enter your message:",
        placeholder="Ask something about smart cities..."
    )

    if st.button("🚀 Send Message") and msg.strip():

        with st.spinner("🤖 AI is thinking..."):

            response = post_request(
                "/chat",
                {
                    "prompt": msg.strip()
                }
            )

        if response is not None:

            if response.ok:

                try:

                    data = response.json()

                    answer = data.get(
                        "response",
                        "No response received."
                    )

                    st.markdown(
                        "### 🤖 Assistant"
                    )

                    st.success(answer)

                except Exception:

                    st.error(
                        "Invalid response received from backend."
                    )

            else:

                display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TEXT CORRECTION
# ============================================================

elif page == "Text Correction":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("✍️ AI Text Correction")

    user_text = st.text_area(
        "Enter text to correct:",
        height=180
    )

    if st.button("✅ Correct Text") and user_text.strip():

        with st.spinner("Correcting text..."):

            response = post_request(
                "/text-correction",
                {
                    "text": user_text.strip()
                }
            )

        if response is not None:

            if response.ok:

                try:

                    data = response.json()

                    corrected = data.get(
                        "corrected_text",
                        "No correction available."
                    )

                    st.markdown(
                        "### ✅ Corrected Text"
                    )

                    st.success(corrected)

                except Exception:

                    st.error(
                        "Invalid backend response."
                    )

            else:

                display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ECO TIP
# ============================================================

elif page == "Eco Tip":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("🌿 Eco-Friendly Tip")

    if st.button("🌱 Get Eco Tip"):

        with st.spinner(
            "Generating eco-friendly tip..."
        ):

            response = get_request(
                "/eco-tips"
            )

        if response is not None:

            if response.ok:

                try:

                    tip = response.json().get(
                        "tip",
                        "No tip available."
                    )

                    st.markdown(
                        "### 🌱 Today's Eco Tip"
                    )

                    st.success(tip)

                    st.image(
                        "https://images.unsplash.com/"
                        "photo-1564316706689-e56f4979877a"
                        "?q=80&w=1000&auto=format&fit=crop",
                        width="stretch"
                    )

                except Exception:

                    st.error(
                        "Invalid backend response."
                    )

            else:

                display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI FORECAST
# ============================================================

elif page == "Forecast":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("📈 KPI Forecasting")

    vals = st.text_input(
        "Recent values (comma-separated):",
        placeholder="10, 12, 15, 18, 20"
    )

    if st.button("📊 Forecast") and vals.strip():

        try:

            data = [
                float(x.strip())
                for x in vals.split(",")
                if x.strip()
            ]

            if not data:

                st.warning(
                    "Please enter at least one value."
                )

            else:

                with st.spinner(
                    "Generating forecast..."
                ):

                    response = post_request(
                        "/forecast-kpi",
                        {
                            "data": data
                        }
                    )

                if response is not None:

                    if response.ok:

                        result = response.json()

                        forecast = result.get(
                            "forecast_next_3_periods",
                            []
                        )

                        # Historical data
                        historical_df = pd.DataFrame(
                            {
                                "period": range(
                                    1,
                                    len(data) + 1
                                ),
                                "value": data
                            }
                        )

                        chart1 = (
                            alt.Chart(
                                historical_df
                            )
                            .mark_line(point=True)
                            .encode(
                                x="period",
                                y="value"
                            )
                            .properties(
                                title="Historical KPI"
                            )
                        )

                        st.altair_chart(
                            chart1,
                            width="stretch"
                        )

                        # Forecast
                        if forecast:

                            try:

                                forecast_values = [
                                    float(x)
                                    for x in forecast
                                ]

                                forecast_df = pd.DataFrame(
                                    {
                                        "period": range(
                                            len(data) + 1,
                                            len(data)
                                            + 1
                                            + len(forecast_values)
                                        ),
                                        "value": forecast_values
                                    }
                                )

                                chart2 = (
                                    alt.Chart(
                                        forecast_df
                                    )
                                    .mark_bar()
                                    .encode(
                                        x="period",
                                        y="value"
                                    )
                                    .properties(
                                        title="Forecasted KPI"
                                    )
                                )

                                st.altair_chart(
                                    chart2,
                                    width="stretch"
                                )

                            except Exception:

                                st.warning(
                                    "Forecast was returned "
                                    "but could not be plotted."
                                )

                        else:

                            st.warning(
                                "The AI did not return "
                                "a valid forecast."
                            )

                    else:

                        display_api_error(response)

        except ValueError:

            st.error(
                "❌ Invalid input. "
                "Use numbers separated by commas."
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FEEDBACK
# ============================================================

elif page == "Feedback":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("✉️ Submit Feedback")

    name = st.text_input(
        "Your Name:"
    )

    feedback = st.text_area(
        "Your Feedback:"
    )

    if st.button("📨 Submit Feedback"):

        if not name.strip():

            st.warning(
                "Please enter your name."
            )

        elif not feedback.strip():

            st.warning(
                "Please enter your feedback."
            )

        else:

            with st.spinner(
                "Submitting feedback..."
            ):

                response = post_request(
                    "/submit-feedback",
                    {
                        "user_id": name.strip(),
                        "message": feedback.strip()
                    }
                )

            if response is not None:

                if response.ok:

                    st.success(
                        "✅ Feedback submitted successfully!"
                    )

                else:

                    display_api_error(response)

    st.markdown("---")

    st.subheader("🗂️ All Feedback")

    response = get_request(
        "/feedback"
    )

    if response is not None:

        if response.ok:

            try:

                items = response.json()

                if items:

                    for item in items:

                        st.markdown(
                            f"**👤 {item.get('user_id', 'Unknown')}**"
                        )

                        st.write(
                            item.get(
                                "message",
                                ""
                            )
                        )

                        st.divider()

                else:

                    st.info(
                        "No feedback submitted yet."
                    )

            except Exception:

                st.error(
                    "Could not read feedback."
                )

        else:

            display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# POLICY SUMMARY
# ============================================================

elif page == "Policy":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("📃 City Policy Summary")

    query = st.text_input(
        "Query keyword:"
    )

    policy_text = st.text_area(
        "Policy text:",
        height=220
    )

    if st.button("📝 Summarize Policy"):

        if not query.strip():

            st.warning(
                "Please enter a query keyword."
            )

        elif not policy_text.strip():

            st.warning(
                "Please enter policy text."
            )

        else:

            with st.spinner(
                "Summarizing policy..."
            ):

                response = post_request(
                    "/policy-summary",
                    {
                        "query": query.strip(),
                        "policy_text": policy_text.strip()
                    }
                )

            if response is not None:

                if response.ok:

                    try:

                        summary = response.json().get(
                            "summary",
                            "No summary available."
                        )

                        st.markdown(
                            "### 📋 Summary"
                        )

                        st.write(summary)

                    except Exception:

                        st.error(
                            "Invalid backend response."
                        )

                else:

                    display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# WEATHER
# ============================================================

elif page == "Weather":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("⛅ Weather Information")

    city = st.text_input(
        "Enter city name:",
        placeholder="Example: Hyderabad"
    )

    if st.button("🌤️ Get Weather") and city.strip():

        with st.spinner(
            "Fetching weather information..."
        ):

            response = get_request(
                "/weather",
                params={
                    "city": city.strip()
                }
            )

        if response is not None:

            if response.ok:

                try:

                    weather_data = response.json().get(
                        "weather",
                        {}
                    )

                    description = weather_data.get(
                        "description",
                        "No weather information available."
                    )

                    temperature = weather_data.get(
                        "temp"
                    )

                    st.markdown(
                        "### 🌤️ Weather Result"
                    )

                    st.write(description)

                    if temperature is not None:

                        st.write(
                            f"🌡️ Temperature: "
                            f"{temperature}°C"
                        )

                except Exception:

                    st.error(
                        "Invalid weather response."
                    )

            else:

                display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CITY UPDATES
# ============================================================

elif page == "Updates":

    st.markdown(
        '<div class="feature-card">',
        unsafe_allow_html=True
    )

    st.subheader("📢 City Updates")

    st.image(
        "https://images.unsplash.com/"
        "photo-1494526585095-c41746248156"
        "?q=80&w=1200&auto=format&fit=crop",
        width="stretch"
    )

    city = st.text_input(
        "Enter city name:",
        placeholder="Example: Hyderabad"
    )

    if st.button("📢 Get Updates") and city.strip():

        with st.spinner(
            "Getting city updates..."
        ):

            response = get_request(
                "/updates",
                params={
                    "city": city.strip()
                }
            )

        if response is not None:

            if response.ok:

                try:

                    updates = response.json().get(
                        "updates",
                        {}
                    )

                    description = updates.get(
                        "description",
                        "No update available."
                    )

                    temperature = updates.get(
                        "temp"
                    )

                    st.markdown(
                        "### 📰 Latest City Updates"
                    )

                    st.write(description)

                    if temperature is not None:

                        st.write(
                            f"🌡️ Temperature: "
                            f"{temperature}°C"
                        )

                except Exception:

                    st.error(
                        "Invalid updates response."
                    )

            else:

                display_api_error(response)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )
