#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print(f"FizzBuzz", end=" ")
        if x % 3 == 0:
            print(f"Fizz", end=" ")
        if x % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print(f"{x}", end=" ")
