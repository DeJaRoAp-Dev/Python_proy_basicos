import random


def adivina_el_numero_computadora(x):
    print("==============================")
    print("== ¡Bienvenido(a) al juego! ==")
    print("==============================")
    print(f"Seleciona un numero entre 1 y {x} para que la computadora adivinarlo...!")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar prediccion
        if limite_inferior != limite_superior:  # Ejemplo[1-15]
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior  # tambien podria ser el limite superior.

            # Obtener respuesta del usuario

        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A)."
                          f" Si es muy baja, ingresa (B)."
                          f" Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":  # Intervalo inicial: [1, 10]
            limite_superior = prediccion - 1  # Prediccion: 6
        elif respuesta == "b":  # Respuesta:"a"
            limite_inferior = prediccion + 1  # intervalo: [1, 5]

    print(f"¡Siii! La computadora adivino tu numero correctamente: {prediccion} ")


adivina_el_numero_computadora(10)
