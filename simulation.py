from franchise import franchise
class Simulation: 

    def run_simulation(self):
        franchise_one = franchise(111)
        franchise_two = franchise(22)
        franchise_three = franchise(333)

        franchise_one.place_order()
        franchise_three.place_order()
        franchise_two.place_order()
        franchise_one.place_order()
        franchise_three.place_order()
