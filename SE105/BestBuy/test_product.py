from products import Product


def test_creating_product_works():
    product_test = Product("BOOP", 10, 10)
    assert (product_test.show() == "BOOP, Price: 10, Quantity: 10")


def test_raise_exception_when_creating_product_with_wrong_parameters():
    exception_raised = False
    try:
        Product()
    except Exception:
        exception_raised = True
    assert (exception_raised == True)


def test_product_becomes_inactive():
    test_product = Product("BOOP", 10, 10)
    test_product.buy(10)
    assert (test_product.is_active() == False)


def test_quantity_after_buying_object():
    test_product = Product("BOOP", 10, 10)
    test_product.buy(5)
    assert (test_product.get_quantity() == 5)


def test_raise_exception_when_buying_larger_quantity():
    test_product = Product("BOOP", 10, 5)
    exception_raised = False
    try:
        test_product.buy(10)
    except Exception:
        exception_raised = True
    assert (exception_raised == True)
