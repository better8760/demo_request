import requests

#信息头
header={
"Accept": "application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Type": "application/json;charset=UTF-8",
}



#写参数
get_param_data={
    "grant_type":"password",
    "username":"503168558581996",
    "password":"123456",
    "timestamp":1630833960021
}
response=requests.get(url="https://a1.easemob.com/1120161113115038/yunye/token",params=get_param_data,headers=header)

print(response.content.decode('utf-8'))




