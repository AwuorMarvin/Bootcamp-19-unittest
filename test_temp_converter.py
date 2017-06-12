import unittest
from converter import convert_celsius_to_farenheight

class TempConverterTest(unittest.TestCase):


    def test_celsius_is_converted_to_farenheit(self):
        actual = convert_celsius_to_farenheight(10)
        expected = 50

        self.assertEqual(actual, expected)