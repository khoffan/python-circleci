from number_unit import number_unit

import unittest


class Testnumber_unit(unittest.TestCase):
    def test_num_of_0_be_ord_number(self):
        number = 0
        
        result = number_unit(number)
        self.assertTrue(result)

    def test_num_of_1_be_ord_number(self):
        number = 1
        
        result = number_unit(number)
        self.assertFalse(result)

    def test_num_of_2_be_ord_number(self):
        number = 2
        
        result = number_unit(number)
        self.assertTrue(result)

    def test_num_of_3_be_ord_number(self):
        number = 3
        
        result = number_unit(number)
        self.assertFalse(result)
