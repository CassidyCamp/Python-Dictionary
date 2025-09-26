config = {}

userKey1 = input("Enter 1 config key: ")
userValue1 = input("Enter 1 config value: ")

userKey2 = input("Enter 2 config key: ")
userValue2 = input("Enter 2 config value: ")

userKey3 = input("Enter 3 config key: ")
userValue3 = input("Enter 3 config value: ")

config.update({userKey1:userValue1,userKey2:userValue2,userKey3:userValue3})

print(config)