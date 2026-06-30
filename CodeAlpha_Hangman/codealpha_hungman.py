import random

while True:

    print("================================")
    print("         HANGMAN GAME")
    print("================================")

    player_name = input("Enter Your Name: ")

    print("\nWelcome", player_name)

    print("\nGAME RULES")
    print("1. Guess the fruit one letter at a time.")
    print("2. You have only 6 wrong chances.")
    print("3. If all letters are guessed, you win!")
    print("4. Points:")
    print("   4 Points = 0 wrong guesses")
    print("   2 Points = 1 or 2 wrong guesses")
    print("   1 Point  = 3 or 4 wrong guesses")
    print("   0 Points = 5 or 6 wrong guesses")

    fruits = [
        "apple",
        "banana",
        "mango",
        "orange",
        "grapes"
    ]

    secret_word = random.choice(fruits)

    guessed_letters = ""
    wrong_guesses = 0

    print("\nCategory : Fruits")
    print("Hint : Fruit starts with", secret_word[0].upper())

    while wrong_guesses < 6:

        display_word = ""

        for letter in secret_word:

            if letter in guessed_letters:
                display_word = display_word + letter
            else:
                display_word = display_word + "_"

        print("\nWord :", display_word)
        print("Wrong Guesses Left :", 6 - wrong_guesses)

        if display_word == secret_word:

            print("\n🎉 Congratulations", player_name + "!")
            print("You guessed the fruit correctly.")

            if wrong_guesses == 0:
                points = 4

            elif wrong_guesses <= 2:
                points = 2

            elif wrong_guesses <= 4:
                points = 1

            else:
                points = 0

            print("Your Score :", points)
            break

        guess = input("\nEnter one letter : ").lower()

        if len(guess) != 1:

            print("Please enter only one letter.")

        elif guess in guessed_letters:

            print("You already guessed this letter.")

        elif guess in secret_word:

            guessed_letters = guessed_letters + guess

            print("✅ Correct Guess!")

        else:

            wrong_guesses = wrong_guesses + 1

            print("❌ Wrong Guess!")

    if wrong_guesses == 6:

        print("\n💀 Game Over!")
        print("The correct fruit was :", secret_word)
        print("Your Score : 0")

    print("\n========================")
    print("1. Play Again")
    print("2. Exit")
    print("========================")

    choice = input("Enter your choice : ")

    if choice == "1":

        continue

    elif choice == "2":

        print("\nThank you for playing,", player_name + "!")
        print("Have a Nice Day!")
        break

    else:

        print("Invalid Choice!")
        print("Game Closed.")
        break