import streamlit as st
import numpy as np

st.title("⚡ Risk Analysis")

if "selected_portfolio" in st.session_state:
    portfolio = st.session_state["selected_portfolio"]
    st.header(f"Risk Profile: {portfolio}")

    col1, col2 = st.columns(2)

    with col1:
        volatility = np.round(np.random.uniform(0.1, 0.5), 2)
        st.metric(label="Volatility", value=f"{volatility * 100:.2f}%", delta=f"{np.round(np.random.uniform(-2, 2), 2)}%")

    with col2:
        sharpe_ratio = np.round(np.random.uniform(0.5, 2.0), 2)
        st.metric(label="Sharpe Ratio", value=sharpe_ratio, delta=f"{np.round(np.random.uniform(-0.2, 0.2), 2)}")

    st.progress(min(volatility, 1.0))
else:
    st.error("⚠️ Please select a portfolio first in the 'Portfolio Selection' page.")
