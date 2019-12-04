from inputreader import aocinput
from typing import List, Tuple, Iterator
from collections import Counter


# def recursive_range(start, factor=5, total=0):
#     if factor == 0:
#         for i in range(start, 10):
#             yield total+i
#         return
#     for number in range(start, 10):
#         yield from recursive_range(number, factor-1, total+number*10**factor,)
#
#
# def numbergen2(start: str, stop: str) ->Iterator[int]:
#     """
#     Generates all numbers from start to stop where the next digit in the number always is the same or higher.
#     Alternative version using recursion instead of nested loops
#     Must always be same number of digits in start and stop
#     """
#     startnr = int(start)
#     stopnr = int(stop)
#     for number in recursive_range(int(start[0]), factor=len(start)-1):
#         if startnr <= number <= stopnr:
#             yield number


def numbergen(start: str, stop: str) ->Iterator[int]:
    """
    Generates all numbers from start to stop where the next digit in the number always is the same or higher.
    Fixed length of 6 numbers.
    """
    startnr = int(start)
    stopnr = int(stop)
    for a in range(int(start[0]), int(stop[0])):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            number = a * 10 ** 5 + b * 10 ** 4 + c * 10 ** 3 + d * 10 ** 2 + e * 10 ** 1 + f
                            if startnr <= number <= stopnr:
                                yield number


def valid_password(password: List[int]) -> bool:
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def extra_valid_password(password: List[int]) -> bool:
    numberPairs = Counter()  # count how many pairs of each number is found, if only 1 its not part of larger group
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            numberPairs[password[i]] += 1

    # if only 1 pair of a number is found it can't be connected to a larger group
    # separated pairs are also not approved since numbers must be the same or increase
    return 1 in numberPairs.values()


def password_count(data: str) -> Tuple[int,int]:
    count1 = 0
    count2 = 0
    for number in numbergen(*data.split('-')):
        passlist = [int(i) for i in str(number)]
        if valid_password(passlist):
            count1 += 1
        if extra_valid_password(passlist):
            count2 += 1
    return count1, count2


def main(day):
    data = aocinput(day)
    result = password_count(data[0])
    print(result)


if __name__ == '__main__':
    main(4)
