import random

# I write some rules of hangman so the user know the game.
print("------------HANGMAN GAME------------")
print("RULES:")
print("1. You need to guess the letter of the word")
print("2. You have total of 6 wrong guesses")
print("3. If you can't guess the word within 6 wrong guesses, you'll lose the game")
print("4. Guess word, and you'll win hangman")

# Some words are stored in a list, so we can pick one of them randomly for user to play
lst = ["apple", "dollar", "programming", "hotel", "remote"]

playing = True

# While loop which will continue to play till user want to play the game.
while playing:
    random_word = random.choice(lst)            # picking a random word from the list
    n = len(random_word)                        # taking length of random word and stored in local variable (n)
    print(f"\n\nword contains {n} characters")
    hidden_word = ["_"] * n                     # making a list of "_" and keeping it in our hidden_word

    user_guesses = []                           # Making a list of user's previous guesses, so we let them know that they guessed this letter before or not
    retry_counter = 6                           # Total retries for user

    while retry_counter > 0 and "_" in hidden_word:                 # Checking if retry counter in not zero (0) and our hidden_words still contains some empty spaces like this(_)

        print("\nWord: ", " ".join(hidden_word))                    # Combining the letters of hidden_word which are guessed so far
        print(f"Retries: {retry_counter}")                          # printing remaining retries

        letter = input("\nEnter your letter: ").lower()             # User input

        if not letter.isalpha() or len(letter) != 1:                # Checking if user input is not an alphabet or the length of user input is not equal to zero (1)
            print("Invalid Input! Please Enter single alphabet")    # Invalid input by user if one of above conditions are true
            continue                                                # Get back to the while loop, and rerun from there.

        if letter in user_guesses:                                  # Checking if user already guess the letter before
            print(f"You Already guess this letter: {letter}")       # If above condition it true, go to the while loop again .
            continue

        user_guesses.append(letter)                                 # Add the user's entered letter in the user_guesses [list]

        if letter in random_word:                                   # Checking if user's entered letter exist in random_word
            print("Your guess is right")                            # printing, that user's guess is right

            for index, char in enumerate(random_word):              # Running a for loop in enumerate(random_word) from which we will take index and Character of random_word
                if letter == char:                                  # If user's letter match one of the letter in random_word
                    hidden_word[index] = letter                     # We will replace that letter with "_" in hidden_word

        else:
            print("Wrong Guess!")                                   # If user's guessed letter does not match
            retry_counter -= 1                                      # We will -1 the retry counter

    if "_" not in hidden_word:                                              # Checking if hidden_word does not contain "_" in it.
        print(f"\nYou Guessed the word ( {random_word} ), well played")     # User will win, because he guessed all the letters of the words

    else:                                              # if user does not guess the word, he will lose the game
        print("\nYou Lose, better luck next time!")    # printing a message for user, that he/she lose the game
        print(f"The word was ( {random_word} )")       # printing that random word which they failed to guess

    try_again = input("If want to play again then Enter Y or Yes: ").lower()    # asking user if they want to play again or not. Using ( .lower() ), so if user entered Y or Yes in any case, we can easily check it in out if condition below.

    if try_again != 'y' and try_again != 'yes':  # Checking if user wants to play again.
        print("\nThanks for playing HANGMAN.!")  # Thanking user to play
        playing = False                          # End the game./
