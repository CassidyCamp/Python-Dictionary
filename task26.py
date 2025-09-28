def merge_dicts(a: dict, b: dict) -> dict:
    a.update(b)
    return a

dict1 = {
    'name': 'daler',
    'age': 17,
    'city':'samarqand'
}
dict2 = {
    'name': 'samandar',
    'age': 20,
}

print(merge_dicts(dict1, dict2))