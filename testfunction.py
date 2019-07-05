import unittest
import calc

class testing_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-5, 5),0)
        self.assertEqual(calc.add(10,-5),5)

    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(-5,5),-10)
        self.assertEqual(calc.sub(10,-5),15)

    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)
        self.assertEqual(calc.mul(-5,5),-25)
        self.assertEqual(calc.mul(0,5),0)

    def test_div(self):
        self.assertEqual(calc.div(10, 5),2)
        self.assertEqual(calc.div(10,2),5)
        self.assertEqual(calc.div(10,-5),-2)


if __name__=='__main__':
    unittest.main()

