# Entero
edad = int(input("Ingresa tu edad: "))
nueva_edad = edad + 5
print("Tu edad en 5 años es", nueva_edad , "años")

# Flotante
estatura = float(input("Ingresa tu estatura en cm: "))
nueva_estatura = estatura * 2
print("Tu nueva estatura doblada es", nueva_estatura, "cm")

# Cadena de Texto
nombre = input("Ingrese su nombre y su apellido: ")

# Booleano y verificación de edad
es_estudiante = input("¿Eres estudiante? (si/no): ").lower()

if es_estudiante == "si" or edad >= 18:
    print("Puede pasar")
else:
    print("NO puede pasar")

