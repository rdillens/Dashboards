# Import the required libraries and dependencies
import os
from dotenv import load_dotenv

import requests
from requests.auth import HTTPBasicAuth
# import json
# import alpaca_trade_api as tradeapi

# import pandas as pd
import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

# Load .env environment variables
load_dotenv()
try:
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_api_secret = os.getenv("ALPACA_API_SECRET")
except Exception as e:
    logging.error(e)
    raise(e)
else:
    logging.debug(f"key type: {type(alpaca_api_key)}")
    logging.debug(f"secret type: {type(alpaca_api_secret)}")   
     