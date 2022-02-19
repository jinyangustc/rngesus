import secrets

with open("restaurants.txt") as f:
    restaurants = f.readlines()

with open("history.txt") as f:
    history = f.readlines()

restaurants = [x for x in restaurants if x not in history]

selected = secrets.choice(restaurants)
history.append(selected)

with open("history.txt", "w") as f:
    f.writelines(history[-5:])

print(f"RNGesus has spoken: {selected}")
