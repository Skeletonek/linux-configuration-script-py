import os
import distro_specific_list
import distro_specific_list_pretty


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


def system_configure(linux, configuration):
    if linux == 1:
        commands = distro_specific_list.debian_configuration
    elif linux == 2:
        commands = distro_specific_list.ubuntu_configuration
    elif linux == 3:
        commands = distro_specific_list.fedora_configuration
    elif linux == 4:
        commands = distro_specific_list.arch_configuration

    for i in configuration:
        print(distro_specific_list_pretty[i])
        print("Return code:", os.system(commands[i]))


def system_update(linux):
    if linux == 1 or linux == 2:
        os.system("apt update")
        command = "apt upgrade -y"
    elif linux == 3:
        command = "dnf update -y"
    elif linux == 4:
        command = "pacman -Syu"
    return os.system(command)


def configure(linux, apps, configurations ,update):
    if len(configurations) > 0:
        print("Return code:", install_apps(linux,apps))
    if len(configurations) > 0:
        system_configure(linux, configurations)
    if update:
        print("Return code:", system_update(linux))
