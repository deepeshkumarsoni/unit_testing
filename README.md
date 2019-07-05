# UNIT_TESTING
< This Program is all about Unit Testing >

PROCESS :

1.First create a function in a file  "D:\Projects\unit_testing\calc.py"

2.Second create another file in which u want to test the function  "D:\Projects\unit_testing\testfuction.py"

POINT TO REMEMBER :

1. Import Unittest module in testfuction.py file by using command.  "import unittest"

2. Import calc.py in testfunction.py file  by using command.   "import calc"

3. Make a class testcalc and Inherit the unittest module in it.   "class testing_calc(unittest.TestCase):"

FUNCTION USED :

1. testcase function is used from unittest Module.

2. assertEqual function is going to be used for checking the Result."self.assertEqual(calc.add(10,5),15)"

RUNNING METHOD :

if __name__=='__main__':

    unittest.main()
