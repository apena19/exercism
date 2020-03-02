def is_pangram(sentence):
    import string
    cadena = sentence.lower()
    alfabeto = string.ascii_lowercase
    for letra in alfabeto:
        if letra not in cadena:
            return False
    return True
