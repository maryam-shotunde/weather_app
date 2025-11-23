#weather app using API
import requests
api_key = 'a755a657573c4b5cb49143655252311' 
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=Banjul'

response = requests.get(url)
print(response.status_code)
print(response.text)