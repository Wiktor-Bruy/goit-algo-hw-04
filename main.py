from cmath import phase
from math import fabs
from os import name


comands = ['"hello" - to start',
          '"exit" or "close" - to close programm',
          '"help" - return valid comands',
          '"add [name] [phone]" - to add contacts',
          '"change [name] [phone]" - to change contact',
          '"phone [name]" - to get phone',
          '"all" - to get all contacts']

def parse_comand(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, args

def add_contact(args: list, contacts: dict):
    if len(args) != 2:
        return False
    name, phone = args
    if name in contacts:
        return "contact exist"
    contacts[name] = phone
    return "Caontact added."

def change_contact(args: list, contacts: dict):
    if len(args) != 2:
        return False
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed"
    return "not found"
    

def get_phone(args: list, contacts: dict):
    if len(args) != 1:
        return False
    name = args[0]
    if name in contacts:
        return f"Name: {name}; Phone: {contacts[name]}"
    else:
        return "Contact not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ").strip()
        comand, list_arg = parse_comand(user_inp)

        if comand in ["exit", "close"]:
            print("Good bye!")
            break
        elif comand == "hello":
            print("How can I help you?")
        elif comand == "help":
            for comand in comands:
                print(comand)
        elif comand == "all":
            if len(contacts) > 0:
                for name in contacts:
                    print(f"Name: {name}, Phone: {contacts[name]}")
            else:
                print("Your contacts is empty...")
        elif comand == "add":
            res =  add_contact(list_arg, contacts)
            if res:
                if res == "contact exist":
                    print("This contact already exists. Would you like to change it?")
                    while True:
                        cmd = input("Enter Yes or No: ").strip().lower()
                        if cmd == "yes":
                            print(change_contact(list_arg, contacts))
                            break
                        elif cmd == "no":
                            print("You have cancelled the contact change.")
                            break
                        else:
                            print("Invalid comand.")
                else:
                    print(res)
            else:
                print("Invalid command. Use the 'help' command to get valid commands.")
        elif comand == "phone":
            res = get_phone(list_arg, contacts)
            if res:
                print(res)
            else:
                print("Invalid command. Use the 'help' command to get valid commands.")
        elif comand == "change":
            res = change_contact(list_arg, contacts)
            if res:
                if res == "not found":
                    print("This contact doesn't exist. Perhaps you wanted to add a new one?")
                    while True:
                        cmd = input("Enter Yes or No: ").strip().lower()
                        if cmd == "yes":
                            print(add_contact(list_arg, contacts))
                            break
                        elif cmd == "no":
                            print("You have canceled adding a contact.")
                            break
                        else:
                            print("Invalid comand")
                else:
                    print(res)
            else:
                print("Invalid command. Use the 'help' command to get valid commands.")
        else:
            print("Invalid command. Use the 'help' command to get valid commands.")

if __name__ == "__main__":
    main()