from ConnectSSH import CallProcess
import time

def StartBackup(Host, TomcatBase):
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    Command = '/bin/mv' + ' ' + TomcatBase + ' ' + TomcatBase + '_' + timestr
    operation = CallProcess(Host, Command)
    return operation