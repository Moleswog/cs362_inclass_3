import unittest
import calculator

class calcTest(unittest.TestCase):
    def test_add(self):
        res = calculator.add(1, 4)
        self.assertEqual(res, 5)
        
        res = calculator.add(4, -2)
        self.assertEqual(res, 2)

        res = calculator.add(3.2, 2.2)
        self.assertEqual(res, 5.4)
        
    def test_sub(self):
        res = calculator.sub(2, 2)
        self.assertEqual(res, 0)
        
        res = calculator.sub(6.2, 2.1)
        self.assertEqual(res, 4.1)
        
        res = calculator.sub(-3.2, 1.4)
        self.assertEqual(res, -4.6)

    def test_mul(self):
        res = calculator.mul(3, 4)
        self.assertEqual(res, 12)
        
        res = calculator.mul(-3, 4)
        self.assertEqual(res, -12)

        res = calculator.mul(3.1, 2.5)
        self.assertEqual(res, 7.75)

    def test_div(self):
        res = calculator.div(6, 3)
        self.assertEqual(res, 2)
        
        res = calculator.div(6, 0)
        self.assertIsNone(res, 0)

        res = calculator.div(6.3, 2.1)
        self.assertEqual(res, 3)

if __name__ == "__main__":
    unittest.main()
    
