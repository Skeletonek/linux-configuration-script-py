import os


def configure(apps):
    command = "dnf install -y"
    for i in apps:
        command += " " + i
    ret = os.system(command)
    print("Return code:", ret)
