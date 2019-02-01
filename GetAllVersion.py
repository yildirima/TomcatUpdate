from bs4 import BeautifulSoup
from DownloadTomcatLatest import DownloadTomcatVersion
import requests



def GetAllVersion():
    url = 'https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.92/bin/'
    ext = '.tar.gz'
    def listFD(url, ext=''):
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        # return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    TomcatVersionList = listFD(url, ext)
    for idx, val in enumerate(TomcatVersionList):
        print(idx, ')', val);
    TomcatPath = int(input("Please enter the number to upgrade Tomcat : "))
    NewTomcatVersion = TomcatVersionList[TomcatPath]
    return NewTomcatVersion