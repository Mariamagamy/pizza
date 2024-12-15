class Pizza:
    def show_description(self):
        pass

    def calculate_cost(self):
        pass


class MargheritaPizza(Pizza):
    def show_description(self):
        return "Margherita Pizza"
    
    def calculate_cost(self):
        return 5.0

class PepperoniPizza(Pizza):
    def show_description(self):
        return "Pepperoni Pizza"
    
    def calculate_cost(self):
        return 6.0


class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()


class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

class Cheese(ToppingDecorator):
    def show_description(self):
        return self._pizza.show_description() + ", Cheese"
    
    def calculate_cost(self):
        return self._pizza.calculate_cost() + 1.0

class Olives(ToppingDecorator):
    def show_description(self):
        return self._pizza.show_description() + ", Olives"
    
    def calculate_cost(self):
        return self._pizza.calculate_cost() + 0.5

class Mushrooms(ToppingDecorator):
    def show_description(self):
        return self._pizza.show_description() + ", Mushrooms"
    
    def calculate_cost(self):
        return self._pizza.calculate_cost() + 0.7

class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.ingredients = {'cheese': 10, 'olives': 10, 'mushrooms': 10}
    
    def check_ingredient(self, ingredient):
        return self.ingredients.get(ingredient, 0) > 0


class PaymentStrategy:
    def pay(self, amount):
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


#Factory Pattern
pizza_factory = PizzaFactory()
pizza = pizza_factory.create_pizza("Margherita")

# Decorator Pattern
pizza = Cheese(pizza)
pizza = Olives(pizza)

#حساب التكلفة والعرض 
print(f"Pizza Description: {pizza.show_description()}")
print(f"Total Cost: ${pizza.calculate_cost()}")

# Strategy Pattern
payment_method = CreditCardPayment()
payment_method.pay(pizza.calculate_cost())
