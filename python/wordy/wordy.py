operators = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '/'}

def answer(question):
    question = question[8:-1]
    if question == '':
        raise ValueError('Error')
    for keys, values in operators.items():
        question = question.replace(keys, values)
    expression = question.split()
    try:
        if len(expression) % 2 == 0:  
            raise ValueError('Error')
        while len(expression) >= 3:
            expression[:3] = [str(eval(' '.join(expression[:3])))]
        return eval(expression[0])
    except (SyntaxError, NameError):
        raise ValueError('Error')  