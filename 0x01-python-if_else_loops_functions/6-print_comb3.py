#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        number = tens * 10 + ones
        print("{:02d}".format(number), end=", " if number < 89 else "\n")
