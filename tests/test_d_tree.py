import unittest
from d_tree.decision_tree import im_here

class TestingDecisionTree(unittest.TestCase):

    def test_if_inside_correct_py_file(self):
        expected_value = "im_here"
        actual_value = im_here()
        self.assertEqual(expected_value, actual_value)


# assertEqual(a, b)         | a == b
# assertNotEqual(a, b)      | a != b
# assertTrue(x)             | bool(x) is True
# assertFalse(x)            | bool(x) is False
# assertIs(a, b)            | a is b
# assertIsNot(a, b)         | a is not b
# assertIsNone(x)           | x is None
# assertIsNotNone(x)        | x is not None
# assertIn(a, b)            | a in b
# assertNotIn(a, b)         | a not in b
# assertIsInstance(a, b)    | isinstance(a, b)
# assertNotIsInstance(a, b) | not isinstance(a, b)
