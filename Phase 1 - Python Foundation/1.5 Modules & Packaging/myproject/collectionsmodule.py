# collections_module_examples.py

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap


# Counter is used to count frequency of items

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

fruit_count = Counter(fruits)

print(fruit_count)
print(fruit_count["apple"])
print(fruit_count.most_common(2))


print("\n--------------------\n")


# Counter also works with strings

text = "hello"

letter_count = Counter(text)

print(letter_count)


print("\n--------------------\n")


# defaultdict gives default value automatically
# defaultdict(int) gives default 0

count = defaultdict(int)

count["a"] += 1
count["a"] += 1
count["b"] += 1

print(count)


print("\n--------------------\n")


# defaultdict(list) gives default empty list
# useful for grouping data

students = defaultdict(list)

students["Python"].append("Raju")
students["Python"].append("Aman")
students["Django"].append("Vikram")

print(students)


print("\n--------------------\n")


# deque is a fast double-ended queue
# append/pop from both sides is efficient

numbers = deque([1, 2, 3])

numbers.append(4)       # add at right
numbers.appendleft(0)   # add at left

print(numbers)

numbers.pop()           # remove from right
numbers.popleft()       # remove from left

print(numbers)


print("\n--------------------\n")


# deque can be used as queue

queue = deque()

queue.append("first")
queue.append("second")
queue.append("third")

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())


print("\n--------------------\n")


# namedtuple is like tuple but with named fields
# normal tuple uses indexes, namedtuple uses names

Student = namedtuple("Student", ["name", "age", "marks"])

s1 = Student("Raju", 21, 90)

print(s1)
print(s1.name)
print(s1.age)
print(s1.marks)


print("\n--------------------\n")


# OrderedDict keeps insertion order
# modern dict also keeps order, but OrderedDict is still useful in some cases

ordered_data = OrderedDict()

ordered_data["one"] = 1
ordered_data["two"] = 2
ordered_data["three"] = 3

print(ordered_data)


print("\n--------------------\n")


# ChainMap combines multiple dictionaries
# it searches from first dictionary to last

default_config = {
    "theme": "light",
    "language": "English"
}

user_config = {
    "theme": "dark"
}

config = ChainMap(user_config, default_config)

print(config["theme"])      # from user_config
print(config["language"])   # from default_config


print("\n--------------------\n")


# practical Counter example
# count words in a sentence

sentence = "python is easy and python is powerful"

words = sentence.split()

word_count = Counter(words)

print(word_count)


print("\n--------------------\n")


# practical defaultdict example
# group students by course

students_data = [
    ("Raju", "Python"),
    ("Aman", "Python"),
    ("Vikram", "Django"),
    ("Rahul", "Django"),
]

course_students = defaultdict(list)

for name, course in students_data:
    course_students[course].append(name)

print(course_students)


print("\n--------------------\n")


# practical deque example
# keep only last 3 items

recent_items = deque(maxlen=3)

recent_items.append("A")
recent_items.append("B")
recent_items.append("C")

print(recent_items)

recent_items.append("D")

# A is removed automatically because maxlen is 3

print(recent_items)


print("\n--------------------\n")


# summary:
#
# Counter      -> counts frequency
# defaultdict  -> gives default value for missing keys
# deque        -> fast queue from both sides
# namedtuple   -> tuple with named fields
# OrderedDict  -> ordered dictionary
# ChainMap     -> combines multiple dictionaries

print("done")