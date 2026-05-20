from pathlib import Path


# current directory
print(Path.cwd())


# home directory
print(Path.home())


# create path object
file = Path("demo.txt")


# create file
file.touch()


# write file
file.write_text(
    "Hello from pathlib"
)


# read file
print(file.read_text())


# file exists?
print(file.exists())


# file name
print(file.name)


# extension
print(file.suffix)


# file name without extension
print(file.stem)


# absolute path
print(file.absolute())


# file size
print(file.stat().st_size)


# create folder
folder = Path("test_folder")

if not folder.exists():

    folder.mkdir()


# join paths
path = Path("folder") / "file.txt"

print(path)


# list current directory
for item in Path(".").iterdir():

    print(item)


# search python files
for py_file in Path(".").glob("*.py"):

    print(py_file)


# rename file
file.rename("new_demo.txt")


# delete file
Path("new_demo.txt").unlink()


# remove folder
folder.rmdir()


print("done")