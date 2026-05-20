'''
Generators
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

'''

# A simple generator function:

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#Using next() with Generators
# You can manually iterate through a generator using the next() function:

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# When there are no more values to yield, the generator raises a StopIteration exception:

def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) # This will raise StopIteration

'''
Generators can be used to create the Fibonacci sequence.

It can continue generating values indefinitely, without running out of memory:
'''

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

'''
Generator Methods
Generators have special methods for advanced control:

send() Method
The send() method allows you to send a value to the generator:
'''

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# close() Method
# The close() method stops the generator:

# Example
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()