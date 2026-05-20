# python-dotenv is used to load variables
# from .env file

from dotenv import load_dotenv

import os


# ==========================================================
# LOAD .env FILE
# ==========================================================

# load_dotenv() loads environment variables
# from .env file

load_dotenv()


print("\n--------------------\n")


# ==========================================================
# ACCESS VARIABLES
# ==========================================================

# os.getenv("VARIABLE_NAME")

api_key = os.getenv("API_KEY")

username = os.getenv("USERNAME")

password = os.getenv("PASSWORD")


print(api_key)

print(username)

print(password)


print("\n--------------------\n")


# ==========================================================
# DEFAULT VALUE
# ==========================================================

# if variable does not exist,
# default value is used

host = os.getenv(
    "HOST",
    "localhost"
)

print(host)


print("\n--------------------\n")


# ==========================================================
# TYPE CONVERSION
# ==========================================================

# environment variables are always strings

port = int(os.getenv("PORT"))

print(port)

print(type(port))


print("\n--------------------\n")


# ==========================================================
# BOOLEAN CONVERSION
# ==========================================================

debug = os.getenv("DEBUG") == "True"

print(debug)

print(type(debug))


print("\n--------------------\n")


# ==========================================================
# PRACTICAL DATABASE CONFIG
# ==========================================================

db_config = {
    "host": os.getenv(
        "DB_HOST",
        "localhost"
    ),

    "user": os.getenv(
        "DB_USER",
        "admin"
    ),

    "password": os.getenv(
        "DB_PASSWORD",
        "1234"
    )
}

print(db_config)


print("\n--------------------\n")


# ==========================================================
# CHECK MISSING VARIABLE
# ==========================================================

secret = os.getenv("SECRET_KEY")

if secret:

    print("Secret key found")

else:

    print("Secret key missing")


print("\n--------------------\n")


# ==========================================================
# SUMMARY
# ==========================================================

# load_dotenv()
# loads .env file
#
# os.getenv("KEY")
# gets variable value
#
# os.getenv("KEY", default)
# gets value or default
#
# environment variables are strings
#
# use int(), float(), bool conversion if needed

print("done")