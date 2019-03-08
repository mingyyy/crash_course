import chap11_03
import unittest


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        self.new_employee = chap11_03.Employee("Michael", "Jordan", 100000)

    def tearDown(self):
        pass

    def test_give_default_raise(self):
        """Test method give_raise() without passing anything would give me the right raise."""
        self.assertEqual(self.new_employee.give_raise(), 105000)

    def test_give_custom_raise(self):
        self.assertEqual(self.new_employee.give_raise(100000), 200000)


if __name__ == '__main__':
    unittest.main()

