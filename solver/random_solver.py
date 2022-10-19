import random

G = "green"
Y = "yellow"
B = "black"


class RandomSolver:
    def __init__(self, wordlist, guess_fn):
        self.wordlist = wordlist
        self.guess_fn = guess_fn
        self.bad_words = set()
        self.bad_letters = set()
        self.good_letters = set()

    def solve(self):
        while self.wordlist:
            word = random.choice(self.wordlist)
            hints = self.guess_fn(word)
            # print(word, hints)
            if hints == [G, G, G, G, G]:
                return word
            self.filter_words(word, hints)

    def filter_words(self, bad_word, hints):
        old_count = len(self.wordlist)
        # update hints
        self.bad_words.add(bad_word)

        for letter, color in zip(bad_word, hints):
            if color in (Y, G):
                self.good_letters.add(letter)
            elif color == B:
                self.bad_letters.add(letter)

        self.bad_letters -= self.good_letters

        # filter words
        self.wordlist = [
            word
            for word in self.wordlist
            if word not in self.bad_words
            and all(bad_letter not in word for bad_letter in self.bad_letters)
            and all(good_letter in word for good_letter in self.good_letters)
        ]
        # print(f"word_list: {old_count} -> {len(self.wordlist)}")
