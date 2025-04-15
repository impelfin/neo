import json
import os.path
import folium, requests

# address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'
address = '서울특별시 서초구 서초대로74길 33'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

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
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address= r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

address_latlng = getGeocoder(address)
latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소지:', address)
print('위도:', latitude)
print('경도:', longitude)

shopinfo = '비트빌'
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker(location=[latitude, longitude], popup=shopinfo, icon=myicon).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius=150, color='blue', fill_color='red', fill=False, popup=shopinfo).add_to(foli_map)
foli_map.save('p413_getGeocoding.html')
print('file saved..')