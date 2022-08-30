import logging
logging.basicConfig(level=logging.INFO)

import requests
from requests.auth import HTTPBasicAuth
import json

import os
from dotenv import load_dotenv
# Load .env environment variables
load_dotenv()
try:
    alpaca_api_key = os.getenv("ALPACA_BROKER_API_KEY")
    alpaca_api_secret = os.getenv("ALPACA_BROKER_API_SECRET")
except Exception as e:
    logging.error(e)
    raise(e)
else:
    logging.debug(f"key type: {type(alpaca_api_key)}")
    logging.debug(f"secret type: {type(alpaca_api_secret)}")   
     

# Base URL for Alpaca Market API
base_url = "https://data.sandbox.alpaca.markets/v2"

# Websocket URL
source = 'iex'
wss_url = f"wss://stream.data.sandbox.alpaca.markets/v2/{source}"

# Set API endpoint
sandbox_endpoint = "https://broker-api.sandbox.alpaca.markets/"
production_endpoint = "https://broker-api.alpaca.markets/"
endpoint = sandbox_endpoint

post_str = endpoint + "v1/assets"

auth_str = HTTPBasicAuth(alpaca_api_key, alpaca_api_secret)

def get_assets():
    return requests.get(post_str, auth = auth_str).json()

def get_bars(
        symbol, 
        timeframe='1Min', 
        start=None,
        end=None,
        limit=None,
        page_token=None,
        adjustment=None,
        asof=None,
        feed=None,

    ):
    params = {
        'timeframe': timeframe,
        'start': start,
        'end': end,
        'limit': limit,
        'page_token': page_token,
        'adjustment': adjustment,
        'asof': asof,
        'feed': feed,
    }
    get_str = base_url + f'/stocks/{symbol}/bars'
    logging.debug("done in function")
    return requests.get(get_str, params = params, auth = auth_str).json()
    # return requests.get(get_str, params = {'timeframe':'1Min'}, auth = auth_str).json()
