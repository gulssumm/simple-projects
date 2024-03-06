import random


def game():
    with open("words.txt", "r") as file:
        all_text = file.read()
        word = list(map(str, all_text.split()))
        random_word = random.choice(word)
        print(random_word)

    guesses = ""
    counter = 6
    done = False

    while not done:
        guess = input("enter a letter: ")
        guesses += guess

        for letter in random_word.lower():
            if letter.lower() in guesses:
                print(letter, end="")
            else:
                print("_", end="")
        print("")

        if guess not in random_word:
            if counter == 6:
                print("________ ")
                print("| | ")
                print("| ")
                print("| ")
                print("| ")
                print("| ")
            elif counter == 5:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print("| ")
                print("| ")
                print("| ")
            elif counter == 4:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print("| / ")
                print("| ")
                print("| ")
            elif counter == 3:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print("| /| ")
                print("| ")
                print("| ")
            elif counter == 2:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print(r"| /|\ ")
                print("| ")
                print("| ")
            elif counter == 1:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print(r"| /|\ ")
                print("| / ")
                print("| ")
            elif counter == 0:
                print("________ ")
                print("| | ")
                print("| 0 ")
                print(r"| /|\ ")
                print(r"| / \ ")
                print("| ")
                restart()
            counter -= 1

        if guesses == random_word:
            done = True
            restart()


def restart():
    choice = input("Do you want to quit? y/n: ")
    if choice == "n":
        game()
    else:
        quit()


while True:
    print("-----HANGMAN GAME-----")
    game()
