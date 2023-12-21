
print("Welcome to Idan's Hangman Game")
def choose_phrase_by_index(index):
    phrases = ["just do it", "this means more", "im the one", "python is fun", "impossible is nothing",
               "against all odds",
               "always be yourself", "be your best", "always be honest", "avoid drunk driving"]
    if 0 <= index < len(phrases):
        return phrases[index].lower()
    else:
        raise ValueError("Invalid index. Please choose a number within the range.")


def display_phrase(phrase, guessed_letters):
    display = ""
    for char in phrase:
        if char.lower() in guessed_letters:
            display += char
        elif char == " ":
            display += "-"
        else:
            display += "_"
    return display


def hangman():
    num_phrases = len(
        ["just do it", "this means more", "im the one", "python is fun", "impossible is nothing", "against all odds",
         "always be yourself", "be your best", "always be honest", "avoid drunk driving"])

    # Display available index numbers
    print("Available phrases:")
    for i in range(1, num_phrases + 1):
        print(i)

    # Ask the user to choose a number
    while True:
        try:
            chosen_number = int(input(f"Choose a number (1-{num_phrases}): "))
            phrase_to_guess = choose_phrase_by_index(chosen_number - 1)
            break
        except ValueError as e:
            print(e)

    guessed_letters = []
    score = 0

    print(display_phrase(phrase_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess not in phrase_to_guess:
            print("Incorrect! Try again.")
            score -= 1
        else:
            print("Correct!")
            score += 5

        phrase_display = display_phrase(phrase_to_guess, guessed_letters)
        print(phrase_display)

        if "_" not in phrase_display:
            print("Congratulations! You guessed the phrase:", phrase_to_guess)
            print("Your final score:", score)
            break


if __name__ == "__main__":
    hangman()
