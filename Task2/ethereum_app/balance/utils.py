import requests

def fetch_ethereum_data(address):
    api_endpoint = 'https://api.etherscan.io/api'
    api_key = 'G9UX6EDRUWI1RMI2CGES1RVB6RG18BRFVP' 

    params = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': api_key
    }

    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        balance = data['result']

        params['action'] = 'txlist'
        params['startblock'] = 0
        params['endblock'] = 99999999

        response = requests.get(api_endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            transactions = data['result']

            return {
                'balance': balance,
                'transactions': transactions[:5]
            }
        else:
            return {
                'error': 'Failed to fetch transactions'
            }
    else:
        return {
            'error': 'Failed to fetch balance'
        }


# valid address
# 1. 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B
# 2. 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
# 3. 0x5d22045dAe9C7f73d20cC7bC0d7b0A4A4d4Bf097