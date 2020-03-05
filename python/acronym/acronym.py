import re


def abbreviate(words):
    ac = ""
    words = re.sub(r'[\'_]', '', words)
    words = re.sub(r'[^\w]', ' ', words)

    for i in words.split():
        ac += i[0]
    return ac.upper()
