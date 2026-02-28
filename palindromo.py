# Solicitamos la palabra al usuario
palabra = input("Introduce una palabra o frase: ").lower().replace(" ", "")
palabra_invertida = ""

# Lógica de construcción carácter por carácter
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

# Verificación
if palabra == palabra_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")