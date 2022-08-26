import broker_app as app

def test_key():
    assert isinstance(app.alpaca_api_key, str)

def test_secret():
    assert isinstance(app.alpaca_api_secret, str)
