import requests

def fetch_market_data(symbol, api_key):
    url = f"http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbol}&limit=5"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def analyze_trends(data):
    prices = [entry['close'] for entry in data['data']]
    if len(prices) < 2:
        return "Not enough data to provide advice."
    trend = prices[-1] - prices[0]
    if trend > 0:
        return "The market trend is upward. Consider buying or holding."
    elif trend < 0:
        return "The market trend is downward. Consider selling or waiting."
    else:
        return "The market is stable. No strong recommendation."

def get_investment_advice(symbol, api_key):
    data = fetch_market_data(symbol, api_key)
    return analyze_trends(data)