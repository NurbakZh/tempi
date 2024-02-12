from lab0maksktl.hangman import get_random_word


def test_hangman():
    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone", "hangman",
             "computer", "science", "programming", "mathematics", "player", "condition",
             "reverse", "water", "board", "geeks", "keyboard", "laptop", "headphone",
             "mouse", "printer", "scanner", "software", "hardware", "network", "server")
    assert find_in_word_list(get_random_word(), WORDS)


def find_in_word_list(word, list_of_words) -> bool:
    for list_part in list_of_words:
        if word == list_part:
            return True
    return False
