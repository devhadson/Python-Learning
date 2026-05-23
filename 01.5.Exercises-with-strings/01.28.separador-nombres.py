## Ejercicios con strings
# 28. **Separador de nombres** - Divide un nombre completo usando split() para extraer nombre y apellido

nombre_completo = input("Nombre completo: ")
partes = nombre_completo.split()
print("Nombre:", partes[0])
print("Apellido:", partes[-1])