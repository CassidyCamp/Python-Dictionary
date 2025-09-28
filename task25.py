def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    for student in people:
        result.setdefault(student["age"], []).append(student["name"])
    print(result)


persons = [
    {
        "name": "ali",
        "age": 12
    },
    {
        "name": "vali",
        "age": 14
    },
    {
        "name": "gani",
        "age": 12
    },
    {
        "name": "smai",
        "age": 19
    },
]

group_by_age(persons)

# {
#     12: ["ali", "gani"],
#     14: ["vali"],
#     19: ["sami"]
# }
