import unittest
from day16 import FFT

class MyTestCase(unittest.TestCase):
    def test_FFT(self):
        setup = [1,2,3,4,5,6,7,8]
        self.assertEqual("01029498", FFT(setup, 4))


if __name__ == '__main__':
    unittest.main()
