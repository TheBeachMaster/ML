import requests
import json


headers = {
    'Authorization': 'Token sDSsNQYd9cmC',
    'Content-Type': 'application/json',
}

data = '{"texts":["yeah right"]}'

requests.post('https://api.uclassify.com/v1/ArthurKenOtieno/democlassifier/classify', headers=headers, data=data)

parsed_json = json.loads(json_string)
print(parsed_json['first_name'])