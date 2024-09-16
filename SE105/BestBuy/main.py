from products import Product
from products import NonStockedProduct
from products import LimitedProduct
from store import Store


def list_all_products(store):
    """
    print a list of the products available in the store
    """
    products = store.get_all_products()
    print('------')
    index = 0
    for product in products:
        index += 1
        print(f"{index}. ", end='')
        print(product.show())
    print('------')


def show_total_amount(store):
    """
    prints the total amount of products available in the store
    """
    quantity = store.get_total_quantity()
    print(f"Total of {quantity} items in store")


def order(store):
    """
    make an order to the store
    """
    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    products = store.get_all_products()
    while True:
        try:
            user_product = int(input("Which product # do you want? "))
            user_amount = int(input("What amount do you want? "))
        except KeyboardInterrupt:
            return
        except ValueError:
            break
        user_product -= 1
        if user_product < len(products):
            shopping_list.append((products[user_product], user_amount))
    total_price = 0
    try:
        total_price = store.order(shopping_list)
    except Exception:
        print("An error occurred during order")
    if total_price > 0:
        print(f"********\nOrder made! Total payment: ${total_price}")


def start(store):
    """
    shows the menu adn asks user for input
    """
    menu = """
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""
    user_input = 0
    while user_input != '4':
        print(menu)
        try:
            user_input = input("Please choose a number:")
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
        match user_input:
            case '1':
                list_all_products(store)
            case '2':
                show_total_amount(store)
            case '3':
                order(store)
            case '4':
                print("Goodbye")
            case _:
                print("Incorrect input")
        print()


def main():
    """
    main function
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds",
                            price=250, quantity=500),
                    Product("Google Pixel 7",
                            price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct(
                        "Shipping", price=10, quantity=250, maximum=1)
                    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
