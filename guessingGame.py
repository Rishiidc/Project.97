import random
print("Number guessing game")
guess = int(input("Enter your guess between 1 to 9 -> "))
computer = random.randint(1,9)

count = 1
for i in range(1,5):
    if guess ==  computer:
        print("Congrats you won!")
        break 
    if guess<computer:
        print("Guess a bigger number")
        count = count+1
        guess = int(input("Enter your guess between 1 to 9 -> "))
    if guess>computer:
        print("Guess a smaller number")
        count = count+1
        guess = int(input("Enter your guess between 1 to 9 -> "))

if count >= 5:
    print("You lose! the correct number is", str(computer)) 