import requests
url = 'https://coinmarketcap.com/historical/20180201/'
data = requests.get(url)
text = data.text
print(text[len(text) - 1])
