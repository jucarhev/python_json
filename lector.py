import json


#read json file

json_data=open('test1.json')

data = json.load(json_data)

print(str(data['Fruteria'][0]['Fruta'][0]['Nombre']))


