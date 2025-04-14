import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Performance Analytics")

if "selected_portfolio" in st.session_state:
    portfolio = st.session_state["selected_portfolio"]
    st.header(f"Performance Overview: {portfolio}")

    dates = pd.date_range(start="2024-01-01", periods=100)
    returns = np.cumsum(np.random.randn(100))
    data = pd.DataFrame({"Date": dates, "Return": returns})

    st.line_chart(data.set_index("Date"))

    with st.expander("See detailed performance metrics"):
        st.write(f"**Average Return**: {np.mean(returns):.2f}")
        st.write(f"**Max Return**: {np.max(returns):.2f}")
        st.write(f"**Min Return**: {np.min(returns):.2f}")
else:
    st.error("⚠️ Please select a portfolio first in the 'Portfolio Selection' page.")
