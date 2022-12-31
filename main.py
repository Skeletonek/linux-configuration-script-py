import os
import getpass
from colorama import Fore, Back, Style

import app_choser
import final_configurator
from clear import clear


def distribution_chooser():
    print("Please choose your current Linux Distribution:\n"
          "1. Debian\n"
          "2. Ubuntu\n"
          "3. Fedora\n"
          "4. Arch Linux", sep="")
    return int(input("Distribution: "))


clear()
print("Linux Post-Install Configuration Script\n\n"
      "Version: 31.12.22\n"
      "Author: Skeletonek (skeleton0199@gmail.com)\n\n",
      Back.RED + Fore.BLACK +
      "!!! This script must be run in su mode to complete all functions !!!",
      Back.RESET + Fore.RESET + "\n\n", sep="")

linux = distribution_chooser()
clear()

choice = ""
while choice != "Y":
    print("1. Choose what apps to install\n"
          "Y. Accept all chosen operations and proceed...")
    choice = input("Choice: ")
    if choice == "1":
        app_choice = app_choser.choose_apps()
    clear()

clear()
final_configurator.configure(app_choice)

# As a test, perform system update
# ret = os.system(f"sudo -S dnf update")  # TODO: Obfuscate password
# print(ret)
