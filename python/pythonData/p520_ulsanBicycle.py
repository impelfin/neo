import json, urllib.request, datetime, math
import pandas as pd
import xml.etree.ElementTree as ET
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
        # print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getBicycleData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6310000/ulsanbicyclepath/getUlsanbicyclepathList'

    parameters = '?'
    parameters += "ServiceKey=" + get_secret("data_apiKey")
    parameters += "&pageNo=" + str(pageNo) 
    parameters += "&numOfRows=" + str(numOfRows) 
    url = end_point + parameters

    print('URL')
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return result

dataList = []

pageNo = 1 
numOfRows = 2
nPage = 0

while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    xmlData = getBicycleData(pageNo, numOfRows)
    print(xmlData)
    xmlTree = ET.fromstring(xmlData)

    if (xmlTree.find('header').find('resultMsg').text == 'success'):
        totalCount = int(xmlTree.find('body').find('totalCount').text)
        print('데이터 총 개수 : ', totalCount)  

        listTree = xmlTree.find('body').find('data').findall('list')
        print(listTree)

        for node in listTree:
            bikeFirstLanes = node.find("bikeFirstLanes").text
            bikeFirstLanesRatio = node.find("bikeFirstLanesRatio").text
            bikeLanesRatio = node.find('bikeLanesRatio').text
            bikeOnlyLanes = node.find('bikeOnlyLanes')
            if bikeOnlyLanes == None:
                bikeOnlyLanes = ""
            else:
                bikeOnlyLanes = bikeOnlyLanes.text

            bikeOnlyLanesRatio = node.find('bikeOnlyLanesRatio').text
            cycleRoute = node.find('cycleRoute').text
            entId = node.find('entId').text
            gugun = node.find('gugun').text
            pedestrianBikeLanes = node.find('pedestrianBikeLanes').text
            pedestrianBikeLanesRatio = node.find('pedestrianBikeLanesRatio').text

            onedict = {'자전거 우선 도로' : bikeFirstLanes, \
                       '자전거 우선 도로 비율' : bikeFirstLanesRatio, \
                       '자전거 전용 도로 비율' : bikeLanesRatio, \
                       '자전거 전용 차로' : bikeOnlyLanes, \
                       '자전거 전용 차로 비율' : bikeOnlyLanesRatio, \
                       '자전거 전용 도로' : cycleRoute, '고유번호':entId, "군구":gugun, \
                       '자전거 보행자 겸용 도로' : pedestrianBikeLanes, \
                       '자전거 보행자 겸용 도로 비율' : pedestrianBikeLanesRatio}
            dataList.append(onedict)

        if totalCount == 0:
            break
        nPage = math.ceil(totalCount / numOfRows)

        if (pageNo == nPage):
            break
        
        pageNo += 1
    else:
        break

savedFilename = 'p520_Ulsan_Bicycle.json'

myframe = pd.DataFrame(dataList)
myframe.to_csv(savedFilename)

print(savedFilename + ' file saved..')


