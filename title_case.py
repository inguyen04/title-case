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






