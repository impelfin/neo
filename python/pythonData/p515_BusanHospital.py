import json, urllib.request, datetime, math
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath('./')))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getHospitalData(pageNo, numOfRows):
    end_point='https://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'
    
    paramter = ''
    paramter += "?resultType=json"
    paramter += "&serviceKey=" + get_secret('data_apiKey')
    paramter += "&pageNo=" + str(pageNo)
    paramter += "&numOfRows=" + str(numOfRows)
    url = end_point + paramter
    
    print("URL : ")
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)

jsonResult = []

pageNo = 1
numOfRows = 100
nPage = 0

while True:
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    print(jsonData)

    if (jsonData['response']['header']['resultCode'] == '00'):
        totalCount = jsonData['response']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)  

        for item in jsonData['response']['body']['items']['item']:
            jsonResult.append(item)

        if totalCount == 0:
            break
        nPage = math.ceil(int(totalCount) / int(numOfRows))
        if (pageNo == nPage):  
            break  

        pageNo += 1
    else :
        break

    savedFilename = 'p515_BusanHospital.json'
    with open(savedFilename, 'w', encoding='utf-8') as outfile:
        resJson = json.dumps(jsonResult, indent=4, ensure_ascii=False, sort_keys=True)
        outfile.write(resJson)
    
    print(savedFilename + ' file saved..')
