
from fastapi import FastAPI
import yfinance as yf
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/aia-stock")

@app.get("/aia-stock")
def get_stock():
    ticker = yf.Ticker("1299.HK")
    info = ticker.info

    current_price = info.get("currentPrice")
    market_cap = info.get("marketCap")
    shares_outstanding = info.get("sharesOutstanding")

    formatted_price = f"HK${current_price:,.2f}" if current_price else "N/A"
    formatted_market_cap = f"HK${market_cap / 1e9:,.2f}B" if market_cap else "N/A"
    formatted_shares = f"{shares_outstanding / 1e9:,.2f}B" if shares_outstanding else "N/A"

    return {
        "current_price": formatted_price,
        "market_cap": formatted_market_cap,
        "shares_outstanding": formatted_shares
        }
