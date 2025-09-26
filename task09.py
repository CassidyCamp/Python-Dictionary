users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]

users[0].update({"active": False})
users[1].update({"active": False})
print(users)