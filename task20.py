permissions = {"read": True, "write": False, "delete": True}
result = ""
for key, val in permissions.items():
    if val:result += key + " "

print(result)