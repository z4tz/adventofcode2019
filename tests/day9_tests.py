import unittest
from day9 import BOOST


class MyTestCase(unittest.TestCase):

    def test_203(self):
        code = [109, 5, 203, 3, 99]
        boost = BOOST(code, 5)
        boost.run()
        print(boost.intcode)

    def test_selfreplicate(self):
        code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        boost = BOOST(code)
        boost.run()
        self.assertEqual(code, boost.log)

    def test_16digit(self):
        code = [1102,34915192,34915192,7,4,7,99,0]
        boost = BOOST(code)
        boost.run()
        self.assertEqual(16, len(str(boost.log[-1])))

    def test_large_number_in_middle(self):
        code = [104,1125899906842624,99]
        boost = BOOST(code)
        boost.run()
        print(boost.log)
        print(boost.intcode)
        self.assertEqual(1125899906842624, boost.log[-1])


if __name__ == '__main__':
    unittest.main()
