from ConnectSSH import CallProcess

def ServiceStatusControl(Host, ServiceName, Action):
    #p = subprocess.Popen(["service", ServiceName, Action], stdout=subprocess.PIPE)
    #out, err = p.communicate()
    #return out
    Command ='/sbin/service' + ' '+ ServiceName +' '+ Action
    out=CallProcess(Host, Command)
    return out

def ServiceControl(Host, ServiceName, Action):
    #p = subprocess.Popen(["service", ServiceName, Action], stdout=subprocess.PIPE)
    #out, err = p.communicate()
    #return out
    Command ='/sbin/service' + ' '+ ServiceName +' '+ Action
    out = CallProcess(Host, Command)
    return out

def ServiceMain(Host, ServiceName, Action):
    if Action == "status":
        out = ServiceStatusControl(Host, ServiceName, Action)
    elif Action == "start" or Action == 'stop':
        operation = ServiceControl(Host, ServiceName, Action)
        out = ServiceStatusControl(Host, ServiceName, Action)


    if ('running with pid' in str(out)):
       ServiceStatus = "Running"
    else:
        ServiceStatus = "Stopped"
    return ServiceStatus