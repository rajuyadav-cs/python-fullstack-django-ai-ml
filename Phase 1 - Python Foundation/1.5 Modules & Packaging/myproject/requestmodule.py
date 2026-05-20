# requests_examples.py

# requests library is used to send HTTP requests
# it helps Python communicate with APIs and websites

import requests


# ==========================================================
# SIMPLE GET REQUEST
# ==========================================================

# requests.get(url)
#
# get() sends a GET request to the given URL
# GET request means:
# "Give me data"

response = requests.get(
    "https://api.github.com"
)

# response object contains everything returned by server

print(response)

# output example:
# <Response [200]>


print("\n--------------------\n")


# ==========================================================
# STATUS CODE
# ==========================================================

# status_code tells whether request succeeded or failed

print(response.status_code)

# common status codes:
#
# 200 -> success
# 201 -> created
# 400 -> bad request
# 401 -> unauthorized
# 404 -> not found
# 500 -> server error


print("\n--------------------\n")


# ==========================================================
# RESPONSE TEXT
# ==========================================================

# .text returns raw response as string

print(response.text[:200])

# [:200] means first 200 characters only


print("\n--------------------\n")


# ==========================================================
# RESPONSE HEADERS
# ==========================================================

# headers contain metadata about response

print(response.headers)


print("\n--------------------\n")


# ==========================================================
# JSON RESPONSE
# ==========================================================

# many APIs return JSON data
#
# .json() converts JSON response into Python dictionary

data = response.json()

print(type(data))

print(data)


print("\n--------------------\n")


# ==========================================================
# ACCESSING JSON DATA
# ==========================================================

# since JSON became Python dictionary,
# we can access keys normally

print(data["current_user_url"])

print(data["current_user_authorizations_html_url"])


print("\n--------------------\n")


# ==========================================================
# GET REQUEST WITH PARAMETERS
# ==========================================================

# params are query parameters added to URL

params = {
    "q": "python"
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

# internally URL becomes:
# https://api.github.com/search/repositories?q=python

print(response.status_code)


search_data = response.json()

print(search_data.keys())


print("\n--------------------\n")


# ==========================================================
# POST REQUEST
# ==========================================================

# POST request is used to send data to server

payload = {
    "name": "Raju",
    "age": 21
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload
)

# json=payload automatically converts dictionary to JSON

print(response.status_code)

print(response.json())


print("\n--------------------\n")


# ==========================================================
# CUSTOM HEADERS
# ==========================================================

# headers send extra information with request

headers = {
    "User-Agent": "MyPythonApp"
}

response = requests.get(
    "https://api.github.com",
    headers=headers
)

print(response.status_code)


print("\n--------------------\n")


# ==========================================================
# TIMEOUT
# ==========================================================

# timeout prevents waiting forever

try:

    response = requests.get(
        "https://api.github.com",
        timeout=5
    )

    print("Request successful")

except Exception as e:

    print(e)


print("\n--------------------\n")


# ==========================================================
# ERROR HANDLING
# ==========================================================

try:

    response = requests.get(
        "https://wrong-url-example.com"
    )

    # raise_for_status() raises error
    # if status code is bad

    response.raise_for_status()

except requests.exceptions.HTTPError:

    print("HTTP error occurred")

except requests.exceptions.ConnectionError:

    print("Connection error")

except Exception as e:

    print(e)


print("\n--------------------\n")


# ==========================================================
# DOWNLOADING CONTENT
# ==========================================================

# .content returns binary data

response = requests.get(
    "https://api.github.com"
)

with open("github_response.txt", "wb") as file:

    # wb means write binary

    file.write(response.content)

print("File downloaded")


print("\n--------------------\n")


# ==========================================================
# REQUEST SESSION
# ==========================================================

# Session keeps connection alive
# useful for multiple requests

session = requests.Session()

response = session.get(
    "https://api.github.com"
)

print(response.status_code)


print("\n--------------------\n")


# ==========================================================
# REAL API EXAMPLE
# ==========================================================

response = requests.get(
    "https://api.github.com/users/octocat"
)

user_data = response.json()

print(user_data["login"])

print(user_data["followers"])

print(user_data["following"])

print(user_data["public_repos"])


print("\n--------------------\n")


# ==========================================================
# CHECKING RESPONSE SUCCESS
# ==========================================================

if response.status_code == 200:

    print("Request successful")

else:

    print("Request failed")


print("\n--------------------\n")


# ==========================================================
# RESPONSE URL
# ==========================================================

# final URL after request

print(response.url)


print("\n--------------------\n")


# ==========================================================
# RESPONSE METHOD
# ==========================================================

# request method used

print(response.request.method)


print("\n--------------------\n")


# ==========================================================
# SUMMARY
# ==========================================================

# requests.get(url)
# sends GET request
#
# requests.post(url)
# sends POST request
#
# response.status_code
# HTTP status code
#
# response.text
# response as string
#
# response.json()
# response JSON -> Python dictionary
#
# response.headers
# response metadata
#
# response.content
# binary data
#
# params={}
# query parameters
#
# headers={}
# custom headers
#
# timeout=5
# maximum wait time

print("done")