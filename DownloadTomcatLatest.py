import requests
import  os
from ConnectSSH import CallProcess

def DownloadTomcatVersion(Host, NewTomcatVersion, TomcatExtract, TomcatUser):
    url = 'https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.92/bin/' + NewTomcatVersion
    r = requests.get(url)

    with open('/appdata/' + NewTomcatVersion, 'wb') as f:
        f.write(r.content)
        CopyBinary = '/bin/scp -pr /appdata/' + NewTomcatVersion + ' ' + Host +':' + TomcatExtract
        CopyBinaryOps = os.system(CopyBinary)
        CopyBinaryCo = 'cd /appdata ; tar -zxf /appdata/' + NewTomcatVersion
        RemoveTarBinary = '/bin/rm  -rf  ' + TomcatExtract + NewTomcatVersion
        MvBinary = '/bin/mv ' + TomcatExtract + 'apache-tomcat-* ' + TomcatExtract +'tomcat'
        ChownBinary = '/bin/chown -R ' + TomcatUser + ' ' + TomcatExtract
        ExtractFile = CallProcess(Host, CopyBinaryCo)
        RemoveFile = CallProcess(Host, RemoveTarBinary)
        MvFile = CallProcess(Host, MvBinary)
        ChFile = CallProcess(Host, ChownBinary)
    return r.status_code
# Retrieve HTTP meta-data
''' print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding) '''
