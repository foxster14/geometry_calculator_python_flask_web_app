import unittest # library for python unit testing
import sphere # When you impot python code into python code, it'll automatically run the main method which is why you see the if __name__ == '__main__' bit of code

# PyUnit is an object-oriented framework
class sphereTest(unittest.TestCase):

    def test_surfaceArea(self):
        # Seeing if expected output when 4 is given as inputmatches actual output
        assert(sphere.surfaceArea(4) == 201.06)

    def test_volume(self):
        assert(sphere.volume(4) == 268.08)

if __name__ == '__main__':
    unittest.main()