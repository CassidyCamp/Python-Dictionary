def count_letters(text: str) -> dict[str, int]:
    result = {}

    for ch in text:
        result.setdefault(ch, text.count(ch))
    return result

word = "assalomu alaykum"
print(count_letters(word))