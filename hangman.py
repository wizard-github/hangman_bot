from random import randint


class Hangman:
    def __init__(self, res_file):
        self.__italian_words = res_file
        self.__guessed_letters = list()
        self.errors = None
        self.attempts = None
        self.word = None
        self.__guessed_items = list()  # List of boolean
        self.__outcome_letters = list()

        self.new_game()

    def get_word(self) -> str:
        words = list()
        with open(self.__italian_words, 'r') as f_in:
            for (count, word) in enumerate(f_in):
                words.append(word.strip())

        item = randint(0, count - 1)

        return words[item]

    def new_game(self) -> None:
        self.word = self.get_word()
        # self.word = "competenze"
        self.__guessed_letters.clear()
        self.attempts = 0
        self.errors = 0
        self.__guessed_items.clear()
        self.__guessed_items = [False] * len(self.word)
        self.__outcome_letters.clear()

    def try_letter(self, letter: str) -> (bool, str):
        if letter is None or len(letter) == 0 or not letter[0].isalpha():
            return False, "Invalid input"

        new_letter = letter[0]
        if new_letter in self.__outcome_letters:
            return False, "Letter already tried"

        self.attempts += 1
        self.__outcome_letters.append(new_letter)
        self.__outcome_letters.sort()

        if new_letter in self.word:
            self.__guessed_letters.append(new_letter)
        else:
            self.errors += 1

        self.__guessed_items = [c in self.__guessed_letters for c in self.word]

        return all(self.__guessed_items), f"{self.__guessed_items.count(False)} letters remaining"

    def show_tried_letters(self) -> str:
        return ' '.join(self.__outcome_letters)

    def show_result(self, end_game=False) -> str:
        if end_game:
            result = self.word
        else:
            result = [c if self.__guessed_items[i] else '_' for i, c in enumerate(self.word)]

        return ' '.join(result)








