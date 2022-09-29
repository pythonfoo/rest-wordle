import random
from pathlib import Path

from fastapi import FastAPI

words = (Path(__file__).parent / "wordlist.txt").read_text().splitlines()
secret_word = random.choice(words)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "secret_word": secret_word}


@app.get("/new_word")
async def new_word():
    global secret_word
    secret_word = random.choice(words)
    return {"secret_word": secret_word}


@app.get("/guess/{word}")
async def guess(word: str):
    def generate_mastermind_result(word):
        for idx, c in enumerate(word):
            if c not in secret_word:
                yield "X"
            elif c == secret_word[idx]:
                yield "G"
            else:
                yield "Y"

    return {
        "mastermind_result": "".join(generate_mastermind_result(word)),
    }
