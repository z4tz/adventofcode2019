from inputreader import aocinput
from typing import List


def valid_password(password: List[int]) -> bool:
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
    return bool(sum([password[i] == password[i+1] for i in range(len(password) - 1)]))


def digitcount(digits: List[int]) -> int:
    return len(set(digits))


def extra_valid_password(password: List[int]) -> bool:
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False

        if password[i] == password[i+1]:
            if i == 0:
                group = password[i:i+3]
            elif i == len(password) - 2:
                group = password[i-1:i+2]
            else:
                group = password[i-1:i+3]

            if digitcount(group) > 1:
                print(password, group, digitcount(group))
                return True
    return False





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
