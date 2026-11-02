from bus import Bus

class BusSystem:
    def __init__(self, ):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        