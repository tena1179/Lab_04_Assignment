class Flight_Information:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        matching_flights = [flight for flight in self.flights if flight.origin == city or flight.destination == city]
        return matching_flights

    def search_by_origin(self, origin):
        matching_flights = [flight for flight in self.flights if flight.origin == origin]
        return matching_flights

    def search_between_cities(self, origin, destination):
        matching_flights = [flight for flight in self.flights if flight.origin == origin and flight.destination == destination]
        return matching_flights

def main():
    flight_database = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for flight_info in flight_data:
        flight_id, origin, destination, price = flight_info
        flight = Flight_Information(flight_id, origin, destination, price)
        flight_database.add_flight(flight)

    while True:
        print("Tena Priyadarsini.Pabbati")
        print("E22CSEU1179")
        print(".......Flight List:......")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Quit")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            city_to_search = input("Enter the city: ")
            matching_flights = flight_database.search_by_city(city_to_search)
        elif user_choice == 2:
            origin_to_search = input("Enter the origin city: ")
            matching_flights = flight_database.search_by_origin(origin_to_search)
        elif user_choice == 3:
            origin_to_search = input("Enter the origin city: ")
            destination_to_search = input("Enter the destination city: ")
            matching_flights = flight_database.search_between_cities(origin_to_search, destination_to_search)
        elif user_choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if matching_flights:
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in matching_flights:
                print(f"{flight.flight_id}\t{flight.origin}\t{flight.destination}\t{flight.price}")
        else:
            print("No flights found for the selected criteria.")

if __name__ == "__main__":
    main()
