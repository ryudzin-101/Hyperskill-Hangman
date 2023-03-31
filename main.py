import random

win_times = 0
lost_times = 0
print("H A N G M A N\n")
while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:\n')
    if choice == "play":
        words = random.choice(["python", "java", "swift", "javascript"])
        hidden_answer = list(len(words) * '-')
        typed = ""
        attempts = 8
        while attempts > 0 and hidden_answer != list(words):
            guess = input(f"{''.join(hidden_answer)}\nInput a letter: \n")
            if len(guess) != 1:
                print("Please, input a single letter.\n")
                continue
            elif not (guess.islower() and guess.isalpha()):
                print("Please, enter a lowercase letter from the English alphabet.\n")
                continue
            if guess in typed:
                print("You've already guessed this letter.\n")
            elif guess in words:
                for check in range(len(words)):
                    if words[check] == guess:
                        hidden_answer[check] = guess
            else:
                print("That letter doesn't appear in the word.\n")
                attempts -= 1
            typed += guess
        if hidden_answer == list(words):
            print(f"""You guessed the word {words}!\nYou survived!""")
            win_times += 1
            continue
        else:
            print("You lost!")
            lost_times += 1
            continue
    if choice == "results":
        print(f"You won: {win_times} times.\nYou lost: {lost_times} times.")
    if choice == "exit":
        break
