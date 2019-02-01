from ConnectSSH import CallProcess

def RemoveFile(Host, FileCurrent):
    CommandFileOps = '/bin/rm -rf  ' + FileCurrent
    FileOps = CallProcess(Host, CommandFileOps)


def SymLink(Host, FileCurrent, FileDest):
    CommandSymLink = '/bin/ln -sf  ' + FileDest + ' ' + FileCurrent
    SymLink = CallProcess(Host, CommandSymLink)

'''TomcatBase = '/appdata/tomcat'
TomcatConfServer = '/appdata/bkm/tomcat/conf/server.xml'
degrlink = CreateSymLink('eagle', TomcatBase+'/conf/server.xml', TomcatConfServer)
print(degrlink)'''