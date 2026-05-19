# =========================================================
# PYTHON FILE I/O - COMPLETE GUIDE
# =========================================================
#
# This file explains:
#
# 1. open()
# 2. read()
# 3. readline()
# 4. readlines()
# 5. write()
# 6. append mode
# 7. create mode
# 8. file cursor
# 9. seek()
# 10. tell()
# 11. context manager (with)
# 12. binary files
# 13. exception handling with files
#
# =========================================================


# =========================================================
# WHAT IS FILE I/O?
# =========================================================
#
# I/O = Input / Output
#
# Input:
#     Reading data from a file
#
# Output:
#     Writing data into a file
#
# =========================================================


# =========================================================
# 1. OPENING A FILE
# =========================================================
#
# Syntax:
#
# open(filename, mode)
#
# =========================================================

print("\n--- Example 1: Opening a File ---")

# Open file in write mode
file = open("sample.txt", "w")

# Write data
file.write("Hello Python")

# Close file
file.close()

print("File created and data written")


# =========================================================
# FILE MODES
# =========================================================
#
# "r"  -> Read mode
# "w"  -> Write mode
# "a"  -> Append mode
# "x"  -> Create new file
# "rb" -> Read binary
# "wb" -> Write binary
#
# =========================================================


# =========================================================
# 2. READ MODE
# =========================================================
#
# read() reads the complete file content
#
# =========================================================

print("\n--- Example 2: Reading File ---")

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# =========================================================
# 3. read(size)
# =========================================================
#
# Reads only specific number of characters
#
# =========================================================

print("\n--- Example 3: Reading Specific Characters ---")

file = open("sample.txt", "r")

data = file.read(5)

print(data)

file.close()


# =========================================================
# 4. readline()
# =========================================================
#
# Reads one line at a time
#
# =========================================================

print("\n--- Example 4: readline() ---")

# Create file with multiple lines
file = open("sample.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

file.close()

# Read line by line
file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()


# =========================================================
# 5. readlines()
# =========================================================
#
# Returns all lines as a list
#
# =========================================================

print("\n--- Example 5: readlines() ---")

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# =========================================================
# 6. WRITE MODE
# =========================================================
#
# "w" mode overwrites old content
#
# =========================================================

print("\n--- Example 6: Write Mode ---")

file = open("sample.txt", "w")

file.write("New Content")

file.close()

print("Old content replaced")


# =========================================================
# 7. APPEND MODE
# =========================================================
#
# "a" mode adds new data at the end
# without deleting old data
#
# =========================================================

print("\n--- Example 7: Append Mode ---")

file = open("sample.txt", "a")

file.write("\nAppended Line")

file.close()

print("New data appended")


# =========================================================
# 8. CREATE MODE
# =========================================================
#
# "x" creates a new file
#
# Error occurs if file already exists
#
# =========================================================

print("\n--- Example 8: Create Mode ---")

try:

    file = open("newfile.txt", "x")

    print("New file created")

    file.close()

except FileExistsError:

    print("File already exists")


# =========================================================
# 9. FILE CURSOR
# =========================================================
#
# Python maintains a cursor position
#
# Cursor moves after reading data
#
# =========================================================

print("\n--- Example 9: File Cursor ---")

file = open("sample.txt", "r")

print(file.read(5))

print(file.read(5))

file.close()


# =========================================================
# 10. seek()
# =========================================================
#
# seek(position)
#
# Moves cursor to specific position
#
# =========================================================

print("\n--- Example 10: seek() ---")

file = open("sample.txt", "r")

print(file.read(5))

# Move cursor back to start
file.seek(0)

print(file.read(5))

file.close()


# =========================================================
# 11. tell()
# =========================================================
#
# tell() returns current cursor position
#
# =========================================================

print("\n--- Example 11: tell() ---")

file = open("sample.txt", "r")

print("Initial Position:", file.tell())

file.read(5)

print("After Reading 5 Characters:", file.tell())

file.close()


# =========================================================
# 12. CONTEXT MANAGER (with)
# =========================================================
#
# BEST PRACTICE
#
# Automatically closes file
#
# =========================================================

print("\n--- Example 12: with Statement ---")

with open("sample.txt", "r") as file:

    content = file.read()

    print(content)

# File automatically closed here


# =========================================================
# WHY 'with' IS IMPORTANT
# =========================================================
#
# Without with:
#
# file = open(...)
# file.close()
#
# If error occurs before close():
# file may remain open
#
#
# With with:
#
# Automatic cleanup
#
# =========================================================


# =========================================================
# 13. WRITING WITH 'with'
# =========================================================

print("\n--- Example 13: Writing with with ---")

with open("sample2.txt", "w") as file:

    file.write("Python File Handling")

print("Data written safely")


# =========================================================
# 14. LOOPING THROUGH FILE
# =========================================================

print("\n--- Example 14: Loop Through File ---")

with open("sample.txt", "r") as file:

    for line in file:

        print(line.strip())

# strip() removes extra newline spaces


# =========================================================
# 15. EXCEPTION HANDLING WITH FILES
# =========================================================

print("\n--- Example 15: File Exception Handling ---")

try:

    with open("unknown.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File does not exist")


# =========================================================
# 16. BINARY FILES
# =========================================================
#
# Used for:
# - Images
# - Videos
# - Audio
#
# =========================================================

print("\n--- Example 16: Binary Files ---")

# Read binary file
# file = open("image.jpg", "rb")

# Write binary file
# file = open("copy.jpg", "wb")

print("Binary mode example shown")


# =========================================================
# 17. COPYING FILE CONTENT
# =========================================================

print("\n--- Example 17: Copy File Content ---")

with open("sample.txt", "r") as source:

    data = source.read()

with open("copy.txt", "w") as target:

    target.write(data)

print("File copied successfully")


# =========================================================
# 18. REAL PROJECT EXAMPLE
# =========================================================
#
# Simple Notes Application
#
# =========================================================

print("\n--- Example 18: Notes App ---")

note = "Learn Python File Handling"

# Save note
with open("notes.txt", "a") as file:

    file.write(note + "\n")

# Read notes
with open("notes.txt", "r") as file:

    print(file.read())


# =========================================================
# IMPORTANT INTERVIEW QUESTIONS
# =========================================================
#
# Q1. Difference between "w" and "a"?
#
# "w":
#     Overwrites old data
#
# "a":
#     Adds data at end
#
#
# Q2. Why use with?
#
# Automatic file closing
#
#
# Q3. Difference between read() and readline()?
#
# read():
#     Reads complete file
#
# readline():
#     Reads one line
#
# =========================================================


# =========================================================
# BEST PRACTICES
# =========================================================
#
# 1. Always use 'with'
#
# 2. Always handle file exceptions
#
# 3. Close files properly
#
# 4. Use append mode carefully
#
# 5. Use binary mode for images/videos
#
# =========================================================


# =========================================================
# FINAL SUMMARY
# =========================================================
#
# open()      -> Open file
# read()      -> Read content
# write()     -> Write content
# append()    -> Add content
# close()     -> Close file
# seek()      -> Move cursor
# tell()      -> Current cursor position
# with        -> Automatic cleanup
#
# =========================================================


# =========================================================
# END OF FILE
# =========================================================