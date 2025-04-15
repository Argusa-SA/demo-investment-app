import streamlit as st
import numpy as np
import pandas as pd

st.title("⚡ Risk Analysis")

if "selected_portfolio" in st.session_state:
    portfolio = st.session_state["selected_portfolio"]
    st.header(f"Risk Profile: {portfolio}")

    df = pd.read_csv("real_fund_data.csv", parse_dates=["Date"])
    returns = df["Daily Return"].dropna()

    vol = np.std(returns) * np.sqrt(252)
    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252)

    col1, col2 = st.columns(2)
    col1.metric("Volatility (Ann.)", f"{vol:.2%}")
    col2.metric("Sharpe Ratio", f"{sharpe:.2f}")

    st.progress(min(vol, 1.0))
else:
    st.warning("Please select a portfolio on the homepage first.")

if st.button("🏠 Back to Home"):
    st.switch_page("Home.py")
