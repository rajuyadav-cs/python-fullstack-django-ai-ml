import os


# current directory
print(os.getcwd())


# list files/folders
print(os.listdir())


# create folder
if not os.path.exists("demo"):

    os.mkdir("demo")


# check folder
print(os.path.isdir("demo"))


# create file
with open("demo.txt", "w") as file:

    file.write("Hello")


# check file
print(os.path.isfile("demo.txt"))


# file size
print(os.path.getsize("demo.txt"))


# absolute path
print(os.path.abspath("demo.txt"))


# rename file
os.rename("demo.txt", "new_demo.txt")


# join path
path = os.path.join(
    "folder",
    "file.txt"
)

print(path)


# environment variable
print(os.getenv("USERNAME"))


# remove file
os.remove("new_demo.txt")


# remove folder
os.rmdir("demo")


print("done")