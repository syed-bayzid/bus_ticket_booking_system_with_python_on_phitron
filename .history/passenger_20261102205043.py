class Passenger:
    def __init__(self, name , phone, bus ):
        self.name= name
        self.phone = phone
        self.bus = []     def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus is None:
            print(f"Bus {bus_number} not found.")
            return 

        