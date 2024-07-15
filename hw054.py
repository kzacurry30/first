
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Error: contact not find"
        except IndexError:
            return ("Invalid command. Usage: add [name] [phone]")

    return inner





def parse_input(user_input):
    """
    Parse user input into command and arguments.
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ''
    args = parts[1:] if len(parts) > 1 else []
    return command, args




@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."




@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."


@input_error
def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Error: contact not found."


@input_error
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."



def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 0:
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                print(add_contact(contacts, name, phone))
            elif len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Enter the argument for the command")
        elif command == "change":
            if len(args) == 0:
                name = input("Enter a name to change: ")
                phone = input("Enter a phone to change: ")
                print(change_contact(contacts, name, phone))
            elif len(args) == 2:
                name, phone = args
                print(change_contact(contacts, name, phone))
            else:
                print("Enter the argument for the command")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Enter the argument for the command")
        elif command == "all":
            print(show_all(contacts))
        elif command in ("close", "exit"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()