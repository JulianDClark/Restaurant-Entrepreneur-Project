from pancake import Pancake 
from sasuage import Sasuage
from eggs import Eggs
class MealFactory:
    @staticmethod
    def create_meal(type):
        if type == 'Pancake':
            return Pancake()
        elif type == 'Sasuage':
            return Sasuage()
        elif type == 'Eggs':
           return Eggs()
        
