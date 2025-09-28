def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}

    for key, value in d.items():
        if value == 0:result.update({key: value})
    return result

dictt = {"a": 0, "b": 5, "c": -3}

print(filter_non_zero(dictt))