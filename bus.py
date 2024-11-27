class BusTicketBot:
    def __init__(self):
        self.routes = {
            "Trivandrum to Kasargod": {"time": "10:00 AM", "price": 20, "available_tickets": 50},
            "Trivandrum to Kochi": {"time": "1:00 PM", "price": 25, "available_tickets": 40},
            "Trivandrum to Kollam": {"time": "3:00 PM", "price": 15, "available_tickets": 30},
        }
        self.bookings = []

    def show_routes(self):
        print("Available Bus Routes:")
        for route, details in self.routes.items():
            print(f"- {route} at {details['time']} (${details['price']}, {details['available_tickets']} available)")

    def book_ticket(self, route_name, quantity):
        print(f"Attempting to book {quantity} tickets for {route_name}...")
        route = self.routes.get(route_name)
        print(f"Route found: {route}")  # Debugging line
        if route and route['available_tickets'] >= quantity:
            route['available_tickets'] -= quantity
            self.bookings.append({"route": route_name, "quantity": quantity})
            print(f"Booked {quantity} tickets for {route_name}.")
        else:
            print("Booking failed: Not enough tickets or route not found.")

    def show_bookings(self):
        if self.bookings:
            print("Your Bookings:")
            for b in self.bookings:
                print(f"- {b['quantity']} tickets for {b['route']}")
        else:
            print("You have no bookings.")

    def cancel_ticket(self, route_name):
        for booking in self.bookings:
            if booking['route'] == route_name:
                self.bookings.remove(booking)
                self.routes[route_name]['available_tickets'] += booking['quantity']
                print(f"Canceled {booking['quantity']} tickets for {route_name}.")
                return
        print("No booking found for this route.")

    def run(self):
        while True:
            print("\n1. Show Routes\n2. Book Tickets\n3. Show Bookings\n4. Cancel Booking\n5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                route_name = input("Enter route (e.g., 'Trivandrum to Kasargod'): ")
                if route_name not in self.routes:
                    print("Invalid route name. Please try again.")
                    continue
                try:
                    quantity = int(input("Enter number of tickets to book: "))
                    if quantity <= 0:
                        print("Please enter a valid number of tickets.")
                        continue
                    self.book_ticket(route_name, quantity)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                self.show_bookings()
            elif choice == "4":
                route_name = input("Enter route to cancel: ")
                if route_name not in self.routes:
                    print("Invalid route name. Please try again.")
                    continue
                self.cancel_ticket(route_name)
            elif choice == "5":
                print("Thank you for using Bus TicketBot!")
                break
            else:
                print("Invalid option. Please choose again.")

if __name__ == "__main__":
    BusTicketBot().run()
