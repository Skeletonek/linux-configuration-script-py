from clear import clear


def choose_apps():
    choice = []
    temp_choice = ""
    while temp_choice != "Y":
        clear()
        print("1. Firefox\n"
              "Y. Accept")
        temp_choice = input("Choice: ")
        if choice.__contains__(temp_choice):
            choice.remove("firefox")
        else:
            choice.append("firefox")
    return choice
