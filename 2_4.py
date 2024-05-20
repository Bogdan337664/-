class Airline:
    aircrafts = []
    routes = []

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)
        print(self.aircrafts)
        return self.aircrafts

    def deregister_aircraft(self, aircraft):
        self.aircrafts.remove(aircraft)
        print(self.aircrafts)
        return self.aircrafts

    def add_route(self, route):
        self.routes.append(route)
        print(self.routes)
        return self.routes

    def remove_route(self, route):
        self.routes.remove(route)
        print(self.routes)
        return self.routes

    def search_aircraft(self, model):
        matching_aircrafts = [aircraft for aircraft in self.aircrafts if model == aircraft]
        print(*matching_aircrafts)
        return matching_aircrafts

    def search_route(self, city):
        matching_routes = [route for route in self.routes if city in route]
        print(*matching_routes)
        return matching_routes

skyline = Airline()
skyline.register_aircraft('bz')
skyline.add_route('a - b')
skyline.add_route('d - f')
skyline.search_route('d')
