import timeit
import os


def setupstring(day):
    return f"""
from day{day} import main"""


def time_day(day, runs=1):
    print("-----## Assignment day {0} ##-----".format(day))
    time = timeit.timeit(f"main({day})", setup=setupstring(day), number=runs) / runs
    print(f"Time used for assignment {day}: {time}s\n\n")


def main():
    days = range(1, len(os.listdir('inputs/')) + 1)
    runs = 1

    for day in days:
        time_day(day, runs)


if __name__ == '__main__':
    main()
