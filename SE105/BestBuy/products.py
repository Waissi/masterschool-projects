class Product:
    """
    a class for product
    """

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
        """
        Getter function for quantity.
        Returns the quantity (float).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string that represents the product, for example:
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        if quantity > self.quantity:
            raise Exception("Remaining quantity is not enough")

        self.quantity -= quantity
        if self.quantity <= 0:
            self.active = False
        return self.price * quantity
