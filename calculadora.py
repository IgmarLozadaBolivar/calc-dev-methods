import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu():
    while True:
        try:
            limpiar_pantalla()
            print("---------------------------")
            print("CALCULADORA BÁSICA SYMBOLAB")
            print("---------------------------\n")
            opcion = int(input("MENU DE OPCIONES\n" +
                            "1. Suma\n" +
                            "2. Resta\n" +
                            "3. Multiplicación\n" +
                            "4. División\n" +
                            "5. Salir del programa\n" +
                            "Ingrese una opción: "))
            return opcion
        except ValueError:
            print("No se permite el ingreso de dato vacío o no numérico.")
            input("Pulse una tecla para continuar...")
    

def pausa():
    input("Pulse una tecla para continuar...")

def suma(numero1, numero2):
    resultado = numero1 + numero2
    if resultado % 1 == 0:
        limpiar_pantalla()
        print("El resultado de tu suma es:", round(resultado))
        pausa()
    else:
        limpiar_pantalla()
        print("El resultado de tu suma es:", resultado)
        pausa()

def resta(numero1, numero2):
    resultado = numero1 - numero2
    if resultado % 1 == 0:
        limpiar_pantalla()
        print("El resultado de tu resta es:", round(resultado))
        pausa()
    else:
        limpiar_pantalla()
        print("El resultado de tu resta es:", resultado)
        pausa()

def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    if float(numero1).is_integer() and float(numero2).is_integer():
        limpiar_pantalla()
        print("El resultado de tu multiplicación es:", round(resultado))
        pausa()
    else:
        limpiar_pantalla()
        print("El resultado de tu multiplicación es:", resultado)
        pausa()

def division(numero1, numero2):
    resultado = numero1 / numero2
    if numero2 == 0:
        print("No se permite la división por cero.")
        pausa()
    elif resultado % 1 == 0:
        limpiar_pantalla()
        print("El resultado de tu división es:", round(resultado))
        pausa()
    else:
        limpiar_pantalla()
        print("El resultado de tu división es:", resultado)
        pausa()

while True:
    opcion = menu()

    if opcion == 1:
        limpiar_pantalla()
        print("-----------------")
        print("OPERACION DE SUMA")
        print("-----------------\n")
        numero1 = float(input('Ingrese un número: '))
        numero2 = float(input('Ingrese otro número: '))
        suma(numero1, numero2)
    elif opcion == 2:
        limpiar_pantalla()
        print("------------------")
        print("OPERACION DE RESTA")
        print("------------------\n")
        numero1 = float(input('Ingrese un número: '))
        numero2 = float(input('Ingrese otro número: '))
        resta(numero1, numero2)
    elif opcion == 3:
        limpiar_pantalla()
        print("---------------------------")
        print("OPERACION DE MULTIPLICACION")
        print("---------------------------\n")
        numero1 = float(input('Ingrese un número: '))
        numero2 = float(input('Ingrese otro número: '))
        multiplicacion(numero1, numero2)
    elif opcion == 4:
        limpiar_pantalla()
        print("---------------------")
        print("OPERACION DE DIVISION")
        print("---------------------\n")
        numero1 = float(input('Ingrese un número: '))
        numero2 = float(input('Ingrese otro número: '))
        division(numero1, numero2)
    elif opcion == 5:
        limpiar_pantalla()
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor ingrese una opción del 1 al 5.")
        pausa()