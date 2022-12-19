import os
import getpass
from colorama import Fore, Back, Style

print("Linux Post-Install Configuration Script\n\n"
      "Version: 19.12.22\n"
      "Author: Skeletonek (skeleton0199@gmail.com)\n\n",
      Back.RED + Fore.BLACK + "!!! This script must be run in su mode to complete all functions !!!",
      Back.RESET + Fore.RESET + "\n\n", sep="")

# As a test, perform system update
ret = os.system(f"sudo -S dnf update")  # Obfuscate password
print(ret)
