import unittest

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(self.add(""), 0)
        self.assertEqual(self.add("8"), 8)
        self.assertEqual(self.add(" 8912 "), 8912)
        self.assertEqual(self.add("20, 30"), 50)
        self.assertEqual(self.add("20, 30, 40, 10"), 100)
        
    def add(self, numbers: str) -> int:
        if len(numbers) == 0:
            return 0
        
        number_list = numbers.split(",")
        if len(number_list) == 2:
            return int(number_list[0]) + int(number_list[1]) 
        
        return int(number_list[0])
        

if __name__ == "__main__":
    unittest.main()
    