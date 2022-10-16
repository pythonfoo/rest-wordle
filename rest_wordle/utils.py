from collections import Counter


def generate_master_mind_result(word: str, secret_word: str):
    word = word.lower()

    result = [""] * len(word)
    missing_indexes = []
    secrect_counter = Counter(secret_word)

    for idx, c in enumerate(word):
        if c == secret_word[idx]:
            result[idx] = "green"
            secrect_counter[c] -= 1
        else:
            missing_indexes.append(idx)

    for idx in missing_indexes:
        c = word[idx]
        if c in secrect_counter and secrect_counter[c] > 0:
            result[idx] = "yellow"
            secrect_counter[c] -= 1
        else:
            result[idx] = "black"

    if word == secret_word:
        return result
    else:
        return result
