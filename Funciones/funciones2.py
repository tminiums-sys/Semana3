def sumar(num1, num2):
    return num1 + num2

suma = sumar(15, 20)
print(suma)


def restar(num1, num2):
    return num1 - num2

resta = restar(4, 2)
print(resta)

resta_con_variables = restar(num1=10, num2=3)
print(resta_con_variables)


def multiplicar(num1, num2):
    return num1 * num2

multiplicacion = multiplicar(4, 2)
print(multiplicacion)


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "No se puede dividir entre 0"

division = dividir(20, 5)
print(division)