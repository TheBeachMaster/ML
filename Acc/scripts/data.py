import requests
import json


headers = {
    'Authorization': 'Token sDSsNQYd9cmC',
    'Content-Type': 'application/json',
}

data = '{"texts":["I do not like cows"]}'

response = requests.post('https://api.uclassify.com/v1/ArthurKenOtieno/democlassifier/classify', headers=headers, data=data)

python_data = response.json()
print(type(python_data))
print(python_data)
