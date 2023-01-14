from clear import clear
import distro_specific_list_pretty

choice = []


def choose_distribution():
    choose_configuration(distro_specific_list_pretty.fedora_configuration)
    return choice


def choose_configuration(local_conf_list):
    while True:
        clear()
        print("Choose configuration to apply: ")
        for i in local_conf_list:
            print("🗹" if choice.__contains__(i) > 0 else " ",
                  " ", i, ". - ", local_conf_list[i],
                  sep="")
        print("  Y. - Accept and exit")
        temp_choice = input("Choice: ")

        if temp_choice == "y":
            break
        elif temp_choice.isnumeric():
            temp_choice = int(temp_choice)
            if choice.__contains__(temp_choice):
                choice.remove(temp_choice)
            else:
                choice.append(temp_choice)
