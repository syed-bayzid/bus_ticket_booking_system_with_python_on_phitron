class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        still_exist = self.total_seats - self.booked_seats
        return still_exist

    def book_seat(self, seat_numbers):
        if seat_numbers = 