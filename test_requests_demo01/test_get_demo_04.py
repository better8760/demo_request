import requests
import json
import jsonpath

#在python中dict,json对象数据
str_dict={'name':'xiaoming','age':22}

str1=json.dumps(str_dict)
print(type(str1))
print(str1)

str2='{"name":"xiaoming","age":22}'
str_json=json.loads(str2)
print(type(str_json))
print(str_json['age'])





