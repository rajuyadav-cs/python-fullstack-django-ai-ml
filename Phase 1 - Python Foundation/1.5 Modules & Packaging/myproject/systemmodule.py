import sys


# python version
print(sys.version)


# version info
print(sys.version_info)


# platform
print(sys.platform)


# command-line arguments
print(sys.argv)


# safe argument access
if len(sys.argv) > 1:

    print(
        "First Argument:",
        sys.argv[1]
    )


# import paths
print(sys.path)


# max integer size
print(sys.maxsize)


# recursion limit
print(sys.getrecursionlimit())


# stdout
sys.stdout.write(
    "Using stdout\n"
)


# stderr
sys.stderr.write(
    "Using stderr\n"
)


print("Program running")


# uncomment to stop program
# sys.exit("Program ended")


print("Done")