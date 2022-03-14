import unittest
from d_tree.decision_tree import im_here

class TestingDecisionTree(unittest.TestCase):

    def test_if_inside_correct_py_file(self):
        expected_value = "im_here"
        actual_value = im_here()
        self.assertEqual(expected_value, actual_value)
