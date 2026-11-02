from bus import Bus

class BusSystem:
    def __init__(self, ):
        self.buses = []
        self.passengers = []
    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus

    def add_bus(self, number, route, seats):
        if self.find_bus(number) is True:
            print(f"Bus {number} already exists.")
            return

        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus {number} added successfully.")


system = BusSystem()
system.add_bus("B1", "Dhaka-Bogura", 40)   
system.add_bus("B1", "Dhaka-Bogura", 40)   