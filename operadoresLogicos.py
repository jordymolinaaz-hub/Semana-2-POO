# Solicitar datos al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Operadores aritméticos
suma = num1 + num2
multiplicacion = num1 * num2

print("El resultado de la suma es:", suma)
print("El resultado de la multiplicación es:", multiplicacion)

# Operadores relacionales
menor = num1 < num2
igual = num1 == num2

print("¿El número 1 es menor al número 2?:", menor)
print("¿El número 1 es igual al número 2?:", igual)

# Operadores lógicos
if menor and not igual:
    print("num1 es menor y diferente de num2")

if menor or igual:
    print("num1 es menor o igual a num2")
