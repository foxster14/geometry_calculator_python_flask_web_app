import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cylinder.volume(10,32) == 10053.096491487338)

    def test_volume2(self):
        assert(cylinder.volume(10,100) == 31415.926535897932)
    
    def test_area(self):
        assert(cylinder.surfaceArea(5,4) >= 282)
    
    def test_lateral(self):
        assert(cylinder.lateral(5,4) >= 125)
    
    def test_base(self):
        assert(cylinder.base(5) >= 78)

    #failing test
    #def test_volume3(self):
        #assert(cylinder.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()
