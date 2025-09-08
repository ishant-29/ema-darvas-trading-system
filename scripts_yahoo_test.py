import yfinance as yf

# NIFTY 50 index
nifty = yf.Ticker("^NSEI")
nifty_hist = nifty.history(period="1y", interval="1d")
print("NIFTY rows:", len(nifty_hist))

# Indian stocks (NSE)
tickers = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
df = yf.download(tickers, period="1y", interval="1d", auto_adjust=True)

# Check if columns is MultiIndex
if hasattr(df.columns, "levels"):
    print("Multi download columns:", [list(level) for level in df.columns.levels])
else:
    # FrozenList or regular Index
    print("Multi download columns:", list(df.columns))
print(df)
