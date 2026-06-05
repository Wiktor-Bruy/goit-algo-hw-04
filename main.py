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
    name, phone = args
    if name in contacts:
        print("The contact already exists, do you want to overwrite it?")
        while True:
            cmd = input("Enter 'Yes' or 'No': ").strip().lower()
            if cmd == "yes":
                contacts[name] = phone
                return "Contact added."
            elif cmd == "no":
                return "You have cancelled the contact overwrite."
            else:
                print("Invalid comand.")

    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        print("Contact not found. Perhaps you wanted to add a new one?")
        while True:
            cmd = input("Enter 'Yes' or 'No': ").strip().lower()
            if cmd == "yes":
                contacts[name] = phone
                return "Contact added."
            elif cmd == "no":
                return "You have cancelled the contact change."
            else:
                print("Invalid comand.")

def get_phone(name: str, contacts: dict):
    if name in contacts:
        return f"Name: {name}; Phone: {contacts[name]}"
    else:
        return "Contact not found"

def all_contacts(contacts):
    for el in contacts:
        print(f"Name: {el}; Phone: {contacts[el]}")

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
                all_contacts(contacts)
            else:
                print("Your contacts is empty...")
        elif comand == "add":
            if len(list_arg) != 2:
                print("You may have misspelled the command. When adding a contact, "\
                    "you must include their name and number along with the command. "\
                    "They are separated by spaces.")
            else:
                print(add_contact(list_arg, contacts))
        elif comand == "phone":
            if len(list_arg) == 1:
                print(get_phone(list_arg[0], contacts))
            else:
                print("Invalid command. Use the 'help' command to get valid commands.")
        elif comand == "change":
            if len(list_arg) == 2:
                print(change_contact(list_arg, contacts))
            else:
                print("Invalid command. Use the 'help' command to get valid commands.")
        else:
            print("Invalid command. Use the 'help' command to get valid commands.")

if __name__ == "__main__":
    main()