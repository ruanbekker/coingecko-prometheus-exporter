"""
API Documentation: https://www.coingecko.com/en/api#explore-api
"""

from flask import Flask, Response
from prometheus_client import Counter, Gauge, start_http_server, generate_latest
import requests
import json
import time
import os

GC_REQUEST_URL = "https://api.coingecko.com/api/v3/coins/markets"
GC_HEADERS = {"content-type": "application/json"}
GC_PARAMETERS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False,
    "price_change_percentage": "24h",
    "ids": os.environ['CRYPTO_COINS']
}

MIME_CONTENT_TYPE = "text/plain; version=0.0.4; charset=utf-8"

app = Flask(__name__)

def request_prices():
    response = requests.get(GC_REQUEST_URL, headers=GC_HEADERS, params=GC_PARAMETERS).json()
    return response

def format_prices():
    current_prices = []
    retrieved_prices = request_prices()
    for coin in retrieved_prices:
        formatted_info = {}
        formatted_info['id'] = coin['id']
        formatted_info['symbol'] = coin['symbol']
        formatted_info['current_price'] = format(coin['current_price'], '.8f')
        formatted_info['market_cap'] = coin['market_cap']
        formatted_info['high_24h'] = format(coin['high_24h'], '.8f')
        formatted_info['low_24h'] = format(coin['low_24h'], '.8f')
        formatted_info['price_change_percentage_24h'] = coin['price_change_percentage_24h']
        formatted_info['circulating_supply'] = coin['circulating_supply']
        current_prices.append(formatted_info)
    return current_prices

coingecko_current_price = Gauge(
        'coingecko_current_price',
        'current price of crypto currency in usd',
        ['name', 'symbol', 'fiat_currency']
)

@app.route('/metrics')
def metrics():
    metrics = format_prices()
    for coin_info in metrics:
        coingecko_current_price.labels(name=coin_info['id'], symbol=coin_info['symbol'], fiat_currency='usd').set(format(coin_info['current_price']))
    return Response(generate_latest(), mimetype=MIME_CONTENT_TYPE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
