class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        still_exist_seats = self.total_seats - self.booked_seats
        return still_exist_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        else:
            return False      

    def add_bus(self, number, route, seats)




                            
b = Bus("B101", "Dhaka-Sylhet", 20)
print(b.book_seat())          # True
print(b.book_seat())          # True
print(b.book_seat())          # False
print(b.book_seat())          # False
print(b.available_seats())    # 0