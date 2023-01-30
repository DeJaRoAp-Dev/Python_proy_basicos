# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga :
# Aprende a Programar con ___________.

#organizacion = "Primer Proyecto Python"

#print("Aprende a programar con " + organizacion)
#print("Aprende a programar con {}".format(organizacion))
#print(f"Aprende a programar con {organizacion}") # f-string

# Map libs (Historias Locas)
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta" \
         f" {verbo1} problemas. ¡Aprende a {verbo2} con Frecodecamp y alcanza tus" \
         f" {sustantivo_plural}!"

print(madlib)