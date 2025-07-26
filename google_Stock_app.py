import yfinance as yf
import streamlit as st
from datetime import date

# --------------------------------------------
# Title
# --------------------------------------------
st.set_page_config(page_title="Stock Viewer", layout="centered")
st.title("📊 Multi-Company Stock Viewer")
st.write("Explore stock price and volume data with historical charts and company information.")

# --------------------------------------------
# Company Dictionary
# --------------------------------------------
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Google (Alphabet)": "GOOGL",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Meta (Facebook)": "META",
    "NVIDIA": "NVDA",
    "Netflix": "NFLX",
    "Berkshire Hathaway": "BRK-B",
    "Visa": "V",
    "JPMorgan Chase": "JPM",
    "Johnson & Johnson": "JNJ",
    "UnitedHealth Group": "UNH",
    "Exxon Mobil": "XOM",
    "Procter & Gamble": "PG",
    "Mastercard": "MA",
    "Home Depot": "HD",
    "Pfizer": "PFE",
    "Coca-Cola": "KO",
    "Walmart": "WMT",
    "Bank of America": "BAC",
    "Intel": "INTC",
    "PepsiCo": "PEP",
    "Walt Disney": "DIS",
    "Chevron": "CVX",
    "Comcast": "CMCSA",
    "Adobe": "ADBE",
    "Salesforce": "CRM",
    "Cisco": "CSCO",
    "AbbVie": "ABBV",
    "Qualcomm": "QCOM",
    "Amgen": "AMGN",
    "Bristol-Myers Squibb": "BMY",
    "AT&T": "T",
    "Verizon": "VZ",
    "Oracle": "ORCL",
    "Ford": "F",
    "General Motors": "GM",
    "3M": "MMM",
    "Goldman Sachs": "GS",
    "American Express": "AXP",
    "Morgan Stanley": "MS",
    "Citigroup": "C",
    "Starbucks": "SBUX",
    "McDonald's": "MCD",
    "Nike": "NKE",
    "Costco": "COST",
    "PayPal": "PYPL",
    "Zoom Video": "ZM"
}

# --------------------------------------------
# User Inputs
# --------------------------------------------
selected_company = st.selectbox("Choose a company", list(companies.keys()))
tickerSymbol = companies[selected_company]

start_date = st.date_input("Start Date", value=date(2018, 1, 1))
end_date = st.date_input("End Date", value=date(2024, 12, 31))

show_ma = st.checkbox("Show 50-day Moving Average")

# --------------------------------------------
# Fetch and Display Data
# --------------------------------------------
with st.spinner("Fetching data..."):
    ticker = yf.Ticker(tickerSymbol)
    try:
        data = ticker.history(start=start_date, end=end_date)
        info = ticker.info
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        st.stop()

# --------------------------------------------
# Display Company Info
# --------------------------------------------
st.subheader(f"📌 {selected_company} ({tickerSymbol})")
st.markdown(f"""
- **Sector:** {info.get('sector', 'N/A')}
- **Market Cap:** {info.get('marketCap', 'N/A'):,}
- **Currency:** {info.get('currency', 'N/A')}
- **Country:** {info.get('country', 'N/A')}
""")

# --------------------------------------------
# Charts
# --------------------------------------------
st.subheader("📈 Stock Closing Price")
if show_ma:
    data["MA50"] = data["Close"].rolling(window=50).mean()
    st.line_chart(data[["Close", "MA50"]])
else:
    st.line_chart(data["Close"])

st.subheader("📉 Trading Volume")
st.line_chart(data["Volume"])
