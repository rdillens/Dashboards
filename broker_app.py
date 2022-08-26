# Import the required libraries and dependencies
import os
from dotenv import load_dotenv

import requests
from requests.auth import HTTPBasicAuth
import json
# import alpaca_trade_api as tradeapi

# import pandas as pd
import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

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
sandbox_endpoint = "https://broker-api.sandbox.alpaca.markets/"
production_endpoint = "https://broker-api.alpaca.markets/"
endpoint = sandbox_endpoint

post_str = endpoint + "v1/assets"
logging.debug(post_str)

# Get all assets in JSON
auth_str = HTTPBasicAuth(alpaca_api_key, alpaca_api_secret)
assets = requests.get(post_str, auth = auth_str).json()

class_list = sorted(list(set([asset["class"] for asset in assets])))
status_list = sorted(list(set([asset["status"] for asset in assets])))