import random

def computerGuess(lowval, highval, randnum, count=1):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
        else:
            count = count + 1
            return computerGuess(guess+1, highval, randnum, count)
    else:
        # number not found
        return -1

# generate a random number between 1 and 100
randnum = random.randint(1,101)

count = 1
guess = 0

while guess != randnum:
    # Get the user's guess
    guess = (int)(input("Enter your guess between 1 and 100: "))
    if guess < randnum:
        print("Higher")
    elif guess > randnum:
        print("Lower")
    else:
        print("Correct!")
        break
    count = count + 1

print(f'you tried {count} times')
print(f'computer took {computerGuess(0, 100, randnum)} steps')
