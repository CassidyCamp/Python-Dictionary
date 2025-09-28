def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    result = []

    for key, value in users.items():
        for valueDict in value.values():
            if valueDict:result.append(key)
    return result

users = {
  "ali": {"active": True},
  "vali": {"active": False},
  "eshmat": {"active": True},
  "toshmat": {"active": False}
}

print(get_active_users(users))