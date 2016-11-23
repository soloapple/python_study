import random

inventory=()
if not inventory:
    print("you are empty handed")

input("continue")

inventory=(
    "sword",
    "armor",
    "shield",
    "healing potion"
    )

print("the tuple inventory is:")
print(inventory)

for item in inventory:
    print("item ", item)

print(inventory[1:3])

chest=("gold", "civer")
inventory += chest

print(inventory)

word = random.choice(inventory)
print(word)

input("Press the entry key to exit.")
