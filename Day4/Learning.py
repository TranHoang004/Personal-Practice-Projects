
## Output: True or False based on the input year
# def is_leap(year):
#     leap = False
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap = True
#     return leap

###############################################################

# Output: ex: n=5
# 12345

# year = int(input())
# print(is_leap(year))
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i+1, end='')
#     print()

###############################################################
# Output:OrderedDict price of each item
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    items = OrderedDict()
    for _ in range(n):
        line = input().rstrip()
        *name_parts, price = line.split()
        name = ' '.join(name_parts)
        price = int(price)
        if name in items:
            items[name] += price
        else:
            items[name] = price
    for name, total in items.items():
        print(f"{name} {total}")