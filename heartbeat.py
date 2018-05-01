import requests
import warnings

il_url = 'https://10.147.72.11'
il_api_port = 8080

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    response = requests.get('{}:{}/heartbeat'.format(il_url, il_api_port), verify=False)
    print(response.json())

