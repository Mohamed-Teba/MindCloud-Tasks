import random

score = 0
rounds = 0
wins = 0

print("Welcome player")

while True:
    rounds += 1
    secret = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100")
    print("You have 6 attempts to guess it")

    won = False

    for i in range(1, 7):
        print(f"Attempt {i}/6")
        guess = int(input("Enter your guess: "))

        if guess == secret:
            print("Congratulations!")
            print("You guessed the number")

            remain = 6 - i
            points = remain + 1

            print("Guesses remaining:", remain)
            print("Multiplier: x" + str(points))
            print("Points earned:", points)

            score += points
            wins += 1

            print("Current Score:", score)
            won = True
            break

        elif guess < secret:
            if secret - guess > 10:
                print("Too low")
            else:
                print("Higher")
        else:
            if guess - secret > 10:
                print("Too high")
            else:
                print("Lower")

    if not won:
        print("You lost.")
        print("The number was", secret)

    again = input("Play another round? (y/n): ")

    if again.lower() == "n":
        break

print("Rounds Played:", rounds)
print("Rounds Won:", wins)
print("Final Score:", score)