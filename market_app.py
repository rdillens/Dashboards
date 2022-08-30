# Import the required libraries and dependencies
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from dotenv import load_dotenv

import requests
from requests.auth import HTTPBasicAuth
import json

from utils import api_hooks as ah

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
     

# Set API endpoint
# Base URL for Alpaca Market API
base_url = "https://data.sandbox.alpaca.markets/v2"

# Websocket URL
source = 'iex'
wss_url = f"wss://stream.data.sandbox.alpaca.markets/v2/{source}"

symbol = 'AAPL'
get_str = base_url + f'/stocks/{symbol}/bars'

# Get bars in JSON
auth_str = HTTPBasicAuth(alpaca_api_key, alpaca_api_secret)
bars_2 = ah.get_bars('AAPL')
# bars = requests.get(get_str, params = {'timeframe':'1Min'}, auth = auth_str).json()

# print(bars_2)
logging.debug("done")
