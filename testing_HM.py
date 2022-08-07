import unittest

from descriptors_HM import Email
import home_work_classes
from to_test import ColorSpecification, SizeSpecification, ProductFilter, \
    Product, Color, Size, AndSpecification

from unittest.mock import patch


class TestEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_email = 'abc-d@mail.com'
        self.invalid_email = 'abc-@mail.com'

    def test_valid_email(self):
        result = Email.validate(self.valid_email)
        self.assertEqual(result, f"{self.valid_email} is valid")

    def test_invalid_email(self):
        result = Email.validate(self.invalid_email)
        self.assertEqual(result, f"{self.invalid_email} is invalid")

    @patch('builtins.print')
    def test_valid_email(self, mock_print):
        mock_print.return_value = 'abc-d@mail.com is valid'
        result = Email.validate(self.valid_email)
        self.assertEqual(result, f"{self.valid_email} is valid")

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            Email.validate(1111111)

################################################################


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

#######################################################################


class TestProductFilter(unittest.TestCase):

    def setUp(self) -> None:
        apple = Product('apple', Color.GREEN, Size.SMALL)
        tree = Product('tree', Color.GREEN, Size.LARGE)
        house = Product('house', Color.BLUE, Size.LARGE)

        self.products = [apple, tree, house]
        self.product_filter = ProductFilter()

    def test_filter_color(self):
        green = ColorSpecification(Color.GREEN)
        for product in self.product_filter.filter(self.products, green):
            self.assertEqual(product.color, Color.GREEN)

    def test_filter_large(self):
        large = SizeSpecification(Size.LARGE)
        for product in self.product_filter.filter(self.products, large):
            self.assertEqual(product.size, Size.LARGE)

    def test_filter_size_and_color(self):
        large_blue = AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
        for product in self.product_filter.filter(self.products, large_blue):
            self.assertEqual(product.size, Size.LARGE)
            self.assertEqual(product.color, Color.BLUE)




if __name__ == '__main__':
    unittest.main()
