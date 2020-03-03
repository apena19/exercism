def es_numero(n):
    try:
        int(n)
    except ValueError:
        if n == "+" or n == "-" or n == "*" or n == "/":
            return True
        else:
            return False
    return True


def error(question):
    return question.find("cubed")


def answer(question):
    if error(question) < 0:
        res = question.replace("plus", "+")
        res = res.replace("minus", "-")
        res = res.replace("multiplied by", "*")
        res = res.replace("divided by", "/")
        li = []
        for n in res:
            if es_numero(n):
                li.append(n)
        oper = ''
        print(li)
        for c in li:
            oper += c
        print(oper)
        return int(eval(oper))
    else:
        raise ValueError(".+")
        
print(answer("What is 2 2 minus 3?"))