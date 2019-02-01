import subprocess


def CallProcess(HOST, COMMAND):
    ssh = subprocess.run(["ssh", HOST, COMMAND],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=False)
    result = ssh.stdout.decode("utf-8")
    return result