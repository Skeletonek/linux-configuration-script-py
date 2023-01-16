import os
import distro_specific_list
import distro_specific_list_pretty
from colorama import Fore, Back, Style


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
        commands_pretty = distro_specific_list_pretty.debian_configuration
    elif linux == 2:
        commands = distro_specific_list.ubuntu_configuration
        commands_pretty = distro_specific_list_pretty.ubuntu_configuration
    elif linux == 3:
        commands = distro_specific_list.fedora_configuration
        commands_pretty = distro_specific_list_pretty.fedora_configuration
    elif linux == 4:
        commands = distro_specific_list.arch_configuration
        commands_pretty = distro_specific_list_pretty.arch_configuration

    for i in configuration:
        print(Fore.GREEN + commands_pretty[i])
        print(Fore.GREEN + "Performed command: ", commands[i])
        print(Fore.RESET)
        print(Back.WHITE + Fore.BLACK + "Return code:", os.system(commands[i]))
        print(Back.RESET + Fore.RESET)


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
    if len(apps) > 0:
        print(Fore.GREEN + "Installing choosen apps..." + Fore.RESET)
        print(Back.WHITE + Fore.BLACK + "Return code:", install_apps(linux, apps))
        print(Back.RESET + Fore.RESET)
    if len(configurations) > 0:
        system_configure(linux, configurations)
    if update:
        print(Fore.GREEN + "Updating system..." + Fore.RESET)
        print(Back.WHITE + Fore.BLACK + "Return code:", system_update(linux))
    print(Back.RESET + Fore.RESET + " \n ")
