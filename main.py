from bus_system import BusSystem
from menu import user_menu
from admin import Admin
system = BusSystem()

admin = Admin("admin", "1234")

user_menu(system, admin)