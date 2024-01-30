from random import randint

from hangman import Hangman


def play():
    hangman = Hangman("words.txt")

    hangman.new_game()
    print(f"The word has {len(hangman.word)} letters")
    print(hangman.show_result())

    attempt = input('Insert a letter ==> ')

    while attempt != '0':
        res, msg = hangman.try_letter(attempt)

        if res:
            print(f"You guessed in {hangman.attempts} attempts!")
            print(f'Word was "{hangman.show_result()}"')
            break

        print(msg)

        print(hangman.show_result())
        print(f"Used letters: [{hangman.show_tried_letters()}], total errors: {hangman.errors}")
        print("")
        attempt = input('Insert a letter ==> ')
        if attempt == "?":
            print(f'You gave up! word was "{hangman.show_result(end_game=True)}"')
            break

    print("Game over")


def load_words():
    with open("words.txt", 'r') as f_in:
        with open("filtered_word.txt", 'w') as f_out:
            for word in f_in:
                if len(word) > 4:
                    f_out.write(word)


if __name__ == "__main__":
    play()
