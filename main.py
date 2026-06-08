
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
        return "Invalid command. Use the 'help' command to get valid commands."
    name, phone = args
    contacts[name] = phone
    return "Caontact added."

def change_contact(args: list, contacts: dict):
    if len(args) != 2:
        return "Invalid command. Use the 'help' command to get valid commands."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed"
    return "Contact not found"
    

def get_phone(args: list, contacts: dict):
    if len(args) != 1:
        return "Invalid command. Use the 'help' command to get valid commands."
    name = args[0]
    if name in contacts:
        return f"Name: {name}; Phone: {contacts[name]}"
    else:
        return "Contact not found"

def get_all(contacts: list):
    if len(contacts) > 0:
        return contacts
    else:
        return "Your contacts is empty..."

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
            print(get_all(contacts))
        elif comand == "add":
            print(add_contact(list_arg, contacts))
        elif comand == "phone":
            print(get_phone(list_arg, contacts))
        elif comand == "change":
            print(change_contact(list_arg, contacts))
        else:
            print("Invalid command. Use the 'help' command to get valid commands.")

if __name__ == "__main__":
    main()