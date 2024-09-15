class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise Exception("A valid name shold be given")
        self.name = name

        if price <= 0:
            raise Exception("Price should be above zero")
        self.price = price

        if quantity <= 0:
            raise Exception("Quantity should be above zero")
        self.quantity = quantity

        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise Exception("Remaining quantity is not enough")

        self.quantity -= quantity
        return self.price * quantity
