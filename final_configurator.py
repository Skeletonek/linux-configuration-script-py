import os


def install_apps(linux, apps):
    if linux == 1 or linux == 2:
        os.system("apt update")
        command = "apt install -y"
    elif linux == 3:
        command = "dnf install -y"
    elif linux == 4:
        command = "pacman -Sy"
    for i in apps:
        command += " " + i
    return os.system(command)


def configure(linux, apps):
    print("Return code:", install_apps(linux,apps))
