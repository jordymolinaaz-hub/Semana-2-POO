def sumarHasta(numero):
    suma = 0
    contador = 1
    while contador <= numero:
        suma += contador
        contador += 1
    return suma

# Paso 1: Pedir al usuario que ingrese un número
numero_ingresado = int(input("Ingresa un número entero positivo: "))

# Paso 2: Llamar a la función con el número ingresado
resultado = sumarHasta(numero_ingresado)

# Paso 3: Mostrar el resultado
print(f"La suma de los números del 1 al {numero_ingresado} es: {resultado}")