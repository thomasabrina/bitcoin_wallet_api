import requests

def fetch_eur_to_btc_rate():
    try:
        response = requests.get('http://api-cryptopia.adca.sh/v1/prices/ticker')
        data = response.json()
        # Loop through the data to find the BTC/EUR conversion rate
        for item in data['data']:
            if item['symbol'] == 'BTC/EUR':
                return float(item['value'])
        print("BTC/EUR conversion rate not found.")
        return None
    except Exception as e:
        print(f"Failed to fetch conversion rate: {e}")
        return None