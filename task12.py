inventory = {
    "Macbook pro":{"quantity":12},
    "Microsoft Surface":{"quantity":8}
}

search = "Macbook air"

if search not in inventory:
    inventory.update( {search: {"quantity":0}} ) 
print(inventory)