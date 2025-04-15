import time, datetime, ssl
import pandas as pd
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

class ChickenStore():
    myencoding = 'utf-8'

    def getWebDraiver(self, cmdJavaScript):
        print(cmdJavaScript)
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')
    
    def getSoup(self):
        if self.soup == None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')
    
    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
            if response.getcode() == 200:
                if self.brandName != 'pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response
        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url : %s' % (now, self.url)
            print(msg)
            return None
        
    def save2Csv(self, result):
        data = pd.DataFrame(result, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding=self.myencoding, index=True)

    def __init__(self, brandName, url):
        self.brandName = brandName
        self.url = url

        self.mycolumns = ['brand', 'store', 'sido', 'gungu', 'address']

        if self.brandName in ['pelicana', 'nene', 'cheogajip', 'goobne']:
            self.mycolumns.append('phone')
        else:
            pass
    
        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else:
            self.soup = None
            filepath = '/root/chromedriver/chromedriver'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)