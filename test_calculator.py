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
        
        with self.assertRaisesRegex(ValueError, "negative numbers not allowed .*") as cm:
            self.add("//;\n-30;-5")
        
        
    def add(self, numbers: str) -> int:
        sum = 0
        
        if len(numbers) > 0 and numbers[-1] == '\n':
            raise ValueError("Invalid Input")
        
        neg_value_list = []
        
        if numbers[:2] == "//":
            number_list = numbers[3:].split(numbers[2])
        else:
            numbers = numbers.replace("\n", ",") 
        
            number_list = numbers.split(",")
        
        for number in number_list:
            if len(number) == 0:
                continue
            num = int(number)
            
            if num < 0:
                neg_value_list.append(str(num))
                continue
            
            sum += num
            
        if len(neg_value_list) != 0:
            neg_list = ', '.join(neg_value_list) 
            raise ValueError(f"negative numbers not allowed {neg_list}")
        return sum
        

if __name__ == "__main__":
    unittest.main()