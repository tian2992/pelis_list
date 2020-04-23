import http.client

#Primero creamos una conn
conn = http.client.HTTPSConnection("www.xkcd.com", port=443)
# conn.request("GET", "/hello")
conn.request("GET", "/")

response1 = conn.getresponse()
data1 = response1.read()

print(data1)
##

### POST
import http.client
import mimetypes

conn = http.client.HTTPSConnection("postman-echo.com")
payload = "This is expected to be sent back as part of response body."
headers = {}
conn.request("POST", "/post", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
