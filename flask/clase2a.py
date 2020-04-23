import requests

url = "https://postman-echo.com/get"

payload = {"a": 1, "b":2, "c":3}
response = requests.request("GET", url, data = payload)
response.text


url = "https://postman-echo.com/post?z=23"

payload = {"a": 1, "b":2, "c":3}
response = requests.request("POST", url, data = payload)
response.text


url = "https://postman-echo.com/get?z=23"

payload = {"a": 1, "b":2, "c":3}
response = requests.request("GET", url, data = payload)
response.json()

### Tres formas de hacer un POST
## las tres se definen mediante el httpheader: Content-Type:
# application/x-www-form-urlencoded # forms / "datos simples"
# multipart/form-data # upload files <<
# application/json <<

