#!/usr/bin/env python3

def is_year_leapyear(year: int) -> bool:
    return (((year % 4 ==0) and (year % 100 !=0)) or (year % 400 == 0 ))


def main():
    year = 2009
    if (is_year_leapyear(year)):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()