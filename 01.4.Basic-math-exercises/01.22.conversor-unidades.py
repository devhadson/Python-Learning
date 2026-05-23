## Ejercicios matemáticos básicos
# 22. **Calculadora de IMC** - Calcula el Índice de Masa Corporal con peso y altura

peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = peso / (altura * altura)
print(f"Tu IMC es: {imc:.2f}")