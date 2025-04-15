import streamlit as st
from datetime import date
import pandas as pd

st.set_page_config(page_title="Investment Fund Dashboard", page_icon="💼", layout="wide")

st.title("💼 Investment Fund Dashboard")

with st.container():
    st.markdown("### Select your Portfolio and Simulation Parameters")

    portfolios = {
        "Growth Fund": "🚀 High-growth tech companies",
        "Stable Income Fund": "🏡 Bonds and dividend stocks",
        "Tech Innovators Fund": "🤖 Cutting-edge innovation"
    }

    selected_portfolio = st.radio("Choose a portfolio:", list(portfolios.keys()))
    st.session_state["selected_portfolio"] = selected_portfolio
    st.caption(portfolios[selected_portfolio])

    st.markdown("#### Simulation Settings")
    col1, col2, col3 = st.columns(3)

    with col1:
        start_date = st.date_input("Start Date", value=st.session_state.get("start_date", date(2022, 1, 1)))
        st.session_state["start_date"] = start_date

    with col2:
        end_date = st.date_input("End Date", value=st.session_state.get("end_date", date(2023, 12, 31)))
        st.session_state["end_date"] = end_date

    with col3:
        initial_investment = st.number_input("Initial Investment ($)", value=st.session_state.get("initial_investment", 10000), step=100)
        st.session_state["initial_investment"] = initial_investment

st.success(f"Portfolio '{selected_portfolio}' selected. Simulation from {start_date} to {end_date} with ${initial_investment:,}.")

col1, col2 = st.columns(2)
with col1:
    if st.button("📊 Go to Performance Analytics"):
        st.switch_page("pages/Performance_Analytics.py")
with col2:
    if st.button("⚡ Go to Risk Analysis"):
        st.switch_page("pages/Risk_Analysis.py")
