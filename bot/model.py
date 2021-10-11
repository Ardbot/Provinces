# https://github.com/hflabs/dadata-py

from dadata import Dadata
import json
import requests

# token = "0ae2f514cfe8de3e37cba837af111de588ab60fb"
# dadata = Dadata(token)
# # result = dadata.suggest("oktmo", "10630000")
# # result = dadata.find_by_id("oktmo", "10630000")
# result = dadata.clean(name="address", source="мск сухонская 11 89")
# print(result)


def Postindex(p_index):
    url = f'https://www.postindexapi.ru/json/{p_index[:3]}/{p_index}.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        # Region = data['Region']
        # Autonom = data['Autonom']
        # Area = data['Area']
        # City = data['City']
        # msg = Region, Autonom, Area, City
        # print(msg)
        # print(data)
        return data
    else:
        return f"Ошибка {p_index}"

# print(Postindex('679000'))

