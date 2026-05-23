## Ejercicios de interacción básica
# 19. **Saludo personalizado** - Personaliza el saludo según la hora del día (mañana/tarde/noche)

nombre = input("¿Cómo te llamas? ")
hora = int(input("¿Qué hora es? (0-23): "))
if hora < 12:
    saludo = "Buenos días"
elif hora < 20:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"
print(f"{saludo}, {nombre}!")