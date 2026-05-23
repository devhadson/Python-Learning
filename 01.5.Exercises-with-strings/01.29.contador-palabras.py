## Ejercicios con strings
# 29. **Contador de palabras** - Cuenta cuántas palabras tiene una frase separándolas por espacios

frase = input("Escribe una frase: ")
palabras = frase.split()
print(f"Tu frase tiene {len(palabras)} palabras")