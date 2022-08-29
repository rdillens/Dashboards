import broker_app as ab

def filter_exchanges(filter):
    return sorted(list(set([
        asset["exchange"] for asset in ab.assets if asset["class"] == filter
    ])))

def filter_assets(filter):
    return sorted(list(set([
            asset['symbol'] for asset in ab.assets 
            if asset["exchange"] == filter
    ])))

def get_asset_name(filter):
    return [
            asset['name'] for asset in ab.assets 
            if asset['symbol'] == filter
    ][0]

def get_asset_by_symbol(filter):
    return [
            asset for asset in ab.assets 
            if asset['symbol'] == filter
    ][0]

    