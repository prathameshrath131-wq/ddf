def main():
    print("""WELCOME TO AIRUS-OS
░█████╗░██╗██████╗░██╗░░░██╗░██████╗░░░░░░░█████╗░░██████╗
██╔══██╗██║██╔══██╗██║░░░██║██╔════╝░░░░░░██╔══██╗██╔════╝
███████║██║██████╔╝██║░░░██║╚█████╗░█████╗██║░░██║╚█████╗░
██╔══██║██║██╔══██╗██║░░░██║░╚═══██╗╚════╝██║░░██║░╚═══██╗
██║░░██║██║██║░░██║╚██████╔╝██████╔╝░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░░░░░╚════╝░╚═════╝░
""")
    name = input("Whats your name?: ")
    while True:
        command = input(f"\n{name}@airusos> ").strip().lower()

        if command == "exit":
            print("Shutting down...")
            break
        elif command == "help":
            print("\nAvailable commands: help, exit, hello, twins, state, about user, clear")
        elif command == "hello":
            print(f"\nHello, {name}!")
        elif command == "twins":
            print("\nReyansh,Ali,Aldana,Salim")
        elif command == "state":
            print("\nSystem state: Running no issues detected")
        elif command == "about user":
            print("\nHi im Kxr a 14 year old programmer who likes to make operating systems")
            print("\nRole: Administrator")
        elif command == "clear":
            print("\033[2J\033[1;1H")
        elif command == "":
            continue
        else:
            print(f"\nCommand not found: {command}")

if __name__ == "__main__":
    main()