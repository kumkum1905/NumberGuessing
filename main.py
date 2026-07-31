import random

# Generate a random 4-digit number with unique digits
num = "".join(random.sample("0123456789", 4))

attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("Guess the 4-digit number.\n")

while True:
    cl = input("Enter your guess: ")

    # Input validation
    if len(cl) != 4 or not cl.isdigit():
        print("❌ Please enter exactly 4 digits.\n")
        continue

    attempts += 1
    count = 0

    for i in range(4):
        if cl[i] == num[i]:
            print(f"{cl[i]} is in the RIGHT position.")
            count += 1
        elif cl[i] in num:
            print(f"{cl[i]} is PRESENT but in the wrong position.")

    if count == 0:
        print("❌ No digits are in the correct position.")

    if count == 4:
        print("\n🎉 Congratulations! You guessed the number!")
        print(f"The number was: {num}")
        print(f"You took {attempts} attempts.")
        break

    print("-" * 35)