import unittest

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(self.add(""), 0)
        self.assertEqual(self.add("8"), 8)
        
    def add(self, numbers: str) -> int:
        if len(numbers) == 0:
            return 0
        return int(numbers)
        

if __name__ == "__main__":
    unittest.main()
    