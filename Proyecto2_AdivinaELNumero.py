import random


def adivina_el_numero(x):
    print("==============================")
    print("== ¡Bienvenido(a) al Juego! ==")
    print("==============================")
    print("Tu meta es adivinar el numero aleatorio generado por la computadora.")

    # random lanza un numero aleatorio
    # randint hace que el numero aleatorio sea entero
    numero_aleatorio = random.randint(1, x)  # numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio :
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x} : ")) # f-tring

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande.")
    print(f"¡Felicitaaciones! adivinaste el numero {numero_aleatorio} ")


adivina_el_numero(10)
