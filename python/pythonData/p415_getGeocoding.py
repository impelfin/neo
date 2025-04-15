#!/usr/bin/env python

import json
import os.path
import folium, requests
import pandas as pd

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

BASE_DIR = os.path.dirname(os.path.relpath("../../../"))
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

header = {'Authorization': 'KakaoAK ' + get_secret("kakao_apiKey")}

def getGeocoder(address):
    result = ""
    url = url_header + address
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

def makeMap(brand, store, getInfo):
    shopinfo = store + '(' + brand_dict[brand] + ')'
    mycolor = brand_color[brand]
    latitude, longitude = float(getInfo[0]), float(getInfo[1])

    marker = folium.Marker([latitude, longitude], popup=shopinfo, icon=folium.Icon(color=mycolor, icon='info-sign')).add_to((mapObject))

mylatitude = 37.4946203470469
mylongitude = 127.027606136235
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

brand_dict = {'cheogajip' : '처가집', 'pelicana' : '페리카나'}
brand_color = {'cheogajip' : 'red', 'pelicana' : 'blue'}

csvfile = 'NewChickenResult.csv'
myframe = pd.read_csv(csvfile, index_col=0, encoding='utf-8')

where = '강남구'
brandName = 'cheogajip'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData01 = myframe.loc[condition1 & condition2]

brandName = 'pelicana'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData02 = myframe.loc[condition1 & condition2]

mylist = []
mylist.append(mapData01)
mylist.append(mapData02)

mapData = pd.concat(mylist, axis=0)

ok = 0
notok = 0
for idx in range(len(mapData.index)):
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    getInfo = getGeocoder(address)

    if getInfo == None:
        print("Not OK : " + address)
        notok += 1
    else:
        print("OK : " + address)
        ok += 1
        makeMap(brand, store, getInfo)
    print('%' * 40)

total = ok + notok
print('ok : ', ok)
print('Not ok : ', notok)
print('total : ', total)

filename = 'xx_chickenMap.html'
mapObject.save(filename)
print('file saved...')

