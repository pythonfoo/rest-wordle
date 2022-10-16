import random
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils import generate_master_mind_result

words = (Path(__file__).parent / "wordlist.txt").read_text().splitlines()
secret_word = random.choice(words)
print(secret_word)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "secret_word": secret_word}


@app.get("/new_word")
async def new_word():
    global secret_word
    secret_word = random.choice(words)
    return {"secret_word": secret_word}


@app.get("/wordlist")
async def wordlist():
    return {"wordlist": words}


@app.get("/guess/{word}")
async def guess(word: str):
    word = word.lower()

    if word not in words:
        return JSONResponse(status_code=404, content={"message": "word not found"})
    if word == secret_word:
        return JSONResponse(
            status_code=200,
            content={"word": word, "mastermind_result": ["green"] * len(word)},
        )
    else:
        return JSONResponse(
            status_code=202,
            content={
                "word": word,
                "mastermind_result": list(
                    generate_mastermind_result(word=word, secret_word=secret_word)
                ),
            },
        )
