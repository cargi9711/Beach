import unittest
from beach import Beach

class TestBeach(unittest.TestCase):
    def test_describe(self):
        b = Beach("Test Beach", "Nowhere")
        self.assertIn("Test Beach", b.describe())

if __name__ == "__main__":
    unittest.main()
