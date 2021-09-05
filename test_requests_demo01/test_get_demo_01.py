import requests

response=requests.get("https://dev.yunyesoft.com/static/ocservice/app/1996/#/home")

print(response.content.decode('utf-8'))


