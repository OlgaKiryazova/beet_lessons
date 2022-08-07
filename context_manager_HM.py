import unittest
import os


# Task 1
class MyOpen:

    counter = 0

    def __init__(self, file, method):
        try:
            self.file_open = open(file, method)
        except FileNotFoundError:
            raise

    def __enter__(self):
        MyOpen.counter += 1
        return self.file_open

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'closing file, number open of file is {self.counter}')
        self.file_open.close()

###############################################################################
# Task 2


class TestMyOpen(unittest.TestCase):

    def test_open_w(self):
        with MyOpen('test.txt', 'w') as file:
            file.write('test')
        self.assertTrue(os.path.exists('test.txt'))

    def test_open_r(self):
        with MyOpen('test.txt', 'r') as file:
            result = file.read()
        self.assertEqual(result, 'test')

    def test_counter(self):
        with MyOpen('test.txt', 'r'):
            ...
        with MyOpen('test.txt', 'r'):
            counter = MyOpen.counter
        self.assertEqual(counter, 2)

    def test_error_open(self):
        with self.assertRaises(FileNotFoundError):
            MyOpen('test4524245.txt', 'r')


if __name__ == '__main__':
    unittest.main()
