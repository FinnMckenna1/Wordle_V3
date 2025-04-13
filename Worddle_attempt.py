import random
# Load target words from file
with open("target_words.txt", "r") as files:
	target_words = [line.strip() for line in files]
# Randomly select one word as the target word
target = random.choice(target_words)

# Load all valid guessable words from file
with open("all_words.txt", "r") as f:
    all_words_list = [line.strip() for line in f]
# #
# --------------------------------------------------------------------------------
# def score_guess(target, guess):
#
#     """
#         Compares the guessed word with the target word and returns a score string.
#
#         Scoring:
#         - '2' for correct letter in the correct position
#         - '1' for correct letter in the wrong position
#         - '0' for incorrect letter
#
#         Parameters:
#         target: The target word to guess.
#         guess: The player's guessed word.
#
#         Returns:
#         str: A string of digits representing the score for each letter.
#         """
#
#
#
    # score = ["0"] * len(target)
    # target_used = [False] * len(target)
    # # First pass: check for correct letters in correct positions
    # for i in range(len(target)):
    #     if guess[i] == target[i]:
    #         score[i] = "2"
    #         target_used[i] = True
    #
    # # Second pass: check for correct letters in wrong positions
    # for i in range(len(target)):
    #     if score[i] == "0":
    #         for j in range(len(target)):
    #             if not target_used[j] and guess[i] == target[j]:
    #                 score[i] = "1"
    #                 target_used[j] = True
    #                 break
#
#     return "".join(score)
# -------------------------------------------------------------------------
def score_guess(target, guess):
    score = ["0"] * len(target)

    for i in range(len(target)):
        if guess[i] == target[i]:
            score[i] = "2"
        elif guess[i] in target:
            score[i] = "1"
    return "".join(score)

attempts = 5
# Set number of attempts

# Game intro and rules
print("--------------------------------------")
print("*******  WELCOME TO WORDLE  **********")
print("RULES: \n"
	  "1. This is the firs rule. \n"
	  "2. This is the second rule. \n"
	  "3. This is the third rule. \n"
	  "5. Have Fun.")
print("--------------------------------------")
print(f"CHEAT: {target}")

# Main game loop
print(f"CHEAT WORD IS: {target}")
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

