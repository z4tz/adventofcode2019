from inputreader import aocinput
from typing import List, Tuple
from collections import Counter
import numpy as np
from numpy import ndarray


def split_to_layers(data: List[int], width, height) -> List[List[int]]:
    length = width * height
    return [data[i:i+length] for i in range(0, len(data), length)]


def corruption_check(layers: [List[List[int]]]) -> int:
    least_zeros = min([Counter(layer) for layer in layers], key=lambda x: x[0])
    return least_zeros[1] * least_zeros[2]


def decode_image(data: str, width=25, height=6) -> Tuple[int, ndarray]:
    np.set_printoptions(linewidth=width * 4+3)  # make sure whole image is printed
    layers = split_to_layers([int(char) for char in data], width, height)
    corrupt = corruption_check(layers)
    arr = np.empty((height, width), dtype=str)

    def get_pixel(position):
        for layer in layers:
            if layer[position] != 2:
                return '#' if layer[position] == 1 else ' '

    for y in range(height):
        for x in range(width):
            pos = y*width + x  # position in the linear layers
            arr[y, x] = get_pixel(pos)
    return corrupt, arr


def main(day):
    data = aocinput(day)
    result = decode_image(data[0])
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    main(8)
