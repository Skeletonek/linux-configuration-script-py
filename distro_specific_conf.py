from clear import clear
import distro_specific_list_pretty

choice = []


def choose_distribution(linux):
    if linux == 1:
        choose_configuration(distro_specific_list_pretty.debian_configuration)
    elif linux == 2:
        choose_configuration(distro_specific_list_pretty.ubuntu_configuration)
    elif linux == 3:
        choose_configuration(distro_specific_list_pretty.fedora_configuration)
    elif linux == 4:
        choose_configuration(distro_specific_list_pretty.arch_configuration)
    return choice


def choose_configuration(local_conf_list):
    while True:
        clear()
        print("Choose configuration to apply: ")
        for i in local_conf_list:
            print("🗹" if choice.__contains__(i) > 0 else " ",
                  " ", i, ". - ", local_conf_list[i],
                  sep="")
        print("  E. - Return")
        temp_choice = input("Choice: ")

        if "eE".__contains__(temp_choice):
            break
        elif temp_choice.isnumeric():
            temp_choice = int(temp_choice)
            if choice.__contains__(temp_choice):
                choice.remove(temp_choice)
            else:
                choice.append(temp_choice)
