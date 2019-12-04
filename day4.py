from inputreader import aocinput
from typing import List
from collections import Counter


def valid_password(password: List[int]) -> bool:
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
    return bool(sum([password[i] == password[i+1] for i in range(len(password) - 1)]))


def extra_valid_password(password: List[int]) -> bool:
    numberPairs = Counter()  # count how many pairs of each number is found, if only 1 its not part of larger group
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
        if password[i] == password[i+1]:
            numberPairs[password[i]] += 1
    return 1 in numberPairs.values()


def password_count(data: str) -> int:
    count1 = 0
    count2 = 0
    for number in range(*map(int, data.split('-'))):
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
