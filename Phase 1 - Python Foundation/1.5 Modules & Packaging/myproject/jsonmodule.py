import json


# python dictionary
data = {
    "name": "Raju",
    "age": 21,
    "skills": [
        "Python",
        "Django"
    ],
    "active": True,
    "salary": None
}


# dictionary -> json string
json_data = json.dumps(data)

print(json_data)

print(type(json_data))


# pretty json
pretty = json.dumps(
    data,
    indent=4
)

print(pretty)


# json string -> dictionary
parsed = json.loads(json_data)

print(parsed)

print(type(parsed))


# access values
print(parsed["name"])

print(parsed["skills"])


# save json file
with open(
    "data.json",
    "w"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )


# read json file
with open("data.json") as file:

    loaded_data = json.load(file)

    print(loaded_data)


# boolean conversion
sample = {
    "success": True,
    "value": None
}

print(json.dumps(sample))


# nested json
nested = {
    "user": {
        "name": "Raju",
        "city": "Bhopal"
    }
}

print(
    nested["user"]["name"]
)


print("done")