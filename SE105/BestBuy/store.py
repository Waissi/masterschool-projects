class Store:
    """
    a class for the store
    """

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """
        Adds a product from store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from store.
        """
        del self.product_list[product]

    def get_total_quantity(self):
        """
        Returns how many items are in the store in total.
        """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        """
        Returns all products in the store that are active.
        """
        products = []
        for product in self.product_list:
            if product.is_active():
                products.append(product)

        return products

    def order(shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product in shopping_list:
            total_price += product[0].buy(product[1])

        return total_price
