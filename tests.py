import unittest
from lab3 import BinaryTree

class TestLab2(unittest.TestCase):

    def test_1(self):
        self.assertEqual(node_5.find_successor(), node_7)

    def test_2(self):
        self.assertEqual(node_15.find_successor(), node_20)
                           
    def test_3(self):
        self.assertEqual(node_10.find_successor(), node_15)

    def test_4(self):
        self.assertEqual(node_20.find_successor(), None)
                



if __name__ == "__main__":
    node_10 = BinaryTree(10)
    node_5 = BinaryTree(5)
    node_15 = BinaryTree(15)
    node_3 = BinaryTree(3)
    node_7 = BinaryTree(7)
    node_20 = BinaryTree(20)

    node_10.left = node_5
    node_5.parent = node_10

    node_10.right = node_15
    node_15.parent = node_10

    node_5.left = node_3
    node_3.parent = node_5

    node_5.right = node_7
    node_7.parent = node_5

    node_15.right = node_20
    node_20.parent = node_15
    unittest.main()