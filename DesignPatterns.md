**1. Factory Pattern**
Description: It creates objects separately from the system so that when a new object is created, it creates it directly without going into details

I used it in my project to create different types of pizza class based on the request

*class PizzaFactory:*
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()*


It enhances the Open/Closed principle because you can add new pizza types in the future without modifying the core code.

-------------------------------
**2. Decorator Pattern**

Adds additional functionality to the object without modifying the original object

I used it to add layers to a pizza such as olives, cheese and mushrooms without changing the basic code of the pizza

*class ToppingDecorator(Pizza):*
    def __init__(self, pizza):
        self._pizza = pizza

class Cheese(ToppingDecorator):
    def show_description(self):
        return self._pizza.show_description() + ", Cheese"
    
    def calculate_cost(self):
        return self._pizza.calculate_cost() + 1.0


It promotes the Single Responsibility principle because each layer focuses on a single behavior.
It makes it easier to add new layers without affecting the core code.
It promotes the Open/Closed principle because you can add more components (layers) without modifying the core code of the pizza.


----------------------------

**3. Singleton Pattern**

Used to check if only one object of a particular class exists in the system

I used it to ensure that there is stock of ingredients like cheese, olives and mushrooms

*class InventoryManager:*
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.ingredients = {'cheese': 10, 'olives': 10, 'mushrooms': 10}
    
    def check_ingredient(self, ingredient):
        return self.ingredients.get(ingredient, 0) > 0


It helps in managing common state across the system.

It promotes the principle of Single Responsibility as it deals with inventory management only.

It ensures that there is only one object in the system, which reduces the complexity of the system.


------------------------------
**4. Strategy Pattern**

The Strategy Pattern is used to define a specific behavior from among several interchangeable behaviors. Instead of using a big conditional statement to select a behavior, the Strategy Pattern allows you to define behaviors in separate categories and easily switch them

I used it to define a payment method where the customer chooses the payment method they prefer



*class PaymentStrategy:*
    def pay(self, amount):
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")



It promotes the Open/Closed principle because you can easily add new payment methods without modifying the core code.
It promotes the Dependency Inversion principle where the upper code depends on interfaces and not implementation details.
It allows replacing payment behavior without affecting the core code.


-----------------------------------------

**5. Overengineering Concept**
Designing a system in a way that is more complex than necessary. This happens when complex solutions are used for simple problems, which increases the complexity of the system and reduces maintainability.

I used it where I used many design patterns on a simple problem such as adding toppings to a pizza

*pizza_factory = PizzaFactory()*
*pizza = pizza_factory.create_pizza("Margherita")*
*pizza = Cheese(pizza)*
*pizza = Olives(pizza)*


Advantages of optimization:
Simplicity: In some cases, it may be better to use a simpler, more straightforward solution.
Maintenance: Complex solutions make the system difficult to maintain and understand.


************
Conclusion:

 By applying these design patterns, the system is improved in terms of flexibility, scalability, and maintainability. The patterns make the code more organized and allow for future expansion without the need to significantly modify the core code.