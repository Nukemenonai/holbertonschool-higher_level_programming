#!/usr/bin/python3
firstd = 0
lastd = 0
for i in range(0, 100):
    first = i / 10
    last = i % 10
    if first == last:
        continue
    elif first > last:
        continue
    elif i == 89:
        print(i)
    else:
        print("{:02d}".format(i), end=", ")
