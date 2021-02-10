import unittest

from blueprint.blueprint import Blueprint


class BlueprintTest(unittest.TestCase):
    def test_multiply_ints_signs(self):
        """
        Test that multiply_ints correctly accounts for the signs of the arguments.
        """

        result = Blueprint.multiply_ints(1, 1)
        self.assertEqual(result, 1)

        result = Blueprint.multiply_ints(-1, 1)
        self.assertEqual(result, -1)

        result = Blueprint.multiply_ints(-1, -1)
        self.assertEqual(result, 1)

        result = Blueprint.multiply_ints(0, 0)
        self.assertEqual(result, 0)

    def test_multiply_ints_types(self):
        """
        Test that multiply_ints raises TypeError if an input argument is not of type int.
        """

        int_input = int(10)

        string_input = "not_a_number"
        self.assertRaises(TypeError, Blueprint.multiply_ints, int_input, string_input)

        float_input = float(10)
        self.assertRaises(TypeError, Blueprint.multiply_ints, int_input, float_input)

        dict_input = {}
        self.assertRaises(TypeError, Blueprint.multiply_ints, int_input, dict_input)

        list_input = []
        self.assertRaises(TypeError, Blueprint.multiply_ints, int_input, list_input)
