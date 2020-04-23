import requests

resp = requests.get("https://api.ipify.org?format=json")
print(resp.json())
s = requests.Session()

proxies = {
  "https": "socks5://localhost:1080",
}
## proxies = {
#  "http://google": "http://10.10.1.10:5323",
#  "https://twitter": "http://123.213"
#}

resp = requests.get("https://api.ipify.org?format=json", proxies=proxies)
print(resp.json())