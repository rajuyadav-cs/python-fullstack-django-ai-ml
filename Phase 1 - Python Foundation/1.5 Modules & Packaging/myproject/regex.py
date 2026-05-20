# regex_clear_examples.py

import re


# ==========================================================
# re.search(pattern, string)
# ==========================================================

# pattern = what we want to search
# string  = where we want to search

text = "My age is 21"

match = re.search(r"\d+", text)

# \d  = digit
# +   = one or more
# \d+ = one or more digits

print(match.group())   # 21


print("\n--------------------\n")


# ==========================================================
# re.findall(pattern, string)
# ==========================================================

# returns all matching values as a list

text = "Marks are 10 20 30"

numbers = re.findall(r"\d+", text)

print(numbers)   # ['10', '20', '30']


print("\n--------------------\n")


# ==========================================================
# re.sub(pattern, replacement, string)
# ==========================================================

# replaces matching pattern with replacement

text = "My phone number is 9876543210"

hidden = re.sub(r"\d", "*", text)

# every digit is replaced with *

print(hidden)


print("\n--------------------\n")


# ==========================================================
# re.split(pattern, string)
# ==========================================================

# splits string using regex pattern

text = "apple,banana;orange"

fruits = re.split(r"[,;]", text)

# [,;] means comma OR semicolon

print(fruits)


print("\n--------------------\n")


# ==========================================================
# search vs match
# ==========================================================

text = "Hello Python"

search_result = re.search(r"Python", text)
match_result = re.match(r"Python", text)

# search checks entire string
# match checks only from the beginning

print(search_result.group())   # Python
print(match_result)            # None


print("\n--------------------\n")


# ==========================================================
# character sets
# ==========================================================

text = "abc123XYZ"

lowercase = re.findall(r"[a-z]", text)
uppercase = re.findall(r"[A-Z]", text)
digits = re.findall(r"[0-9]", text)

print(lowercase)   # ['a', 'b', 'c']
print(uppercase)   # ['X', 'Y', 'Z']
print(digits)      # ['1', '2', '3']


print("\n--------------------\n")


# ==========================================================
# quantifiers
# ==========================================================

text = "a aa aaa aaaa"

one_or_more = re.findall(r"a+", text)

# a+ means one or more "a"

print(one_or_more)


text = "111 22 3333 44444"

two_digits = re.findall(r"\d{2}", text)

# \d{2} means exactly 2 digits

print(two_digits)


print("\n--------------------\n")


# ==========================================================
# extracting 10 digit phone numbers
# ==========================================================

text = """
Raju: 9876543210
Aman: 9123456780
Wrong: 12345
"""

phones = re.findall(r"\d{10}", text)

print(phones)


print("\n--------------------\n")


# ==========================================================
# grouping
# ==========================================================

date = "2026-05-20"

match = re.search(
    r"(\d{4})-(\d{2})-(\d{2})",
    date
)

# group(1) = first bracket
# group(2) = second bracket
# group(3) = third bracket

print(match.group(1))   # year
print(match.group(2))   # month
print(match.group(3))   # day


print("\n--------------------\n")


# ==========================================================
# simple email validation
# ==========================================================

email = "test@gmail.com"

pattern = r"^\w+@\w+\.\w+$"

# ^     = start of string
# \w+   = one or more word characters
# @     = @ symbol
# \.    = dot
# $     = end of string

result = re.search(pattern, email)

print(bool(result))


print("\n--------------------\n")


# ==========================================================
# replacing multiple spaces with single space
# ==========================================================

text = "Hello     my     friend"

cleaned = re.sub(r"\s+", " ", text)

# \s  = whitespace
# +   = one or more
# \s+ = one or more spaces

print(cleaned)


print("\n--------------------\n")


# ==========================================================
# removing special characters
# ==========================================================

text = "Hello@#$ Python!!! 123"

cleaned = re.sub(r"[^a-zA-Z0-9 ]", "", text)

# ^ inside [] means NOT
# this keeps only letters, numbers and spaces

print(cleaned)


print("\n--------------------\n")


# ==========================================================
# practical password validation
# ==========================================================

password = "Raju123"

has_digit = re.search(r"\d", password)
has_letter = re.search(r"[a-zA-Z]", password)

if has_digit and has_letter:
    print("Password is valid")
else:
    print("Password is invalid")


print("\n--------------------\n")


# ==========================================================
# safe search example
# ==========================================================

text = "No number here"

match = re.search(r"\d+", text)

if match:
    print(match.group())
else:
    print("No number found")


print("\n--------------------\n")


# ==========================================================
# SUMMARY
# ==========================================================

# re.search(pattern, string)
# finds first match
#
# re.findall(pattern, string)
# returns all matches as list
#
# re.sub(pattern, replacement, string)
# replaces matching values
#
# re.split(pattern, string)
# splits string using regex
#
# match.group()
# returns actual matched value

print("done")

# ==========================================================
# REGEX SYMBOLS CHEAT SHEET
# ==========================================================


# ==========================================================
# BASIC SYMBOLS
# ==========================================================

# .       -> any character except newline
# ^       -> start of string
# $       -> end of string
# *       -> zero or more repetitions
# +       -> one or more repetitions
# ?       -> zero or one repetition
# {n}     -> exactly n repetitions
# {m,n}   -> between m and n repetitions
# []      -> character set
# [^ ]    -> NOT inside character set
# |       -> OR operator
# ()      -> grouping/capturing


# ==========================================================
# SPECIAL CHARACTER CLASSES
# ==========================================================

# \d      -> digit (0-9)
# \D      -> non-digit
# \w      -> word character (a-z, A-Z, 0-9, _)
# \W      -> non-word character
# \s      -> whitespace (space, tab, newline)
# \S      -> non-whitespace


# ==========================================================
# CHARACTER SETS
# ==========================================================

# [abc]       -> match a or b or c
# [a-z]       -> lowercase letters
# [A-Z]       -> uppercase letters
# [0-9]       -> digits
# [a-zA-Z]    -> all letters
# [a-zA-Z0-9] -> letters and digits
# [^0-9]      -> anything except digits


# ==========================================================
# QUANTIFIERS
# ==========================================================

# a*      -> zero or more "a"
# a+      -> one or more "a"
# a?      -> optional "a"
# a{3}    -> exactly 3 "a"
# a{2,5}  -> between 2 and 5 "a"


# ==========================================================
# GROUPING
# ==========================================================

# ()      -> creates group
# group(1)-> first group
# group(2)-> second group

# Example:
# (\d{4})-(\d{2})-(\d{2})

# group(1) -> year
# group(2) -> month
# group(3) -> day


# ==========================================================
# ESCAPE CHARACTERS
# ==========================================================

# \.      -> actual dot
# \*      -> actual star
# \\      -> actual backslash

# because:
# . * + ? have special regex meanings


# ==========================================================
# COMMON PATTERNS
# ==========================================================

# \d+                 -> one or more digits
# \w+                 -> one or more word characters
# \s+                 -> one or more spaces
# [a-z]+              -> lowercase word
# [A-Z][a-z]+         -> capitalized word
# \d{10}              -> exactly 10 digits
# \w+@\w+\.\w+        -> simple email pattern


# ==========================================================
# START AND END
# ==========================================================

# ^hello      -> starts with "hello"
# world$      -> ends with "world"
# ^hello$     -> exactly "hello"


# ==========================================================
# OR OPERATOR
# ==========================================================

# cat|dog     -> matches "cat" OR "dog"


# ==========================================================
# EXAMPLES
# ==========================================================

# r"\d+"
# one or more digits

# r"[a-z]+"
# one or more lowercase letters

# r"\s+"
# one or more spaces

# r"^\w+$"
# string containing only word characters

# r"\d{4}"
# exactly 4 digits

# r"[^a-zA-Z0-9]"
# special characters only

# r"\w+@\w+\.\w+"
# simple email pattern


# ==========================================================
# IMPORTANT NOTES
# ==========================================================

# r"" is raw string
# always preferred in regex

# Example:
# r"\d+"

# instead of:
# "\\d+"


# ==========================================================
# MOST COMMONLY USED SYMBOLS
# ==========================================================

# \d    -> digit
# \w    -> word
# \s    -> space
# +     -> one or more
# *     -> zero or more
# ?     -> optional
# []    -> character set
# ()    -> grouping
# ^     -> start
# $     -> end