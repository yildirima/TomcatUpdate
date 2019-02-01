import os.path
import argparse
import configparser
from TomcatVersionControl import CurrentVersionControl
from GetAllVersion import GetAllVersion
from ServiceStatus import ServiceMain
from ConnectSSH import CallProcess
from StartBackup import StartBackup
from DownloadTomcatLatest import DownloadTomcatVersion
from CreateSymLink import RemoveFile
from CreateSymLink import SymLink
from PrintUpgradeResults import PrintResults
def parser_arg():
    parser = argparse.ArgumentParser(description="Define Configuration  file for Tomcat Instance")
    parser.add_argument("-f", "--file", help="Define configuration  file  name", type=str)
    args = parser.parse_args()
    return args.file
def main():
    config_file = parser_arg()
    if not config_file:
        print("HELP:Use  -f  option to define configuration file.\n"
              "     Ex: python main_function.py -f  <update_config>")
    else:
        config = configparser.ConfigParser()
        config.read(config_file)
        '''Tomcat Base Directory'''
        TomcatHost = config.get('Tomcat', 'TomcatHost')
        TomcatBase = config.get('Tomcat', 'TomcatBase')
        TomcatExtract = config.get('Tomcat', 'TomcatExtract')
        TomcatUser = config.get('Tomcat', 'TomcatUser')

        '''Tomcat Config File'''
        TomcatConfigServer = config.get('TomcatConfigFile', 'TomcatConfigServer')
        TomcatConfigContext = config.get('TomcatConfigFile', 'TomcatConfigContext')
        TomcatConfigUser = config.get('TomcatConfigFile', 'TomcatConfigUser')
        TomcatConfigWeb = config.get('TomcatConfigFile', 'TomcatConfigWeb')

        '''Tomcat Environment  File'''
        TomcatSetEnv = config.get('TomcatEnvironmentFile', 'TomcatSetEnv')
        TomcatSetVars = config.get('TomcatEnvironmentFile', 'TomcatSetVars')

        '''Tomcat Application and  Log directories'''
        TomcatWebapps = config.get('TomcatDirectory', 'TomcatWebapps')
        TomcatLogs = config.get('TomcatDirectory', 'TomcatLogs')
        TomcatExtLib = config.get('TomcatDirectory', 'TomcatExtLib')
        while True:
            # TomcatPath = input("Please enter Tomcat BASE Directory: ")
            TomcatVersionSH = TomcatBase + '/bin/version.sh'
            CheckFileCommand = '/usr/bin/test ' + TomcatVersionSH + ' && echo $?'
            CheckFileExists = CallProcess(TomcatHost, CheckFileCommand).strip()
            if CheckFileExists == '0':
                TomcatBaseCommand=TomcatBase + '/bin/version.sh' + '|grep  number'
                #TomcatVersSH = TomcatBase + '/bin/version.sh' + '|grep  number'
                TomcatVersSH = CallProcess(TomcatHost, TomcatBaseCommand)
                TomcatCurrentVersion = CurrentVersionControl(TomcatVersSH)
                TomcatVersionUpgrade = GetAllVersion()
                TomcatServiceStatus = ServiceMain(TomcatHost,'tomcat', 'status')
                ServerHostname = CallProcess(TomcatHost,'hostname').strip()
                ServerIPADDR = CallProcess(TomcatHost, "ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}'|grep  -v 127.0.0.1").strip()
                ##print('{} {}'.format(TomcatCurrentVersion, TomcatVersionUpgrade))
                print("#######################Analyze#################################\n")
                print("-----------------------Tomcat General------------------------")
                print("Hostname                 :", ServerHostname)
                print("IPADDR                   :", ServerIPADDR)
                print("Tomcat Base Directory    :", TomcatBase)
                print("Tomcat Application User  :", TomcatUser)
                print("Tomcat Service Status    :", TomcatServiceStatus)
                print("Tomcat Version           :", TomcatCurrentVersion)
                print("Tomcat Update Version    :", TomcatVersionUpgrade)
                print("-----------------------Tomcat Links--------------------------")
                print("Tomcat Server XML File   :", TomcatConfigServer)
                print("Tomcat Context XML File  :", TomcatConfigContext)
                print("Tomcat User XML File     :", TomcatConfigUser)
                print("Tomcat Web  XML File     :", TomcatConfigWeb)
                print("-----------------------Tomcat Binaries-----------------------")
                print("Tomcat Environment File  :", TomcatSetEnv)
                print("Tomcat Additional Var    :", TomcatSetVars)
                print("-----------------------Tomcat Directories--------------------")
                print("Tomcat Logs Directory    :", TomcatLogs)
                print("Tomcat WebApps Directory :", TomcatWebapps)
                print("Tomcat Ext.Lib Directory :", TomcatExtLib)
                print("\n")
                print("#############################################################\n")
                print("Do you want to perform upgrade  operation with this config set[Y/N]:")
                UpgradeYes = input("")
                if UpgradeYes == 'Y':
                    ServiceMain(TomcatHost, 'cron', 'stop')
                    BackupStatus = StartBackup(TomcatHost, TomcatBase)
                    if BackupStatus == '':
                        BackupStatus = 'OK'
                        DownloadTomcat = DownloadTomcatVersion(TomcatHost, TomcatVersionUpgrade, TomcatExtract, TomcatUser)
                        if ('200'in str(DownloadTomcat)):
                            DownloadTomcat = 'OK'
                            if (TomcatLogs != '') or (TomcatWebapps != '') or (TomcatConfigServer != '') or \
                                    (TomcatConfigContext != '') or (TomcatConfigWeb != '') or \
                                    (TomcatConfigUser != '') or (TomcatSetEnv != '') or (TomcatSetVars != ''):
                                CreateLink = "OK"
                                if TomcatLogs != '':
                                    rmLogs = RemoveFile(TomcatHost, TomcatBase + '/logs')
                                    SymLogs = SymLink(TomcatHost, TomcatBase + '/logs', TomcatLogs)
                                if TomcatWebapps != '':
                                    rmWebapps = RemoveFile(TomcatHost, TomcatBase + '/webapps')
                                    SymWebapps = SymLink(TomcatHost, TomcatBase + '/webapps', TomcatWebapps)
                                if TomcatConfigServer != '':
                                    rmConfServer = RemoveFile(TomcatHost, TomcatBase + '/conf/server.xml')
                                    SymConfServer = SymLink(TomcatHost, TomcatBase + '/conf/server.xml',
                                                            TomcatConfigServer)
                                if TomcatConfigContext != '':
                                    rmConfContext = RemoveFile(TomcatHost, TomcatBase + '/conf/context.xml')
                                    SymConfContext = SymLink(TomcatHost, TomcatBase + '/conf/context.xml',
                                                             TomcatConfigContext)
                                if TomcatConfigWeb != '':
                                    rmConfWeb = RemoveFile(TomcatHost, TomcatBase + '/conf/web.xml')
                                    SymConfWeb = SymLink(TomcatHost, TomcatBase + '/conf/web.xml', TomcatConfigWeb)
                                if TomcatConfigUser != '':
                                    rmconfTomcatUser = RemoveFile(TomcatHost, TomcatBase + '/conf/tomcat-users.xml')
                                    SymConfTomcatUser = SymLink(TomcatHost, TomcatBase + '/conf/tomcat-users.xml',
                                                                TomcatConfigUser)
                                if TomcatSetEnv != '':
                                    SymEnvBin = SymLink(TomcatHost, TomcatBase + '/bin/setenv.sh', TomcatSetEnv)
                                if TomcatSetVars != '':
                                    SymEnvVar = SymLink(TomcatHost, TomcatBase + '/bin/setvars.sh', TomcatSetVars)
                                ServiceMain(TomcatHost, 'tomcat', 'start')
                                TomcatServiceStatus = ServiceMain(TomcatHost, 'tomcat', 'status')
                                ProcessCommand = '/bin/ps -ef |grep ' + \
                                                 TomcatBase + " |/bin/grep -v grep|awk  '{print $2}'"
                                TomcatProcessID = CallProcess(TomcatHost, ProcessCommand)
                                PrintResults(ServerHostname, ServerIPADDR, BackupStatus, CreateLink, TomcatServiceStatus, TomcatProcessID, TomcatBase)
                            else:
                                CreateLink = 'Passed'
                        else:
                            DownloadTomcat = 'Failed'

                    else:
                        BackupStatus == 'Failed'

                else:
                    break
                '''print('Do you want to upgrade tomcat version from {} to {} [Y/N] \n'.format(TomcatCurrentVersion,
                                                                                         TomcatVersionUpgrade))'''
                break
            else:
                print("You entered wrong tomcat base directory:Please check config file . There  is  no file  that : ", TomcatVersionSH)
                break
main()