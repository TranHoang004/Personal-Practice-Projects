x= 10
y= 20
def add_numbers(a, b):
    return a + b
print("The sum of", x, "and", y, "is:", add_numbers(x, y))
def multiply_numbers(a, b):
    return a * b
print("The product of", x, "and", y, "is:", multiply_numbers(x, y))

def calculate_area_of_circle(radius):
    return 3.14 * (radius ** 2)
print("The area of a circle with radius", x, "is:", calculate_area_of_circle(x))
print("The area of a circle with radius", y, "is:", calculate_area_of_circle(y))

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)
print("The perimeter of a rectangle with length", x, "and width", y, "is:", calculate_perimeter_of_rectangle(x, y))

def calculate_area_of_rectangle(length, width):
    return length * width   
print("The area of a rectangle with length", x, "and width", y, "is:", calculate_area_of_rectangle(x, y))

def calculate_square(a):
    return a ** 2
print("The square of", x, "is:", calculate_square(x))
print("The square of", y, "is:", calculate_square(y))

ageOfPerson = [25, 30, 35, 40, 45]
def sort_ages(ages):
    return sorted(ages)
print("Sorted ages:", sort_ages(ageOfPerson))
def find_max_age(ages):
    return max(ages)
print("Maximum age:", find_max_age(ageOfPerson))
def find_min_age(ages):
    return min(ages)
print("Minimum age:", find_min_age(ageOfPerson))

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_and_even_numbers(numbers):
    local_even = []
    local_odd = []
    for num in numbers:
        if num % 2 == 0:
            local_even.append(num)
        else:
            local_odd.append(num)
    return local_even, local_odd
even_numbers_result, odd_numbers_result = odd_and_even_numbers(i)

print("The Even numbers is:", even_numbers_result)
print("The Odd numbers is:", odd_numbers_result)