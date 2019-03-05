import unittest
import city_functions


class CityFunctionsTest(unittest.TestCase):

    def test_if_city_functions_contains_empty_strings(self):
        self.assertIs(city_functions.city("", "dfdflksdj"), False)
        self.assertIs(city_functions.city("dfad", ""), False)
        self.assertIs(city_functions.city("", ""), False)

    def test_if_city_functions_contains_only_char(self):
        self.assertIs(city_functions.city("324", "dfdk34 dk"), False)
        self.assertIs(city_functions.city(" 32", "1"), False)

    def test_if_city_functions_print_properly(self):
        self.assertEqual(city_functions.city("Santiago", "Chile"), "Santiago, Chile")
        self.assertEqual(city_functions.city("Miami", "USA"), "Miami, USA")

    def test_city_country_population(self):
        self.assertEqual(city_functions.city("Santiago", "Chile", 100000), "Santiago, Chile - population 100000")


if __name__ == '__main__':
    unittest.main()





