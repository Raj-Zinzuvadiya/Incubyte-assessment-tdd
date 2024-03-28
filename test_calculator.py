import unittest

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(self.add(""), 0)
        self.assertEqual(self.add("8"), 8)
        self.assertEqual(self.add(" 8912 "), 8912)
        self.assertEqual(self.add("20, 30"), 50)
        self.assertEqual(self.add("20, 30, 40, 10"), 100)
        self.assertEqual(self.add("20 \n\n30, 50"), 100)
        with self.assertRaises(ValueError) as cm:
            self.add("20, \n")
        self.assertEqual(str(cm.exception), "Invalid Input")
        
        self.assertEqual(self.add("//;\n30;5"), 35)
        
        
    def add(self, numbers: str) -> int:
        sum = 0
        
        if len(numbers) > 0 and numbers[-1] == '\n':
            raise ValueError("Invalid Input")
        
        if numbers[:2] == "//":
            number_list = numbers[3:].split(numbers[2])
        else:
            numbers = numbers.replace("\n", ",") 
        
            number_list = numbers.split(",")
        
        for number in number_list:
            if len(number) == 0:
                continue
            
            sum += int(number)
            
        return sum
        

if __name__ == "__main__":
    unittest.main()