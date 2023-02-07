import unittest

from blueprint.blueprint import Blueprint


class BlueprintTest(unittest.TestCase):
    def test_multiply_numbers_signs(self):
        """
        Test that multiply_numbers correctly accounts for the signs of the arguments.
        """

        result = Blueprint.multiply_numbers(1, 1)
        self.assertEqual(result, float(1))

        result = Blueprint.multiply_numbers(-1, 1)
        self.assertEqual(result, float(-1))

        result = Blueprint.multiply_numbers(-1, -1)
        self.assertEqual(result, float(1))

        result = Blueprint.multiply_numbers(0, 0)
        self.assertEqual(result, float(0))

    def test_multiply_numbers_types(self):
        """
        Test that multiply_numbers raises TypeError if an input argument is not of type int or float.
        """

        int_input = int(1)
        float_input = float(1)

        string_input = "not_a_number"
        self.assertRaises(TypeError, Blueprint.multiply_numbers, int_input, string_input)
        self.assertRaises(TypeError, Blueprint.multiply_numbers, float_input, string_input)

        dict_input = {}
        self.assertRaises(TypeError, Blueprint.multiply_numbers, int_input, dict_input)
        self.assertRaises(TypeError, Blueprint.multiply_numbers, float_input, dict_input)

        list_input = []
        self.assertRaises(TypeError, Blueprint.multiply_numbers, int_input, list_input)
        self.assertRaises(TypeError, Blueprint.multiply_numbers, float_input, list_input)
