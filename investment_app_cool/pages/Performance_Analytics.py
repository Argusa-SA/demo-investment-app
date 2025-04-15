import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Performance Analytics")

if "selected_portfolio" in st.session_state:
    portfolio = st.session_state["selected_portfolio"]
    st.header(f"Performance Overview: {portfolio}")

    # Set unique seed per portfolio for different random walks
    portfolio_seeds = {
        "Growth Fund": 42,
        "Stable Income Fund": 7,
        "Tech Innovators Fund": 21
    }

    np.random.seed(portfolio_seeds.get(portfolio, 0))

    # Generate random walk data
    full_dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq="B")
    price = 100 + np.cumsum(np.random.randn(len(full_dates)) * 0.5)
    returns = np.diff(price) / price[:-1]
    df_all = pd.DataFrame({
        "Date": full_dates[1:],
        "Price": price[1:],
        "Daily Return": returns
    })

    # Filter by selected dates
    start = pd.to_datetime(st.session_state.get("start_date", "2022-01-01"))
    end = pd.to_datetime(st.session_state.get("end_date", "2023-12-31"))
    initial = st.session_state.get("initial_investment", 10000)

    df = df_all[(df_all["Date"] >= start) & (df_all["Date"] <= end)].copy()
    df["Value"] = df["Price"] / df["Price"].iloc[0] * initial

    st.plotly_chart(px.line(df, x="Date", y="Value", title="Portfolio Value Over Time"), use_container_width=True)

    # Metrics
    avg_return = df["Daily Return"].mean() * 252  # annualized
    total_return = (df["Value"].iloc[-1] / df["Value"].iloc[0] - 1) * 100
    final_amount = df["Value"].iloc[-1]

    col1, col2, col3 = st.columns(3)
    col1.metric("📈 Total Return", f"{total_return:.2f} %")
    col2.metric("📊 Avg Annual Return", f"{avg_return*100:.2f} %")
    col3.metric("💰 Final Amount", f"{final_amount:,.2f} CHF")

    st.download_button("📥 Download CSV", df.to_csv(index=False).encode(), file_name="portfolio_simulation.csv")
else:
    st.warning("Please select a portfolio on the homepage first.")

if st.button("🏠 Back to Home"):
    st.switch_page("Home.py")
