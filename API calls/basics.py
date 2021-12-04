import requests

response = requests.get("https://www.dataquest.io/blog/python-api-tutorial/")

b=response.text
print(b)