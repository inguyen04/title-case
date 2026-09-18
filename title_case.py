
def my_cap(text):
    return text[0].upper() + text[1:]


def my_title(text):
    words = []
    for t in text.split():
        words.append(my_cap(t))
    return " ".join(words)
