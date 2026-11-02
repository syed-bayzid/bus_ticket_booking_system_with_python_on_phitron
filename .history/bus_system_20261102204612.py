from bus import Bus
from passenger import Passenger

class BusSystem:
    def __init__(self, ):
        self.buses = []
        self.passengers = []
        
    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus

    def add_bus(self, number, route, seats):
        if self.find_bus(number) is not None:
            print(f"Bus {number} already exists.")
            return

        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus {number} added successfully.")
    
    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus is None:
            print(f"Bus {bus_number} not found.")
            return 

        if bus.a

        
    # def show_buses(self):
    
# system = BusSystem()
# system.add_bus("B1", "Dhaka-Bogura", 40)   
# system.add_bus("B1", "Dhaka-Bogura", 40)   

system = BusSystem()
system.admin_logged_in = True
system.add_bus("B1", "Dhaka-Bogura", 2)      # মাত্র ২ সিট

system.book_ticket("X9", "Rahim", "017")     # Bus not found
system.book_ticket("B1", "Rahim", "017")     # টিকিট ১
system.book_ticket("B1", "Karim", "018")     # টিকিট ২
system.book_ticket("B1", "Salma", "019")     # no seats available
print(len(system.passengers))                 # 2