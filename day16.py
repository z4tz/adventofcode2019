from inputreader import aocinput
from typing import List
from itertools import cycle

base = [0, 1, 0, -1]


def patternGen(n):
    return cycle([num for num in base for _ in range(n)])


def FFT(signal, phases=100):
    for i in range(phases):
        signal = phase2(signal)
    return ''.join(map(str, signal[0:8]))


def phase(signal: List[int]):
    output = []
    for i in range(1, len(signal) + 1):
        gen = patternGen(i)
        next(gen)  # throw away first value
        result = abs(sum([next(gen) * value for value in signal])) % 10
        output.append(result)
    return output


def phase2(signal):
    output = []
    length = len(signal)
    for i in range(1, length + 1):
        print(i)
        add = 0
        sub = 0

        counter = -1
        try:
            while counter < length:
                counter += i
                add += sum(signal[counter:counter + i])
                counter += i*2
                sub += sum(signal[counter:counter + i])
                counter += i

        except IndexError:
            pass
        output.append(abs(add - sub) % 10)

    return output


def decode(signal):
    signal = signal*10000
    print(FFT(signal), 1)


def main(day):
    data = aocinput(day)
    data = [int(part) for part in data[0].strip()]
    #result = FFT(data)
    result2 = decode(data)
    #print(result)


if __name__ == '__main__':
    main(16)
