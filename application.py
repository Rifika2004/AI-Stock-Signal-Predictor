import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Title
st.title("📈 AI-Powered Stock Signal Predictor")

# Sidebar
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", "AAPL")

# Dummy historical data
dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
prices = np.linspace(100, 150, 30) + np.random.normal(0, 3, 30)

df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

# Plot
st.line_chart(df)

# Dummy AI Prediction
st.subheader("🤖 AI Prediction")
prediction = random.choice(["Buy", "Sell", "Hold"])
st.success(f"The AI suggests: **{prediction}** for {ticker.upper()}")

# Tech Stack Info
with st.expander("🧠 About This App"):
    st.markdown("""
    - Built with **Streamlit**
    - Dummy AI logic using Python `random`
    - Can be extended to use real stock APIs & ML models
    """)

# Footer
st.caption("Application by RIFIKA — AIML + Full Stack Developer")
