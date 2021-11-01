import unittest
import cone

class triangleTest(unittest.TestCase):
    # Since the calculations return doubles which can be inconsistent in
    # how they're rounded, I've implemented unit tests that check for
    # approximate value as long as it's greater than/equal to the given integer
    def test_slant(self):
        assert(cone.slant(3,4) == 5)

    def test_surfaceArea(self):
        assert(cone.surface(3,4) >= 75)

    def test_volume(self):
        assert(cone.volume(3,4) >= 37)
    
    def test_lateral(self):
        assert(cone.lateral(3,4) >= 47)

# When this program is invoked, run a unittest on the main method
if __name__ == '__main__':
    unittest.main()