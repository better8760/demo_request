import requests


#写参数
get_param_data={
    "grant_type":"password",
    "username":"503168558581996",
    "password":"123456",
    "timestamp":1630833960021
}
response=requests.get("https://a1.easemob.com/1120161113115038/yunye/token",get_param_data)

print(response.content.decode('utf-8'))




