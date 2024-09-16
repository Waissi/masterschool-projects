from abc import abstractmethod


class Promotion:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, price, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity):
        if quantity > 1:
            return price * (quantity - 1) + price/2


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity):
        if quantity >= 3:
            return price * (quantity - 1)


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percentage = percent

    def apply_promotion(self, price, quantity):
        discount = ((price * quantity) * self.percentage) / 100
        return price * quantity - discount
