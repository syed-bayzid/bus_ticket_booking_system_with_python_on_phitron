from bus import Bus

class BusSystem:
    def __init__(self, ):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, total_seats):
        bus = Bus(number, route, total_seats)
        self.buses.append(bus)