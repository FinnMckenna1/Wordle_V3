import random
with open("target_words.txt", "r") as files:
	target_words = [line.strip() for line in files]
target = random.choice(target_words)

with open("all_words.txt", "r") as f:
	all_words_list = [line.strip() for line in f]

def score_guess(target, guess):
    score = ["0"] * len(target)
    target_used = [False] * len(target)

    for i in range(len(target)):
        if guess[i] == target[i]:
            score[i] = "2"
            target_used[i] = True

    for i in range(len(target)):
        if score[i] == "0":
            for j in range(len(target)):
                if not target_used[j] and guess[i] == target[j]:
                    score[i] = "1"
                    target_used[j] = True
                    break

    return "".join(score)

attempts = 5

print("--------------------------------------")
print("*******  WELCOME TO WORDLE  **********")
print("RULES: \n"
	  "1. This is the firs rule. \n"
	  "2. This is the second rule. \n"
	  "3. This is the third rule. \n"
	  "5. Have Fun.")
print("--------------------------------------")
print(f"CHEAT: {target}")
for attempt in range(attempts):
    guess = input(f"Attempts {attempt + 1}/{attempts}: ").lower()

    if len(guess) != len(target):
        print(f"Word must be {len(target)} letters long.")
        continue
    elif guess not in all_words_list:
        print(f"'{guess}' Is not a valid word. Please try again.")
        continue
    elif guess == target:
        print("Congrats! You guessed the word!")
        break

    score = score_guess(target, guess)
    print("Result:", score)
else:
    print(f"Out of attempts! The word was: {target}")


print("NEW COMMIT")