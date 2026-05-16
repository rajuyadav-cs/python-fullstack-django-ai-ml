number = 1
\
# If
if number:
    print("True")

# If-else
if number > 1:
    print("True")

else:
    print("False")


# if-elif-else

if number > 1:
    print("Truen")
elif number == 1:
    print("Equal")
else:
    print("False")

# Nested if
age = 20
if number > age:
    print("first if")
    if number < age:
        print("Second if")

# Ternary Operator

age = 20

result = 'Adult' if age >= 18 else 'Minor'
print(result)


