# type_hints_examples.py

from typing import Optional, Union, Any


# basic variable type hints

name: str = "Raju"
age: int = 21
price: float = 99.99
is_active: bool = True

print(name)
print(age)
print(price)
print(is_active)


# python does not strictly stop wrong type at runtime
# but IDE/type checker can warn about it

wrong_name: str = 123
print(wrong_name)


# function parameter and return type hints

def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)
print(result)


# function returning string

def greet(name: str) -> str:
    return f"Hello {name}"


print(greet("Raju"))


# list type hints

numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Raju", "Aman", "Vikram"]

print(numbers)
print(names)


# dict type hints
# keys are str, values are int

marks: dict[str, int] = {
    "math": 90,
    "science": 85
}

print(marks)


# list of dictionaries
# each dictionary has string keys and string values

users: list[dict[str, str]] = [
    {"name": "Raju", "city": "Bhopal"},
    {"name": "Aman", "city": "Delhi"}
]

print(users)


# Optional means value can be given type or None
# Optional[str] means str or None

def find_user(user_id: int) -> Optional[str]:

    if user_id == 1:
        return "Raju"

    return None


user = find_user(1)
print(user)

user2 = find_user(5)
print(user2)


# Union means multiple types are allowed
# here value can be int or str

def show_id(user_id: Union[int, str]) -> None:
    print("User ID:", user_id)


show_id(101)
show_id("EMP101")


# in Python 3.10+, you can also write:
# int | str
# instead of Union[int, str]

def show_value(value: int | str) -> None:
    print("Value:", value)


show_value(10)
show_value("Hello")


# Any means any type is allowed
# use Any only when type is really unknown

def print_anything(data: Any) -> None:
    print(data)


print_anything(10)
print_anything("Python")
print_anything([1, 2, 3])
print_anything({"name": "Raju"})


# nested type hints
# list of dicts where key is str and value is int

student_marks: list[dict[str, int]] = [
    {"math": 90, "english": 80},
    {"math": 75, "english": 85}
]

print(student_marks)


# type alias
# useful when type becomes long or repeated

User = dict[str, str]

def print_user(user: User) -> None:
    print(user["name"])
    print(user["email"])


u1: User = {
    "name": "Raju",
    "email": "raju@example.com"
}

print_user(u1)


# list of custom type alias

all_users: list[User] = [
    {"name": "Raju", "email": "raju@example.com"},
    {"name": "Aman", "email": "aman@example.com"}
]

print(all_users)


# function returning list

def get_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]


print(get_numbers())


# function returning dict

def get_profile() -> dict[str, str]:
    return {
        "name": "Raju",
        "role": "Python Developer"
    }


print(get_profile())


# function returning Optional dict
# useful when data may or may not exist

def get_user_profile(user_id: int) -> Optional[dict[str, str]]:

    if user_id == 1:
        return {
            "name": "Raju",
            "city": "Bhopal"
        }

    return None


profile = get_user_profile(1)
print(profile)

profile2 = get_user_profile(99)
print(profile2)


# class with type hints

class Student:

    def __init__(self, name: str, age: int, marks: int) -> None:

        self.name: str = name
        self.age: int = age
        self.marks: int = marks

    def show_details(self) -> None:
        print(self.name)
        print(self.age)
        print(self.marks)

    def is_passed(self) -> bool:
        return self.marks >= 33


s1 = Student("Raju", 21, 90)

s1.show_details()
print(s1.is_passed())


# Union with list items
# list can contain int or str values

mixed_values: list[int | str] = [1, "two", 3, "four"]

print(mixed_values)


# Any in dictionary
# useful when values can be different types

api_response: dict[str, Any] = {
    "id": 1,
    "name": "Raju",
    "is_active": True,
    "skills": ["Python", "Django"]
}

print(api_response)


# practical example

def calculate_discount(
    price: float,
    discount: float = 0.0
) -> float:

    final_price = price - (price * discount / 100)

    return final_price


print(calculate_discount(1000, 10))
print(calculate_discount(500))


# summary:
#
# str              -> string
# int              -> integer
# float            -> decimal number
# bool             -> True/False
# list[int]        -> list of integers
# dict[str, int]   -> dictionary with str keys and int values
# Optional[str]    -> str or None
# Union[int, str]  -> int or str
# Any              -> any type