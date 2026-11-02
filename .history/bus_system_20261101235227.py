from bus import Bus

class BusSystem:
    def __init__(self, ):
        self.buses = []
        self.passengers = []
    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return True

    def add_bus(self, number, route, seats):

        
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus {number} added successfully.")


system = BusSystem()
system.add_bus("B1", "Dhaka-Bogura", 40)   