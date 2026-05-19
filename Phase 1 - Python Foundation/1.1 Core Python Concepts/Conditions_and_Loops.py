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

# for loop
# It has fixed number of iterations
a = [10,20,30,40,50]

for i in a:
    print(i)
count = 2
for i in range(1,11):
    print(f"{count}x{i} = {count * i}")

dic = {'item':20, 'orange': 'fruit','fruits' : ['apple','banana','grapes']}

for key , value in dic.items():
    print(f"Key :{key}, Value : {value}")

print(dic['fruits'][1])    

# While loop
# it has condition based iterations can be infinite
count = 10
while count > 0:

    print("Hello world")
    count -= 1

# break statement

magicnum = 10
#searching magic number only

i = 1

while True:
    if i == magicnum:
        print("Found it!")
        break 
    else:
        i += 1

# Continue

# Skipping odd numbers

num =50
i = 1
while i <= 50:
    if i % 2 != 0:
        i += 1
        continue
    else:
        print(i, end=" ")

    i += 1    


# Comprehensions

numbers = [x for x in range(1,101)]
print("\n" , numbers)
Evennumbers = [x for x in range(1, 101) if x % 2 == 0]
dualloop = [(x, y) for x in range(1,11) for y in range(1,6) if x == y]

print(f"{Evennumbers}\n {dualloop}")