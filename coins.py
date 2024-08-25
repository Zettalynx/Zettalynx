import requests
from html import escape

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': '10',
    'page': '1'
}

def fetch_coins(api_url, params):
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

def update_readme(coins):
    with open('README.md', 'r') as f:
        readme_content = f.readlines()
    
    start_marker = "<!--START_SECTION:coins-->"
    end_marker = "<!--END_SECTION:coins-->"
    start_idx = None
    end_idx = None

    for idx, line in enumerate(readme_content):
        if start_marker in line:
            start_idx = idx
        if end_marker in line:
            end_idx = idx

    new_content = '\n'
    new_content += '<div style="overflow-x:auto;">\n'
    new_content += '<table style="width: 100%; border-collapse: collapse; color: white;">\n'
    new_content += '  <tr>\n'
    new_content += '    <th style="border: 1px solid white; padding: 10px;">#</th>\n'
    new_content += '    <th style="border: 1px solid white; padding: 10px;">Coin</th>\n'
    new_content += '    <th style="border: 1px solid white; padding: 10px;">Current Price (USD)</th>\n'
    new_content += '    <th style="border: 1px solid white; padding: 10px;">Market Cap (USD)</th>\n'
    new_content += '    <th style="border: 1px solid white; padding: 10px;">24h Volume (USD)</th>\n'
    new_content += '  </tr>\n'

    for coin in coins:
        new_content += '  <tr>\n'
        new_content += f'    <td style="border: 1px solid white; padding: 10px;">{coin["rank"]}</td>\n'
        new_content += f'    <td style="border: 1px solid white; padding: 10px;">'
        new_content += f'<img src="{coin["image"]}" alt="Coin Image" style="width: 50px; height: auto; vertical-align: middle;"> '
        new_content += f'<span style="vertical-align: middle;">{escape(coin["name"])} ({escape(coin["symbol"].upper())})</span>'
        new_content += '</td>\n'
        new_content += f'    <td style="border: 1px solid white; padding: 10px;">${coin["current_price"]:,.2f}</td>\n'
        new_content += f'    <td style="border: 1px solid white; padding: 10px;">${coin["market_cap"]:,.2f}</td>\n'
        new_content += f'    <td style="border: 1px solid white; padding: 10px;">${coin["total_volume"]:,.2f}</td>\n'
        new_content += '  </tr>\n'

    new_content += '</table>\n'
    new_content += '</div>\n'
    new_content += '\n'
    
    if start_idx is not None and end_idx is not None:
        updated_content = readme_content[:start_idx + 1] + [new_content] + readme_content[end_idx:]
        
        with open('README.md', 'w') as f:
            f.writelines(updated_content)

if __name__ == "__main__":
    coins_data = fetch_coins(COINGECKO_API_URL, PARAMS)
    coins = [{
        'rank': i + 1,
        'image': coin['image'],
        'name': coin['name'],
        'symbol': coin['symbol'],
        'current_price': coin['current_price'],
        'market_cap': coin['market_cap'],
        'total_volume': coin['total_volume']
    } for i, coin in enumerate(coins_data)]
    
    update_readme(coins)
