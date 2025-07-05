import requests

url = 'https://restcountries.com/v3.1/independent?status=true&fields=languages,capital'
response = requests.get(url)
print(response.json())