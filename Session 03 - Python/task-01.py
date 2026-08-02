import random

posture = random.choice(["sitting", "standing"])
direction = random.choice(["left", "right", "facing"])
distance = random.randint(1, 10)

print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance: {distance}")

if posture == "sitting":
    print("Nexus stands up")

if direction == "left":
    print("Nexus turns right towards the door")
elif direction == "right":
    print("Nexus turns left towards the door")

while distance > 0:
    print(f"Moving {distance} steps left")
    distance -= 1

print("Door reached")