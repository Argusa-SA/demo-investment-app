import streamlit as st

st.title("📈 Portfolio Selection")

st.subheader("Choose the investment fund you're interested in:")

portfolios = {
    "Growth Fund": "🚀 Focus on high growth companies.",
    "Stable Income Fund": "🏡 Focus on steady income with bonds.",
    "Tech Innovators Fund": "🤖 Focus on technology leaders."
}

portfolio = st.radio("Select a portfolio:", list(portfolios.keys()))

st.session_state["selected_portfolio"] = portfolio

st.success(f"You selected: {portfolio} - {portfolios[portfolio]}")
