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
        sum = 0
        number_list = numbers.split(",")
        
        for number in number_list:
            sum += int(number)
            
        return sum
        

if __name__ == "__main__":
    unittest.main()
    