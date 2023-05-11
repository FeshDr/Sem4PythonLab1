from container import Container
from CONSTANTS import RULES, REG
import re
import os

if __name__ == "__main__":

    current_container: Container
    validator = 1

    print("Welcome to my container system")

    while (validator):
        get = input("Enter you name\n")
        try:
            current_container = Container(get)
            validator = 0
        except:
            print("Enter valid user name")

    validator = 1

    while (validator):
        get = input("Do y want to load your db? Y/N : ")
        if (get == "Y"):
            validator = 0
            current_container.load()
        elif (get == "N"):
            validator = 0
            print("OK")
        else:
            print("wrong Input")

    print(RULES)

    while (cmd := input()) != "Exit":

        os.system("clear")
        print(RULES)

        if (cmd == "A"):
            get = input("(Add function) Enter elements separated by spaces : ")
            current_container.add(re.findall(REG, get))
        elif (cmd == "R"):
            get = input(
                "(Remuve function) Enter elements separated by spaces : ")
            current_container.remuve(re.findall(REG, get))
        elif (cmd == "F"):
            get = input(
                "(Find function) Enter elements separated by spaces : ")
            current_container.find(re.findall(REG, get))
        elif (cmd == "L"):
            print("(List function)")
            current_container.list()
        elif (cmd == "G"):
            get = input("(Grep function) Enter regular expration : ")
            current_container.grep(get)
        elif (cmd == "Save"):
            current_container.save()
        elif (cmd == "Load"):
            current_container.load()
        elif (cmd == "Switch"):
            get = input("(Switch function) Enter new user name : ")
            current_container.switch(re.findall(REG, get)[0])

    ending = 1

    while (ending):
        get = input("Do y want to save your db? Y/N : ")
        if (get == "Y"):
            ending = 0
            current_container.save()
        elif (get == "N"):
            ending = 0
            print("OK")
        else:
            print("wrong Input")
