from colorama import Fore, Back

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
      "Version: 9.02.23\n"
      "Author: Skeletonek (skeleton0199@gmail.com)\n\n",
      Back.RED + Fore.BLACK +
      "!!! This script must be run in su mode to complete all functions !!!",
      Back.RESET + Fore.RESET + "\n\n", sep="")

linux = distribution_chooser()
clear()

choice = " "
while not "yYeE".__contains__(choice):
    print("🗹" if len(app_choice) > 0 else " ", " 1. Choose what apps to install\n",
          "🗹" if len(conf_choice) > 0 else " ", " 2. Use distro-specific configurations\n",
          "🗹" if update > 0 else " ", " 3. Perform system update\n",
          "------------------------------------------------\n",
          "  Y. Accept all chosen operations and proceed\n",
          "  E. Exit without applying any chosen operations", sep="")
    choice = input("Choice: ")
    if choice == "1":
        app_choice = app_choser.choose_category()
    elif choice == "2":
        conf_choice = distro_specific_conf.choose_distribution(linux)
    elif choice == "3":
        update = not update
    clear()

clear()
if choice == ("y" or "Y"):
    final_configurator.configure(
        linux,
        app_choice,
        conf_choice,
        update)

# As a test, perform system update
# ret = os.system(f"sudo -S dnf update")  # TODO: Obfuscate password
# print(ret)
