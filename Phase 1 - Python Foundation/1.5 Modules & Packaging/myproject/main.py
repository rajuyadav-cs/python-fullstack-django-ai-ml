from utils.math_utils import Calculator


calc = Calculator()


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


result = calc.add(x, y)

print(f"Adding {x} and {y} = {result}")