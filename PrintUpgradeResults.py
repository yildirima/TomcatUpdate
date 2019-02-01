from ConnectSSH import CallProcess

def PrintResults(TomcatHost, ServerIPADDR, BackupStatus, LinkStatus, TomcatServiceStatus, TomcatProcessID, TomcatBase):
    print("#############################################################\n")
    print("-----------------------Tomcat Upgrade-----------------------")
    print("Hostname                 :", TomcatHost)
    print("IPADDR                   :", ServerIPADDR)
    print("Tomcat Base Directory    :", TomcatBase)
    print("Backup File    Status    :", BackupStatus)
    print("Symbolic Link Status     :", LinkStatus)
    print("Tomcat Service Status    :", TomcatServiceStatus)
    print("Tomcat Process ID        :", TomcatProcessID)
    print("\n")
    print("#############################################################\n")