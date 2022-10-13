import unittest
from Triangle import classifyTriangle 

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testrighttrianglea(self):
        """
        Testcase for right triangle a
        """
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testrighttriangleb(self):
        """
        Testcase for right triangle b
        """
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testequilateraltriangles(self):
        """
        Testcase for equilateral triangles
        """
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testinvalidinput(self):
        """
        Testcase for invalid input
        """
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 should not be a Invalid input')

    def testdecimalsides(self):
        """
        Testcase for decimal sides
        """
        self.assertEqual(classifyTriangle(3.0,4.0,5.0),"InvalidInput",'3.0,4.0,5.0 is a Invalid Input')

    def testnegativeinput(self):
        """
        Testcase for negative input
        """
        self.assertEqual(classifyTriangle(-2,5,10),"InvalidInput","-2,5,10 is a Invalid Input")

    def testnotatriangle(self):
        """
        Testcase for not a triangle
        """
        self.assertEqual(classifyTriangle(5,2,10),"NotATriangle","5,2,10 is not a triangle")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
