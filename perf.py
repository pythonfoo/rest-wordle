import random
from collections import defaultdict
from functools import partial

from rich import print
from rich.progress import track
from rich.traceback import install

from rest_wordle import get_hints, wordlist
from solver import all_solvers
from solver.random_solver import G

install(show_locals=True)

counter = defaultdict(int)


def get_guess_fn(word, solver_name, secret_word):
    counter[solver_name] += 1
    return get_hints(word=word, secret_word=secret_word)


def main():
    for _ in track(range(1000), description="Perfrun"):
        secret_word = random.choice(wordlist)
        # print(secret_word)
        for solver in all_solvers:
            guess = partial(
                get_guess_fn, solver_name=solver.__name__, secret_word=secret_word
            )
            for _ in range(10):
                # we want to test each word 10 times
                guessed_word = solver(wordlist=wordlist, guess_fn=guess).solve()
                assert secret_word == guessed_word, f"{secret_word} != {guessed_word}"

    print(counter)


if __name__ == "__main__":
    main()
