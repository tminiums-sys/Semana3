#Calculadar la edad de una persona y decir si es mayo o menor de edad
from datetime import datetime
from colorama import Fore, Style
try:
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    edad = datetime.now().year - año_nacimiento
    if edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")
except ValueError:
    print(f"{Fore.RED}Ingrese un valor un numerico.{Style.RESET_ALL}")