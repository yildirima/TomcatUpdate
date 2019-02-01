import subprocess

def CurrentVersionControl(TomcatVersionOutput):
    result = {}
    if ': ' in TomcatVersionOutput:
        key, value = TomcatVersionOutput.split(': ')
        result[key.strip(' .')] = value.strip()
    TomcatVersion = result['Server number']
    return TomcatVersion