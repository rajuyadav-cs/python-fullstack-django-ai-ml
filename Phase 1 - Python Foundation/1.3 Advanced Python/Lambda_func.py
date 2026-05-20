# lambda_map_filter_zip.py


# ==========================================================
# LAMBDA FUNCTION
# ==========================================================

# normal function

def square(x):

    return x * x


print(square(5))


# same thing using lambda

square_lambda = lambda x: x * x

print(square_lambda(5))


# lambda with multiple arguments

add = lambda a, b: a + b

print(add(10, 20))


# lambda returning boolean

is_even = lambda x: x % 2 == 0

print(is_even(4))
print(is_even(7))


# lambda is mostly used for short temporary functions


print("\n=========================\n")


# ==========================================================
# MAP FUNCTION
# ==========================================================

# map(function, iterable)

# map applies function on every item


numbers = [1, 2, 3, 4, 5]

# square every number

result = map(lambda x: x * x, numbers)

# map object is returned
print(result)

# convert to list to see values
print(list(result))


# another example

names = ["raju", "aman", "vikram"]

# convert every name to uppercase

upper_names = map(lambda name: name.upper(), names)

print(list(upper_names))


# using normal function with map

def cube(x):

    return x ** 3


cube_result = map(cube, numbers)

print(list(cube_result))


print("\n=========================\n")


# ==========================================================
# FILTER FUNCTION
# ==========================================================

# filter(function, iterable)

# filter keeps only values where function returns True


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# keep only even numbers

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))


# keep only odd numbers

odd_numbers = filter(
    lambda x: x % 2 != 0,
    numbers
)

print(list(odd_numbers))


# filter names with length greater than 4

names = ["Raj", "Raju", "Aman", "Vikram"]

long_names = filter(
    lambda name: len(name) > 4,
    names
)

print(list(long_names))


print("\n=========================\n")


# ==========================================================
# ZIP FUNCTION
# ==========================================================

# zip combines multiple iterables index-wise


names = ["Raju", "Aman", "Vikram"]
marks = [90, 85, 95]

result = zip(names, marks)

print(result)

print(list(result))


# loop with zip

names = ["Raju", "Aman", "Vikram"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):

    print(name, mark)


# zip with 3 lists

names = ["A", "B", "C"]
marks = [80, 90, 70]
cities = ["Delhi", "Bhopal", "Mumbai"]

combined = zip(names, marks, cities)

print(list(combined))


print("\n=========================\n")


# ==========================================================
# ZIP WITH DIFFERENT LENGTHS
# ==========================================================

# zip stops at shortest iterable


a = [1, 2, 3, 4]
b = ["A", "B"]

print(list(zip(a, b)))


print("\n=========================\n")


# ==========================================================
# PRACTICAL MAP EXAMPLE
# ==========================================================

# add GST to prices


prices = [100, 200, 300]

gst_prices = map(
    lambda price: price * 1.18,
    prices
)

print(list(gst_prices))


print("\n=========================\n")


# ==========================================================
# PRACTICAL FILTER EXAMPLE
# ==========================================================

# filter passed students


marks = [25, 80, 45, 20, 90]

passed_students = filter(
    lambda mark: mark >= 33,
    marks
)

print(list(passed_students))


print("\n=========================\n")


# ==========================================================
# PRACTICAL ZIP EXAMPLE
# ==========================================================

# create student report


students = ["Raju", "Aman", "Vikram"]
marks = [90, 80, 95]

for student, mark in zip(students, marks):

    print(f"{student} scored {mark}")


print("\n=========================\n")


# ==========================================================
# MAP VS LIST COMPREHENSION
# ==========================================================


numbers = [1, 2, 3, 4]


# using map

map_result = list(
    map(lambda x: x * x, numbers)
)

print(map_result)


# using list comprehension

list_result = [x * x for x in numbers]

print(list_result)


print("\n=========================\n")


# ==========================================================
# FILTER VS LIST COMPREHENSION
# ==========================================================


numbers = [1, 2, 3, 4, 5, 6]


# using filter

filter_result = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(filter_result)


# using list comprehension

list_filter_result = [
    x for x in numbers if x % 2 == 0
]

print(list_filter_result)


print("\n=========================\n")


# ==========================================================
# SORTING WITH LAMBDA
# ==========================================================

# lambda is very commonly used in sorting


students = [
    {"name": "Raju", "marks": 90},
    {"name": "Aman", "marks": 80},
    {"name": "Vikram", "marks": 95}
]


# sort by marks

sorted_students = sorted(
    students,
    key=lambda student: student["marks"]
)

print(sorted_students)


print("\n=========================\n")


# ==========================================================
# IMPORTANT NOTES
# ==========================================================

# lambda:
# short anonymous function


# map():
# transforms data


# filter():
# selects data based on condition


# zip():
# combines iterables


# map/filter return iterator objects
# convert to list if needed


print("done")