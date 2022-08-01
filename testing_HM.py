import unittest

from descriptors_HM import Email
import home_work_classes
import to_test

class TestEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_email = 'abc-d@mail.com'
        self.invalid_email = 'abc-@mail.com'

    def test_valid_email(self):
        result = Email.validate(self.valid_email)
        self.assertEqual(result, print(f"{self.valid_email} is valid"))

    def test_invalid_email(self):
        result = Email.validate(self.invalid_email)
        self.assertEqual(result, print(f"{self.invalid_email} is invalid"))

    # проверочный результат не полный, но тест прошел успешно, почему?
    # def test_invalid_email(self):
    #     result = Email.validate(self.invalid_email)
    #     self.assertEqual(result, print(f"{self.invalid_email} "))

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            Email.validate(1111111)



class TestTVController(unittest.TestCase):

    channels = ["BBC", "Discovery", "TV1000"]

    def test_first_channel(self):
        result = home_work_classes.TVController(self.channels).first_channel()
        self.assertEqual(result, "BBC")

    def test_last_channel(self):
        result = home_work_classes.TVController(self.channels).last_channel()
        self.assertEqual(result, "TV1000")

    def test_turn_channel(self):
        result = home_work_classes.TVController(self.channels).turn_channel(3)
        self.assertEqual(result, "TV1000")

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            home_work_classes.TVController(self.channels).turn_channel('bbbkb')

    def test_next_channel(self):
        result = home_work_classes.TVController(self.channels).next_channel()
        self.assertEqual(result, "Discovery")

    def test_previous_channel(self):
        result = home_work_classes.TVController(self.channels).previous_channel()
        self.assertEqual(result, "TV1000")

    def test_current_channel(self):
        result = home_work_classes.TVController(self.channels).current_channel()
        self.assertEqual(result, "BBC")

    def test_is_exist(self):
        result = home_work_classes.TVController(self.channels).is_exist("BBC")
        self.assertEqual(result, print('yes BBC'))


#######################################################################

class TestProductFilter(unittest.TestCase):


    def setUp(self) -> None:
        apple = to_test.Product('apple', to_test.Color.GREEN, to_test.Size.SMALL)
        tree = to_test.Product('tree', to_test.Color.GREEN, to_test.Size.LARGE)
        house = to_test.Product('house', to_test.Color.BLUE, to_test.Size.LARGE)

        self.products = [apple, tree, house]
        self.product_filter = to_test.ProductFilter()

    def test_filter_color(self):
        green = to_test.ColorSpecification(to_test.Color.GREEN)
        for product in self.product_filter.filter(self.products, green):
            result = f'{product.name} is GREEN'

        self.assertEqual(result, "apple is GREEN" and "tree is GREEN")

    def test_filter_large(self):
        large = to_test.SizeSpecification(to_test.Size.LARGE)
        for product in self.product_filter.filter(self.products, large):
            result = f'{product.name} is LARGE'

        self.assertEqual(result, "apple??? is LARGE" and "house is LARGE")
        # product.name указан не правильно, но тест прошел успешно?



if __name__ == '__main__':
    unittest.main()
