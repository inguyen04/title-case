def my_cap(text):
    return text[0].upper() + text[1:]


def my_title(text):
    words = []
    for t in text.split():
        if t not in ("the", "a", "an"):
            words.append(my_cap(t))
        else:
            words.append(t)
    return " ".join(words)








def test_driver():
    cases = [
        ("the human torch", "The Human Torch"),
        ("uatu the watcher", "Uatu The Watcher"),
        ("susan storm-richards", "Susan Storm-richards"),
    ]
    for given, expected in cases:
        got = my_title(given)
        print(got == expected, repr(given), "->", repr(got))


if __name__ == "__main__":
    test_driver()