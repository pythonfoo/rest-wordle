import pytest

from rest_wordle.utils import generate_master_mind_result

G = "green"
Y = "yellow"
B = "black"


@pytest.mark.parametrize(
    ["word", "secret_word", "expected"],
    [
        pytest.param("hello", "hello", [G, G, G, G, G], id="word is secret word"),
        pytest.param("words", "hello", [B, Y, B, B, B], id="one letter in wrong place"),
        pytest.param("stuck", "hello", [B, B, B, B, B], id="all letters wrong"),
        pytest.param(
            "cheer",
            "hello",
            [B, Y, Y, B, B],
            id="secret word doesn't contain two e letters",
        ),
    ],
)
def test_mastermind(word, secret_word, expected):
    assert generate_master_mind_result(word, secret_word) == expected
