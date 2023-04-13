from meal_factory import MealFactory
from logger import Logger
class franchise:
    def __init__(self, location_number) -> None:
        self.location_number = location_number
        
        def place_order(self):
            # Ask Users what food they want
            user_choice = input('What would you like to order?  (Pancake, Sausage, or Eggs?) > ')
            # use OrderFactory to create order 
            user_order = MealFactory.create_meal(user_choice)
            # use logger to log order to txt file 
            Logger.log_transaction(user_order, self.location_number)
