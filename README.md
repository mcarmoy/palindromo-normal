# 🔄 Ejercicio: Detector de Palíndromos

Este proyecto consiste en un script de Python diseñado para identificar si una palabra o frase es un palíndromo (se lee igual en ambos sentidos). El desarrollo se ha realizado siguiendo buenas prácticas de control de versiones con Git.

## 📝 Lógica del Código

Para este ejercicio, se utilizó la técnica de **acumulación en cadena vacía**, que es la forma más didáctica de entender cómo manipular strings:

1.  **Entrada de datos:** Se utiliza `input()` para recibir el texto del usuario.
2.  **Limpieza:** Se aplica `.lower()` (minúsculas) y `.replace(" ", "")` (quitar espacios) para que la comparación sea precisa.
3.  **Inversión manual:** Se recorre la palabra con un bucle `for` y se construye la versión invertida sumando cada letra al inicio de una variable vacía.
4.  **Validación:** Se comparan ambas cadenas para dar un resultado.

```python
palabra = input("Introduce una palabra: ").lower().replace(" ", "")
palabra_invertida = ""

for letra in palabra:
    palabra_invertida = letra + palabra_invertida

if palabra == palabra_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")