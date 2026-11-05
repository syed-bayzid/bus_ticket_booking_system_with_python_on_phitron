def user_menu(system, admin):
    while True:
        print("\n===== Bus Ticket Booking =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username == admin.username and password == admin.password:
                print("Admin login successful.")
                system.admin_logged_in = True
                while True:
                    print("\n===== Admin Menu =====")
                    print("1. Add Bus")
                    print("2. Remove Bus")
                    print("3. View Buses")
                    print("4. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        bus_number = input("Enter bus number: ")
                        route = input("Enter route: ")
                        seats = int(input("Enter number of seats: "))
                        system.add_bus(bus_number, route, seats)
                    elif admin_choice == "2":
                        bus_number = input("Enter bus number to remove: ")
                        system.remove_bus(bus_number)
                    elif admin_choice == "3":
                        system.show_buses()
                    elif admin_choice == "4":
                        system.admin_logged_in = False
                        print("Admin logged out.")
                        break
                    else:
                        print("Invalid choice. Please enter 1-4.")

        elif choice == "2":
            system.show_buses()
            bus_number = input("Enter bus number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone: ")
            system.book_ticket(bus_number, name, phone)
        elif choice == "3":
            system.show_buses()
        elif choice == "4":
            print("Exited the program.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

def admin_menu(system):
    while True:
        print("\n===== Admin Menu =====")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            bus_number = input("Enter bus number: ")
            route = input("Enter route: ")
            seats = int(input("Enter number of seats: "))
            system.add_bus(bus_number, route, seats)
        elif choice == "2":
            system.show_buses()
        elif choice == "3":
            system.admin_logged_in = False
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please enter 1-3.")