import requests

resp=requests.get("http://httpbin.org/")

#print status
print(resp.status_code)

#print text
print(resp.text)

#print headers
print(resp.headers)

