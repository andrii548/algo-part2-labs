import unittest
from avl_priority_queue import AVLPriorityQueue

class TestPriorityQueueAVL(unittest.TestCase):
    
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_empty_queue(self):
        self.assertEqual(self.pq.view_queue(), [])
        self.assertIsNone(self.pq.dequeue())

    def test_insert_and_view_all(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 100)
        self.pq.insert("Середній", 50)
        
        expected_order = [
            ("Високий", 100),
            ("Середній", 50),
            ("Низький", 1)
        ]
        self.assertEqual(self.pq.view_queue(), expected_order)

    def test_extract_max(self):
        self.pq.insert("Завдання 1", 10)
        self.pq.insert("Завдання 2", 20)
        self.pq.insert("Завдання 3", 5)

        extracted = self.pq.dequeue()
        self.assertEqual(extracted, ("Завдання 2", 20))
        
        expected_remaining = [("Завдання 1", 10), ("Завдання 3", 5)]
        self.assertEqual(self.pq.view_queue(), expected_remaining)

    def test_duplicate_priorities(self):
        self.pq.insert("А", 10)
        self.pq.insert("Б", 10)
        self.pq.insert("В", 10)
        result = self.pq.view_queue()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], 10)
        self.assertEqual(result[1][1], 10)
        self.assertEqual(result[2][1], 10)

    def test_avl_balancing(self):
        for i in range(1, 101):
            self.pq.insert(f"Завдання {i}", i)
        self.assertEqual(self.pq.dequeue(), ("Завдання 100", 100))
        self.assertEqual(self.pq.dequeue(), ("Завдання 99", 99))


if __name__ == '__main__':
    unittest.main()