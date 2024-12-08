import requests

def get_gold_price():
    url = 'https://api.gold-api.com/price/XAU'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gold price data: {e}")
        return None

def get_asset_price(asset):
    url = f'https://api.gold-api.com/price/{asset}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching asset - {asset} price data: {e}")
        return None