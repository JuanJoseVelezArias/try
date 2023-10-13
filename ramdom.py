import random
list = ["Juan Esteban", "Anderson", "Yo", "Wilson"]
Win1 = random.choice(list)
Win2 = random.choice(list)
while Win2 == Win1:
    Win2 = random.choice(list)
print(f"Los ganadores son {Win1} y {Win2}")