def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}

    for ch in words:
        result.setdefault(len(ch), []).append(ch)

    return result

words = ["salom", "python", "developer", "javascript", "django", "React"]

print(group_by_length(words))
