import requests as re

def request(url,params = None):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://www.volkswagen.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.volkswagen.co.uk/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    

    response = re.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        return None
    








