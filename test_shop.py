import unittest

from shop import Product, ProductStore, CartProducts


class TestProductStore(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Product('potato', 8)
        self.store = ProductStore()

    def test_add_product_to_stock(self):
        self.store.add_product(self.p, 10)
        result = self.p.amount
        self.assertEqual(result, 10)

    def test_add_product_to_stock2(self):
        self.store.add_product(self.p, 10)
        self.store.add_product(self.p, 30)
        result = self.p.amount
        self.assertEqual(result, 40)


class TestCartProductsAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Product('potato', 8)
        self.store = ProductStore()
        self.store.add_product(self.p, 300)
        self.my_cart = CartProducts()

    def test_add_to_cart_success(self):
        self.my_cart.add_to_cart(4, self.p)
        for prod in self.my_cart.cart:
            result = prod['amount']
            self.assertEqual(result, 4)

    def test_add_to_cart_more_number(self):
        self.my_cart.add_to_cart(400, self.p)
        for prod in self.my_cart.cart:
            result = prod['amount']
            self.assertEqual(result, 300)

    def test_add_to_cart_empty(self):
        p2 = Product('banana', 40)
        self.my_cart.add_to_cart(5000, p2)
        result = self.my_cart.cart
        self.assertEqual(result, [])

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            self.my_cart.add_to_cart('1', self.p)


class TestCartProductsOther(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Product('potato', 20)
        self.store = ProductStore()
        self.store.add_product(self.p, 300)
        self.my_cart = CartProducts()
        self.my_cart.add_to_cart(10, self.p)

    def test_correct_cart(self):
        self.my_cart.correct_cart(self.p, 5)
        for prod in self.my_cart.cart:
            result = prod['amount']
            self.assertEqual(result, 5)

    def test_check(self):
        p2 = Product('banana', 40)
        self.store.add_product(p2, 300)
        self.my_cart.add_to_cart(10, p2)
        total_costs = self.my_cart.check()
        self.assertEqual(total_costs, 720)


if __name__ == '__main__':
    unittest.main()
