def convert(number):
    cadena = ''
    for i in range(1, number+1):
        if number % i == 0:
            if i == 3:
                cadena += 'Pling'
            elif i == 5:
                cadena += 'Plang'
            elif i == 7:
                cadena += 'Plong'
    if cadena == '':
        return str(number)
    else:
        return cadena
