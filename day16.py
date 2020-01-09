from inputreader import aocinput
from typing import List
from itertools import accumulate


def FFT(signal: List[int], phases: int =100) -> str:
    return
    for i in range(phases):
        signal = phase(signal)
    return ''.join(map(str, signal[0:8]))


def phase(signal: List[int]):
    output = []
    length = len(signal)
    for i in range(1, length + 1):
        add = 0
        sub = 0

        counter = -1
        while counter < length:
            counter += i
            add += sum(signal[counter:counter + i])
            counter += i*2
            sub += sum(signal[counter:counter + i])
            counter += i
        output.append(abs(add - sub) % 10)

    return output


def decode(signal):
    offset = int(''.join(str(number) for number in signal[0:7]))

    if offset < len(signal)*10000 / 2:
        print('This solution method does not work')
        return

    rev_signal = list(reversed((signal*10000)[offset:]))
    for _ in range(100):
        tot = 0
        new_signal = []

        for num in rev_signal:
            tot = (tot + num) % 10
            new_signal.append(tot)
        rev_signal = new_signal

    return ''.join(map(str, reversed(rev_signal[-8:])))


def main(day):
    data = aocinput(day)
    data = [int(part) for part in data[0].strip()]
    result = FFT(data)
    result2 = decode(data)
    print(result, result2)



if __name__ == '__main__':
    main(16)
