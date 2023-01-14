import os
import getpass
from colorama import Fore, Back, Style

import app_choser
import distro_specific_conf
import final_configurator
from clear import clear


def distribution_chooser():
    print("Please choose your current Linux Distribution:\n"
          "1. Debian\n"
          "2. Ubuntu\n"
          "3. Fedora\n"
          "4. Arch Linux", sep="")
    return int(input("Distribution: "))


app_choice = []
conf_choice = []
update = False

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
while choice != "y":
    print("🗹" if len(app_choice) > 0 else " ", " 1. Choose what apps to install\n",
          "🗹" if len(conf_choice) > 0 else " ", " 2. Use distro-specific configurations\n",
          "🗹" if update > 0 else " ", " 3. Perform system update\n",
          "  Y. Accept all chosen operations and proceed...", sep="")
    choice = input("Choice: ")
    if choice == "1":
        app_choice = app_choser.choose_category()
    elif choice == "2":
        conf_choice = distro_specific_conf.choose_distribution()
    elif choice == "3":
        update = not update
    clear()

clear()
final_configurator.configure(
    linux,
    app_choice,
    conf_choice,
    update)

# As a test, perform system update
# ret = os.system(f"sudo -S dnf update")  # TODO: Obfuscate password
# print(ret)
