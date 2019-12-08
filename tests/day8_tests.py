import unittest
import numpy as np
from day8 import split_to_layers, corruption_check, decode_image


class MyTestCase(unittest.TestCase):
    def test_splitter(self):
        data = [1,2,3,4,5,6,7,8,9,0,1,2]
        layers = split_to_layers(data, 3, 2)
        self.assertEqual(2, len(layers))
        self.assertEqual(6, len(layers[0]))

    def test_imagedecoder(self):
        data = '0222112222120000'
        expected = np.array(list(' ## ')).reshape((2, 2))
        self.assertEqual(True, (expected == decode_image(data, 2, 2)[1]).all())  # comparing numpy arrays


if __name__ == '__main__':
    unittest.main()
