import unittest
import bqhus


class TestSelect(unittest.TestCase):
    def test_select_with_no_params(self):
        query = "SELECT 1"
        task = bqhus.select(None, query)
        self.assertEqual(query, task.query)


if __name__ == "__main__":
    unittest.main()
