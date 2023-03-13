class Pizza():
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost
        
    def get_description(self):
        return self.__description
    
    def get_cost(self):
        return self.__cost

# Pizza Types Subclasses
class Clasic(Pizza):
    def __init__(self, description="Classic Pizza", cost = 20):
        super().__init__(description,cost)

class Margherita(Pizza):
    def __init__(self, description = "Pizza with Margherita Cheese", cost = 20):
        super().__init__(description,cost)

class Turkish(Pizza):
    def __init__(self, description = "Turkish Style Pizza", cost = 30):
        super().__init__(description,cost)  

class Simple(Pizza):
    def __init__(self, description = "Plain Pizza", cost = 10):
        super().__init__(description,cost)  



# Sauce Types Subclasses
class Decorator(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)


class Olive(Decorator):
    def __init__(self, description  = "Olive Sauce", cost = 5):
        super().__init__(description, cost)

class Mushroom(Decorator):
    def __init__(self, description="Mushroom Sauce", cost=7):
        super().__init__(description, cost)

class GoatCheese(Decorator):
    def __init__(self, description  = "Goat Cheese Sauce", cost = 10):
        super().__init__(description, cost)

class Meat(Decorator):
    def __init__(self, description  = "Meat Sauce", cost = 15):
        super().__init__(description, cost)

class Onion(Decorator):
    def __init__(self, description  = "Onion Sauce", cost = 5):
        super().__init__(description, cost)

class Corn(Decorator):
    def __init__(self, description  = "Corn Sauce", cost = 7):
        super().__init__(description, cost)



