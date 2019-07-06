<h1><B>UNIT_TESTING<B></h1>

< This Program is all about Unit Testing  by refrering https://www.youtube.com/watch?v=6tNS--WetLI >

<h3
><B><u>PREREQUISITE :</u></B></h3>
1.Install Unittest Module if it is not installed (pip install unittest)

<h3><B><u>PROCESS :</u></h3>

1.First create a function in a file name calc.py ( "D:\Projects\unit_testing\calc.py")

2.Second create another file unit_testing in which u want to test the function. (  "D:\Projects\unit_testing\testfuction.py")

<h3><B><u>POINT TO REMEMBER :</u></h3>

1.Import Unittest module in testfuction.py file by using command.  ("import unittest")

2.Import calc.py in testfunction.py file  by using command.   ("import calc")

3.Make a class testcalc and Inherit the unittest module in it.   ("class testing_calc0(unittest.TestCase):")

<h3><B><u>FUNCTION USED :</u></h3>

1.Testcase function is present in unittest Module.So,we have to use it.

2.AssertEqual function is present in unittest Module.So,we going to be used for checking the Result.("self.assertEqual(calc.add(10,5),15)")

<h3><B><u>RUNNING METHOD :</u></h3>

if __name__=='__main__':

    unittest.main()
