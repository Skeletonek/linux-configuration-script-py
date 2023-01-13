from clear import clear
import apps

choice = []


def print_choosen_apps():
    print("Current choice: ", end="")
    for i in choice:
        print(i, end=",")
    print()


def choose_category():
    temp_choice = ""
    while True:
        clear()
        print("Choose app category: ")
        for i in apps.categories_list:
            print(i, ". - ", apps.categories_list[i], sep="")
        print("Y. - Accept and exit")
        print_choosen_apps()
        temp_choice = input("Choice: ")
        if temp_choice == "y":
            break
        elif temp_choice == "1":
            choose_apps(apps.apps_list_audiovideo)
        elif temp_choice == "2":
            choose_apps(apps.apps_list_development)
        elif temp_choice == "3":
            choose_apps(apps.apps_list_education)
        elif temp_choice == "4":
            choose_apps(apps.apps_list_game)
        elif temp_choice == "5":
            choose_apps(apps.apps_list_graphics)
        elif temp_choice == "6":
            choose_apps(apps.apps_list_network)
        elif temp_choice == "7":
            choose_apps(apps.apps_list_office)
        elif temp_choice == "8":
            choose_apps(apps.apps_list_system)
        elif temp_choice == "9":
            choose_apps(apps.apps_list_utility)
    return choice


def choose_apps(local_apps_list):
    temp_choice = ""

    while True:
        clear()
        print("Choose app to install: ")
        for i in local_apps_list:
            print(i, ". - ", local_apps_list[i], sep="")
        print("Y. - Accept and exit")
        print_choosen_apps()
        temp_choice = input("Choice: ")

        if temp_choice == "y":
            break
        else:
            temp_choice = int(temp_choice)
        if choice.__contains__(local_apps_list[temp_choice]):
            choice.remove(local_apps_list[temp_choice])
        else:
            choice.append(local_apps_list[temp_choice])
