import random
from typing import Callable, List, Literal, Text


class FilterSolver:
    def __init__(
        self,
        wordlist: List[Text],
        guess_fn: Callable[[Text], List[Literal["black", "yellow", "green"]]],
    ):
        self.wordlist = wordlist
        self.guess_fn = guess_fn

    def select_word(self, wordlist: List[Text]) -> Text:
        return random.choice(wordlist)

    def solve(self) -> Text:
        counter = 0

        while len(self.wordlist) > 1:
            counter += 1

            guess_word = self.select_word(self.wordlist)
            guess_result = self.guess_fn(guess_word)

            if not all(status == "green" for status in guess_result):
                self.wordlist.remove(guess_word)

            for index, (char, status) in enumerate(zip(guess_word, guess_result)):
                if status == "green":
                    self.wordlist = [
                        *filter(
                            lambda word: word[index] == char,
                            self.wordlist,
                        )
                    ]
                elif status == "yellow":
                    self.wordlist = [
                        *filter(
                            lambda word: char in word and word[index] != char,
                            self.wordlist,
                        )
                    ]
                elif (
                    status == "black"
                    and guess_word.count(char) > 1
                    and not any(
                        other_status in {"green", "yellow"}
                        for other_index, (other_char, other_status) in enumerate(
                            zip(guess_word, guess_result),
                        )
                        if char == other_char and index != other_index
                    )
                ):
                    self.wordlist = [
                        *filter(
                            lambda word: char not in word,
                            self.wordlist,
                        )
                    ]

        solution, *_ = self.wordlist

        return solution


class DistinctFilterSolver(FilterSolver):
    def select_word(self, wordlist: List[Text]) -> Text:
        max_distinctness = len({*max(wordlist, key=lambda word: len({*word}))})
        wordlist = list(
            filter(
                lambda word: len({*word}) == max_distinctness,
                wordlist,
            )
        )
        return super().select_word(wordlist)
