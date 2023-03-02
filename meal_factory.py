from pancake import Pancake 
from sasuage import Sasuage

class MealFactory:
    def create_meal(self,type):
        if type == 'Pancake':
            return Pancake()
        elif type == 'Sasuage':
            return Sasuage()
        