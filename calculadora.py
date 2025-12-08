#calculadorapr
# print("Calculadora basica Python")

# num1 = float(input("Ingrese el primer numero "))
# num2 = float(input("Ingrese el segundo numero "))

# print("1.-Suma ")
# print("2.-Resta ")
# print("3.-Multiplicacion ")
# print("4.-Divicion ")

# opciones = input("Ingrese un numero del (1/2/3/4) ")

# if opciones == "1":
#     resultado = num1 + num2
#     print(f"El resultado de la suma es: {resultado}")
# elif opciones == "2":
#     resultado = num1 - num2
#     print(f"El resultado de la resta es: {resultado}")
# elif opciones == "3":
#     resultado = num1 * num2
#     print(f"El resultado de la multiplicacion es: {resultado}")
# elif opciones== "4":
#     if num2!= 0:
#         resultado = num1 / num2
#         print(f"El resultado de la divicion es: {resultado}")
#     else:
#         print("No se puede multiplicar entre 0 ")

#nunero impar par
# numero = int(input("Ingrese un numero "))

# if numero%2== 0:
#     print("el numero es par")
# else:
#     print("El nunero es impar")


#Adivinaza
# import random

# numero_secreto = random.randint(1, 100)
# intentos = 0


# while True:
#     intentos = int(input("Ingrese un numero "))
#     intentos += 1

#     if intentos == numero_secreto:
#         print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
#         break

#     elif intentos < numero_secreto:
       
#         print("maas alto ")

#     else:
#         print("mas bajo ")


# import random

# opciones = ["piedra", "papel", "tijera"]
# victorias_usuario = 0
# victorias_computadora = 0

# print("¡Juego de Piedra, Papel o Tijera!")

# while True:
#     # 1. Usuario elige
#     print("\nOpciones: piedra, papel, tijera")
#     usuario = input("Tu elección (o 'salir'): ").lower()
    
#     if usuario == "salir":
#         break
    
#     # 2. Computadora elige
#     computadora = random.choice(opciones)
    
#     # 3. Mostrar elecciones
#     print(f"Tu elección: {usuario}")
#     print(f"Computadora eligió: {computadora}")
    
#     # 4. Determinar ganador
#     if usuario == computadora:
#         print("¡Empate!")
#     elif (usuario == "piedra" and computadora == "tijera") or \
#          (usuario == "papel" and computadora == "piedra") or \
#          (usuario == "tijera" and computadora == "papel"):
#         print("¡Ganaste!")
#         victorias_usuario += 1
#     else:
#         print("Perdiste")
#         victorias_computadora += 1
    
#     # 5. Mostrar marcador
#     print(f"Marcador - Tú: {victorias_usuario} | Computadora: {victorias_computadora}")

# # Al salir
# print(f"\n¡Juego terminado!")
# print(f"Resultado final - Tú: {victorias_usuario} | Computadora: {victorias_computadora}")


# tareas = []

# while True:
#     print("\n--- GESTOR DE TAREAS ---")
#     print("1. Agregar tarea")
#     print("2. Ver tareas")
#     print("3. Eliminar tarea")
#     print("4. Salir")
    
#     opcion = input("Elige una opción: ")
    
#     if opcion == "1":
#         nueva_tarea = input("Ingresa la tarea ")
#         tareas.append(nueva_tarea)
#         print(f"tarea {nueva_tarea}  sido agregada")

#     elif opcion == "2":
#         if len(tareas) == 0:
#             print("No hay tareas")
#         else:
#             print("Tareas:")
#         for i in range(len(tareas)):
#             print(f"{i+1}. {tareas[i]}")
        
#     elif opcion == "3":
#         if tareas:
#         # Mostrar tareas con números
#             for i in range(len(tareas)):
#              print(f"{i+1}. {tareas[i]}")
        
#         # Pedir número a eliminar
#         num = int(input("¿Qué tarea eliminar? "))
#         tareas.pop(num - 1)  # Elimina (restamos 1 porque las listas empiezan en 0)
#         print("Tarea eliminada")
#     else:
#         print("No hay tareas para eliminar")




#Ejercicio for
# ========================================
# EJERCICIO 1: For básico con range()
# ========================================
# range(5) genera números del 0 al 4

# print("Imprimiendo números del 0 al 4:")
# for i in range(8):
#     print(f"Número: {i}")

# print("\n" + "-" * 40)

# nombres = ["Omar" , "Andi",  "Adelmo", "Joahana"]

# print("Recorredor de nombres ")

# for nombre in nombres:
#     print(f"Nombres:  {nombre}")

# frutas = ["Manzana", "Pera", "Uva", "Babana"]

# for i in range(len(frutas)):
#     print(f"{i+1} {frutas[i]}")


# colores = ["Rojo",  "Negro", "Azul", "Verde"]

# for indice, color in enumerate(colores, start=1):
#     print(f"{indice} Color {color}" )

#EJERCICIO 5: For con Condiciones (if)
# numeros = [0,3,4,5,6,7,12,12,9]

# for num in numeros:
#     if num >=7 and num <=12:
#         print(num) 

#EJJERCICIO 6 

# Perro = 0
# Loro = 0
# oro = 0
# animales = ["Perro", "iguaba", "serpiente", "Perro", "Oro", "Loro"]

# for animal in animales:
#     if animal == "Perro":
#         Perro += 1
#     elif animal == "Loro":
#         Loro += 1
#     elif animal == "oro":
#         Loro += 1
        
        
# print(f"cantidad de Perros: {Perro}")
# print(f"cantidad de Loros: {Loro}")
# print(f"cantidad de Oro: {oro}")

#EJERCICIO 7 suma de valores

# precios = {10.56, 12.67, 7}
# total = 0
# for precio in precios:
#     total += precio
#     print(f"El precio es {precio} || Total acumulado {total}")
# print(f"El total es: {total}")

# precios = {10.56, 12.67, 7}
# total = 0
# for  precio in precios:
#     if precio > 10:
#         total += precio
#         print(f"Solo precios mayores a 10 {total}")

#EJERCICIO 8 Break

# numeros = [1,6,8,3,4,5,12,7,8,3,9]
# for num in numeros:
#     print(f"revisando {num}")
#     if num == 3:
#         print("Encontradoooo saliendoooo..........")
#         break
#     print("Buscando el numero ")
# print("fin del programa")
    
# numeros = [1,6,8,3,4,5,12,7,8,3,9]
# for num in numeros:
#     if num > 10:
#         print(f"encontre el primer nuimero mayor a 10 y es {num}")
#         break


# Nombres = {"Maria", "Omar", "Alx", "Kevin"}

# buscar = "Omar"
# encontrado = False

# for nombre in Nombres:
#     if nombre == buscar:
#         print(f"Listo encontrado {nombre} ")
#         encontrado = True
#         break
# if not encontrado:
#     print(f"El nombre {nombre} no esta ")


# Verificar si hay números negativos

# numeros_negativos = False

# numeros = [2, 5, 8, 9, 6]

# for numero in numeros:
#     if numero < 0:
#         print(f"si hay numeros y son los {numero}")
#         numeros_negativos = True
#         break
# else: 
#     print("No hay numeros negativos")

# CON CONTINUE (SALTA esa vuelta)
# print("Con CONTINUE:")
# for num in [1,4,5,6,7,8]:
#     if num == 4:
#         continue
#     print(num)
# print("FIN")

#Multiplos de 5

# for numero in range(1,24):
#     if numero %5 == 0:
#         continue
#     print(numero)

#Letras 
# Nombres = ["Angel", "Omar", "kevin", "Arlet"]
# for letras in Nombres:
#     if letras[0] == "A":
#         continue
#     print(letras)

# print("FIN")


# numeros = [1,5,-4,7,-7]
# suma = 0

# for numero in numeros:
#     if numero <0:
#         continue
#     suma += numero
# print(suma)


#Ejerccios finales 
# frutas = ["manzana" , "Ovo", "perra", "aguacate"]

# for i in range(len(frutas)):
#     print(f"{i+1}. {frutas[i]}")
    

# estudiantes = ["Carlos", "Laura", "Miguel", "Sofia", "Ana"]
# calificaciones = [85, 92, 78, 95, 88]

# while True:
#     print("===========Sistemas de estudiantes===========")
#     print("1.- Ver todos los estudiantes")
#     print("2.- Ver estudiantes con calificacion ")
#     print("3.- Buscar estudiante")
#     print("4.- Calcular promedio")
#     print("5.- Estudiantes aprobados")
#     print("6.- Salir")

#     print("===============================")

#     opcion = input("\n Elige un numeros de las opciones disponibles (1-6) ")

#     if opcion == "1":
#         print("Lista de estudiantes")
#         for estudiante in estudiantes:
#             print(f" o -{estudiante}")

#     elif opcion == "2":
#         print("Lista de estudiantes con calificaciones ")
#         for i in range(len(estudiantes)):
#             print(f"{i+1} {estudiantes[i]} {calificaciones[i]}")

#     elif opcion == "3":
#         print("Busca el nombre ")
#         buscar = input("Ingrese un nombre para ver si se encuentra en la lista de estudiantes ").strip()
#         encontrado = False
#         for i in range(len(estudiantes)):
#             if estudiantes[i].lower() == buscar.lower():
#                 print(f"✓ {estudiantes[i]} está en la lista")
#                 print(f"  Calificación: {calificaciones[i]} puntos")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print(f"no se encuentra en la lista {buscar}")
        
#     elif opcion == "4":
#         suma = 0
#         for calificacion in calificaciones:
#             suma += calificacion
#         promedio = suma / len(calificaciones)
#         print(f"promedio general {promedio:.2f}")

#     elif opcion== "5":
#         contador = 0

#         for i in range(len(estudiantes)):
#             if calificaciones[i] >= 80:
#                 print(f"o {estudiantes[i]} : {calificaciones[i]}")
#                 contador += 1
#         print(f"total de aprobados {contador} de {len(estudiantes)}")

#     elif opcion == "6":
#         print("saliendo del programa.............")
#         break
#     else:
#         print("Ingrese una opcion valida ")


#Ejercicio reto

# numeros = [4, 9, 2, 10, 3]

# mayor = numeros[0]
# for numero in numeros:
#     if numero > mayor:
#         mayor = numero
        
# print(f"El numero meyor es {mayor}")


# mayor = max(numeros)
# print(f"El numero mayor es  {mayor}")
# numeros = [4, 9, 2, 10, 3]
# numeros.remove(9)
# print(numeros)


# print("========== GESTOR DE TAREAS ==========")
# tareas = []

# while True:
#     print("1. Ver todas las tareas")
#     print("2. Agregar tarea al final (append)")
#     print("3. Agregar tarea en posición (insert)")
#     print("4. Modificar una tarea")
#     print("5. Eliminar por nombre (remove)")
#     print("6. Eliminar por posición (pop)")
#     print("7. Buscar tarea")
#     print("8. Contar tareas")
#     print("9. Limpiar todas (clear)")
#     print("10. Salir")
    
#     opcion = input("\nElige opción (1-10): ")
#     if opcion == "1":
#         if len(tareas) == 0:
#             print("No hay tareas")
#         else:
#             print("tareas disponibles")
#             for i in range(len(tareas)):
#                 print(f"{i+1} - {tareas[i]}")
#     elif opcion == "2":
#         agregar_tareas = input("Agrega una tarea ")
#         tareas.append(agregar_tareas)
#         print(f"{agregar_tareas} Se agregado correctamete ")
  
#         print("\n Lista actualizada")
#         for i in range(len(tareas)):
#             print(f"{i+1} - {tareas[i]}")
#     elif opcion == "3":
#         nombre_tarea = input("Ingresa el numbre de la tarea ")
#         posicion = int(input("¿En qué posición? (1, 2, 3...): "))

#         tareas.insert(posicion-1, nombre_tarea)

#         print(f"la tarea {nombre_tarea} se agrego en la posicion {posicion}")

#         print("\n Lista actualizada")
#         for i in range(len(tareas)):
#             print(f"{i+1} - {tareas[i]}")
#     elif opcion == "4":
#         print("\nLista de tareas:")
#         for i in range(len(tareas)):
#                 print(f"{i+1} - {tareas[i]}")

#         posicion = int(input("\n¿En qué posición está la tarea que quieres modificar? (1, 2, 3...): "))
#         nuevo_texto = input("Ingresa el numbre de la tarea ")
#         tareas[posicion-1] = nuevo_texto

#         print("\n Lista actualizada")
#         for i in range(len(tareas)):
#             print(f"{i+1} - {tareas[i]}")
    
#     elif  opcion == "5":
#         if len(tareas) == 0:
#             print("No hay tareas para eliminar.")
#         else:
#             print("\nLista de tareas:")
#             for i in range(len(tareas)):
#                 print(f"{i+1} - {tareas[i]}")
#             nombre = input("Nombre exacto de la tarea que deseas eliminar ")
        
#             try:
#                 tareas.remove(nombre)
#                 print(f"\n✓ La tarea '{nombre}' fue eliminada correctamente.")
#             except ValueError:
#                 print(f"No se encuentra en la lista {nombre}")

#         print("\n Lista actualizada")
#         for i in range(len(tareas)):
#             print(f"{i+1} - {tareas[i]}")
        
#     elif opcion == "6":
#         if len(tareas) == 0:
#             print("No hay tareas para eliminar.")
#         else:
#             print("\nLista de tareas:")
#             for i in range(len(tareas)):
#                 print(f"{i+1} - {tareas[i]}")

#             try:
#                 posicion = int(input("\n¿Qué tarea eliminar? (número): "))
#                 if 1<= posicion <= len(tareas):
#                     eliminada = tareas.pop(posicion -1)
#                     print(f"La tarea {eliminada} fue eliminda correctamente")

#                     if len(tareas) > 0:
#                         print("\n Lista actualizada")
#                         for i in range(len(tareas)):
#                             print(f"{i+1} - {tareas[i]}")
#                     else:
#                         print("lista vacia")
#                 else:
#                     print(f"Posicion ivalida. debe ser de 1 a {len(tareas)} ")
#             except ValueError:
#                 print("Debes ingresar un numero valido ")

#     elif opcion == "7":
#         if len(tareas) == 0:
#             print("No hay tareas.")
#         else:
#             print("\nLista de tareas:")
#             for i in range(len(tareas)):
#                 print(f"{i+1} - {tareas[i]}")
        
#         buscar = input("Que tareas buscas una tarea").strip()
#         tarea_encontrada = False
#         for i in range(len(tareas)):
#             if tareas[i].lower() == buscar.lower():
#                 print(f"{tareas[i]} Esta en la posicion {i+1}")
#                 tarea_encontrada = True
#                 break
#         if not tarea_encontrada:
#             print(f"{buscar} no esta en la lista ")
    
#     elif opcion== "8":
#         print(f"Total de tareas {len(tareas)}")
#     elif opcion == "9":
#         if len(tareas) == 0:
#             print("No hay tareas.")

#         confirmacion = input("Seguro que deseas eliminar todas las tareas? (si/no)").strip().lower()
#         if confirmacion == "Si" or confirmacion == "s":
#             tareas.clear()
#             print("Todas las tareas a sido eliminadas ")
#         else:
#             print("cancelado")
#     elif opcion == "10":
#         print("="*40)
#         print("Saliendo del programa...............")
#         print("="*40)
#         print(f"Total de tareas al momento de salir {len(tareas)}")
#         if len(tareas) > 0:
#             print("Tareas pendientes")
#             for i in range(len(tareas)):
#                 print(f"{i+1} {tareas[i]} ")
#         else:
#             print(f"No hay tareas pendientes {len(tareas)}")
#             print("Hasta Luego")
#         break

        


# productos = []
# precios = []
# while True:
#     print("========== INVENTARIO DE TIENDA ==========")
#     print("1. Ver inventario completo")
#     print("2. Agregar producto")
#     print("3. Modificar precio de un producto")
#     print("4. Eliminar producto")
#     print("5. Buscar producto")
#     print("6. Producto más caro")
#     print("7. Producto más barato")
#     print("8. Calcular total del inventario")
#     print("9. Aplicar descuento a todos los productos")
#     print("10. Salir")

#     opcion = input("Selecione un opcion del (1-10) ")
#     if opcion == "1":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("Inventario actualizado")
#             for i in range(len(productos)) :
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#     elif opcion == "2":
#         producto = input("Ingrese un producto al inventario ")
#         precio = float(input("Ingrese el precio "))

#         productos.append(producto)
#         precios.append(precio)
#         print(f"El producto {producto} con el {precio} se agregaron correctamente")
#         print("Lista actualiza")
#         for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#     elif opcion == "3":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#         pocicion = int(input("En que posion deseas modificar? (1,2,3,4.........)"))
#         nuevo_precio = float(input("Ingresa el precio qe deseas modificar "))

#         precios[pocicion-1] = nuevo_precio
#         print("Lista actualiza")
#         for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")

#     elif opcion == "4":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#         producto_eliminar = int(input("Ingresa el producto que deseas eliminar (1,2,3,4.........)"))

#         producto_borrado = productos.pop(producto_eliminar -1)
#         precio_borrado = precios.pop(producto_eliminar -1)

#         print(f"El producto {producto_borrado} con {precio_borrado} se eliminado correctamente")
        
#         print("Lista actualiza")
#         for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#     elif opcion == "5":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#         buscar_nombre = input("Ingresa el nombre que deseas buscar ").strip().lower()
#         encontrado = False
#         for i in range(len(productos)):
#             if productos[i].lower() == buscar_nombre.lower():
#                 print(f"Si existe {productos[i]} {precios[i]} y esta en la posicion {i+1} ")
#                 encontrado = True
#                 break
#         if not encontrado:
#              print(f"El producto {buscar_nombre} no se encuentra ")
#     elif opcion == "6":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#             maximo = max(precios)
#             indice_maximo = precios.index(maximo)
#             print("\nEl producto mas caro es:")
#             print(f"{productos[indice_maximo]} -${maximo}")
#     elif opcion == "7":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#             minimo = min(precios)
#             indice_minimo = precios.index(minimo)
#             print("\nEl producto menos caro es:")
#             print(f"{productos[indice_minimo]} -${minimo}")
#     elif opcion == "8":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#             total = 0
#             for precio in precios:
#                 total +=  precio
                
#                 print(f"Cantidad de productos {len(productos)}")
#                 print(f"Precio total del inventario: ${total:.2f}")
#     elif opcion == "9":
#         if len(productos) == 0:
#             print("No hay productos")
#         else:
#             print("==================Inventario=================")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#             descuento = float(input("Ingrese el descuento: "))
#             for i in range(len(precios)):
#                 precios[i] = precios[i] * (1 - descuento/100)
#             print("Lista actualiza con el descuento aplicado ")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]:.2f}")
#     elif opcion == "10":
#         print("="*40)
#         print("SALIENDO DEL PROGRAMA.................")
#         print(f"Total de productos al momento de salir {len(productos)}")
#         if len(productos) > 0:
#             print("\nProductos registrados")
#             for i in range(len(productos)):
#                 print(f"{i+1} {productos[i]} - {precios[i]}")
#         else:
#             print(f"No se registraron productos  ")
#         print("Hasta luego")
#         break



# titulos = []
# autores = []
# años = []

# while True:
#     print("="*50)
#     print("       📚 SISTEMA DE BIBLIOTECA 📚")
#     print("="*50)
#     print("1. Ver catálogo completo")
#     print("2. Agregar libro")
#     print("3. Modificar año de publicación")
#     print("4. Eliminar libro")
#     print("5. Buscar libro por título")
#     print("6. Libro más antiguo")
#     print("7. Libro más reciente")
#     print("8. Contar libros por autor")
#     print("9. Aplicar descuento de años (libros usados)")
#     print("10. Salir")
#     print("="*50)
    
#     opcion = input("Seleciones una opcion del (1-10)")

#     if opcion == "1":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
#     elif opcion == "2":
#         titulo = input("Ingresa un titulo de un libro ")
#         nombre = input("Ingresa el nombre de un autor ")
#         año = int(input("Ingresa el año de publicacion "))
        
#         titulos.append(titulo)
#         autores.append(nombre)
#         años.append(año)
#         print(f"Se a añadido coorectame el titulo del libro de {titulo} con su autor {nombre} y fue publicado el {año}")

#         print("Lista actualiza del sistema de biblioteca ")
#         for i in range(len(titulos)):
#                 print(f"{i+1}. {titulos[i]} - {autores[i]} {(años[i])}")
#     elif opcion == "3":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)): 
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
#             posicion = int(input("Ingresa la pocision del libro que deseas modificar (1,2,3,4..........) "))
#             año_nuevo = int(input("ingresa el nuevo año que deseas modificar "))
#             años[posicion -1] = año_nuevo

#         print("Lista actualiza del sistema de biblioteca ")
#         for i in range(len(titulos)):
#                 print(f"{i+1}.{titulos[i]} - {autores[i]} {(años[i])}")
#     elif opcion == "4":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
#             posicion = int(input("Ingresa la pocision del libro que deseas eliminar (1,2,3,4..........) "))
#             titulo_eliminado = titulos.pop(posicion -1)
#             autores_eliminado = autores.pop(posicion -1)
#             años_eliminados = años.pop(posicion -1)

#             print(f"\n Libro eliminado {titulo_eliminado} - {autores_eliminado} {años_eliminados}")
            
#             print(f"=====Catalogo actualizado======")
#             if len(titulos) == 0:
#                  print("No quedan libros en el catologo ")
#             else:
#                 for i in range(len(titulos)):
#                     print(f"{i+1}.{titulos[i]} - {autores[i]} {(años[i])}")
#     elif opcion == "5":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")

#             buscar_libro = input("Ingresa el titulo que deseas buscar ").strip().lower()
#             encontrado = False
#             for i in range(len(titulos)):
#                 if titulos[i].lower() == buscar_libro.lower():
#                     print(f"Se encontro el siguiente libro {titulos[i]} _ {autores[i]} {años[i]} que estaba en la pocision {i+1}")
#                     encontrado = True
#                     break
#             if not encontrado:
#                 print("No se encontro el libro ")
#     elif opcion == "6":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
            
#             año_minimo = min(años)
#             indice_minimo = años.index(año_minimo)
#             print("\nEl libro mas antiguo es: ")
#             print(f"{titulos[indice_minimo]} - {autores[indice_minimo]} {año_minimo}")
#     elif opcion == "7":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
            
#             año_maximo = max(años)
#             indice_maximo = años.index(año_maximo)
#             print("\nEl libro mas reciente es: ")
#             print(f"{titulos[indice_maximo]} - {autores[indice_maximo]} {año_maximo}")
#     elif opcion == "8":
#         if len(titulos) == 0:
#             print("No hay libros")
#         else:
#             print("SISTEMA DE LA BIBLIOTECA")
#             for i in range(len(titulos)):
#                 print(f"{i+1} .{titulos[i]} - {autores[i]} {(años[i])}")
            
#             nombre_autor = input("Ingresa el nombre del autor ").lower().strip()
#             contador = 0
#             for autor in autores:
#                 if autor.lower() == nombre_autor.lower():
#                     contador +=1
#             if contador > 0:
#                 print(f"\nEl autor {nombre_autor} tiene {contador} libros ")
#             else:
#                 print(f"\nNo se encontraron libros de {nombre_autor}")
#     elif opcion == "9":
#         if len(titulos) == 0:
#          print("No hay libros")
#         else:
#             print("========== SISTEMA DE LA BIBLIOTECA ==========")
#             for i in range(len(titulos)):
#                 print(f"{i+1}. {titulos[i]} - {autores[i]} ({años[i]})")
        
#             descuento = int(input("\n¿Cuántos años deseas restar? "))
#             for i in range(len(años)):
#                 años[i] = años[i] - descuento
#                 print("\n===== Catálogo actualizado =====")
#             for i in range(len(titulos)):
#                 print(f"{i+1}. {titulos[i]} - {autores[i]} ({años[i]})")
        
#     elif opcion == "10":
#         print("="*50)
#         print("SALIENDO DEL SISTEMA DE BIBLIOTECA...")
#         print("="*50)
#         print(f"\nTotal de libros registrados: {len(titulos)}")
    
#         if len(titulos) > 0:
#             print("\n📚 Libros en el catálogo:")
#         for i in range(len(titulos)):
#             print(f"{i+1}. {titulos[i]} - {autores[i]} ({años[i]})")
#         else:
#             print("No se registraron libros en el sistema")
    
#         print("\n¡Hasta luego! 👋")
#         break


#Funciones
# numeros = [3,6,7,8,12,9]

# def encontra_mayor(numeros):
#    mayor = numeros[0]
#    for numero in numeros:
#       if numero > mayor:
#         mayor = numero
   
#    return mayor
# resultado = encontra_mayor(numeros)
# print(f"El numero mayor es: {resultado}")

# # Ejemplo:
# # numeros = [3, 7, 2, 9, 1, 5]
# # mayor = encontrar_mayor(numeros)
# # print(mayor)  # 9
# # Crea una función contar_pares(numeros) que cuente cuántos números son pares

#EJERCICIO 2 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# def contar_pares(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero %2 == 0:
#             contador += 1
#     return contador
# resultado = contar_pares(numeros)
# print(f"hay {resultado} numeros pares ")
      # Ejemplo:


# Crea una función filtrar_mayores(numeros, limite) que devuelva una lista
# con solo los números mayores al límite


# numeros = [5, 12, 3, 18, 7, 20]

# def filtrar_mayores(numeros, limite):
#     resultado = []
#     for numero in numeros:
#         if numero > limite :
#             resultado.append(numero)
#     return resultado
# filtrados = filtrar_mayores(numeros, 10)
# print(filtrados)
    
# Crea una función multiplicar_lista(numeros) que multiplique todos los elementos

# Ejemplo:
# numeros = [2, 3, 4]
# numeros2 = [5, 2, 3]
# def multiplicar_lista(numeros):
#     resultado = 1
#     for numero in numeros:
#         resultado *= numero
#     return resultado
# multi = multiplicar_lista(numeros)
# multi2 = multiplicar_lista(numeros2)
# print(multi)
# print(multi2)

# Crea una función contar_vocales(palabra) que cuente cuántas vocales tiene
# vocales = "aeiouAEIOU"
# def contar_vocales(palabra):
#     contador = 0
#     for letra in palabra:
#         if letra.lower() in vocales.lower():
#             contador += 1
#     return contador

# print(contar_vocales("vvaCA"))

# nombres = ["Ana", "Luis", "Carlos"]

# def invertir_lista(lista):
#     invertida = []
#     for i in range(len(lista)-1,-1,-1):
#         invertida.append(lista[i])
#     return invertida

# print(invertir_lista(nombres))

# numeros = [1, 2, 3, 4, 5]
# def invertir_numeros(lista):
#     invertida = []
#     for i in range(len(lista)-1,-1,-1):
#         invertida.append(lista[i])
#     return invertida
# print(invertir_numeros(numeros))



#Tabla de multiplicar

# def tabla_multiplicar(numero):
#     for i in range(1,11):
#         print(f"{numero} x {i} = {numero * i}")

# tabla_multiplicar(4)
# tabla_multiplicar(7)


# Crea una función calcular_promedio(numeros) que calcule el promedio
# notas = [8, 7, 9, 6, 10]
# def calcular_promedio(numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#         promedio = total / len(numeros)
#     return promedio

# print(calcular_promedio(notas))

   
# frutas = ["banana", "pera", "manzana"]
# def buscar_palabra(lista, palabra):
#     for item in lista:
#         if item.lower() == palabra.lower():
#             return True  # Encontrada
#     return False  # No encontrada (después del for)

# print(buscar_palabra(frutas, "pera"))

# numeros = [2,7,8,9,]
# def buscar_numero(lista, numero):
#     for i in lista:
#         if i == numero:
#             return True
#     return False
# print(buscar_numero(numeros, 10))

# Crea las siguientes funciones:

# 1. agregar_nota(notas, nota) - Agrega una nota a la lista
# 2. calcular_promedio(notas) - Calcula el promedio
# 3. nota_mas_alta(notas) - Encuentra la nota más alta
# 4. nota_mas_baja(notas) - Encuentra la nota más baja
# 5. contar_aprobados(notas) - Cuenta cuántas notas son >= 7`
# notas = []
# def agregar_notas(notas, nota):
#     notas.append(nota)
#     print(f"Nota {nota} agregada correctamente")

# def calcular_promedio(notas):
#     total = 0
#     for nota in notas:
#         total += nota
#     promedio = total /len(notas)
#     return promedio

# def nota_alta(notas):
#     alta = max(notas)
#     return alta
# def nota_baja(notas):
#     baja = min(notas)
#     return baja

# def contar_aprobados(notas):
#     contador = 0
#     for nota in notas:
#         if nota >=7:
#             contador += 1
#     return contador



# while True:
#     print(" ========== SISTEMA DE NOTAS ==========")
#     print(" 1. Agregar nota")
#     print("2. Ver promedio")
#     print("3. Ver nota más alta")
#     print("4. Ver nota más baja")
#     print("5. Contar aprobados (>= 7)")
#     print("6. Ver todas las notas")
#     print("7.- Salir")

#     opcion = input("Ingresa una de las opciones (1-7)")

#     if opcion == "1":
#         nota = float(input(f"Ingresa la nota "))
#         agregar_notas(notas, nota)

#     elif opcion == "2":
#         if len(notas) ==  0:
#             print("No hay notas")
#         else:
#             promedio = calcular_promedio(notas)
#             print(f"El promedio es {promedio}")
#     elif opcion == "3":
#         if len(notas) ==  0:
#             print("No hay notas")
#         else:
#             alta = nota_alta(notas)
#             print(f"La nota mas alta es {alta}")

#     elif opcion == "4":
#         if len(notas) ==  0:
#             print("No hay notas")
#         else:
#             baja = nota_baja(notas)
#             print(f"La nota mas baja es {baja}")
#     elif opcion == "5":
#         if len(notas) ==  0:
#             print("No hay notas")
#         else:
#             aprovados = contar_aprobados(notas)
#             print(f"Estos son los sigunetes aprobados {aprovados}")
#     elif opcion == "6":
#         if len(notas) ==  0:
#             print("No hay notas")
#         else:
#             for i in range(len(notas)):
#                 print(f"{i+1} - {notas[i]}")
#     elif opcion == "7":
#         print(f"Total de notas registras {len(notas)}")
#         print("Hazta luego")
#         break



##LISTA DE COMPRAS

# productos = []  # ✅ Corregido

# def agregar_productos(lista, producto):
#     lista.append(producto)
#     print(f"✓ El producto '{producto}' se agregó correctamente")

# def eliminar_producto(lista, posicion):
#     producto_eliminado = lista.pop(posicion - 1)
#     print(f"✓ El producto '{producto_eliminado}' se eliminó correctamente")

# def buscar_productos(lista, nombre):
#     for producto in lista:
#         if producto.lower() == nombre.lower():
#             return True
#     return False

# def contar_productos(lista):
#     return len(lista)

# def vaciar_lista(lista):
#     lista.clear()  # ✅ Corregido
#     print("✓ Lista vaciada correctamente")

# while True:
#     print("\n========== LISTA DE COMPRAS ==========")
#     print("1. Agregar producto")
#     print("2. Ver lista completa")
#     print("3. Eliminar producto")
#     print("4. Buscar producto")
#     print("5. Vaciar lista")
#     print("6. Salir")
#     print("======================================")

#     opcion = input("Ingrese una opción (1-6): ")

#     if opcion == "1":
#         producto = input("Ingresa un producto: ")
#         agregar_productos(productos, producto)
    
#     elif opcion == "2":
#         if len(productos) == 0:
#             print("❌ No hay productos")
#         else:
#             print("\n===== LISTA DE COMPRAS =====")
#             for i in range(len(productos)):
#                 print(f"{i+1}. {productos[i]}")
#             print(f"\nTotal: {contar_productos(productos)} producto(s)")
    
#     elif opcion == "3":
#         if len(productos) == 0:
#             print("❌ No hay productos")
#         else:
#             print("\n===== PRODUCTOS =====")
#             for i in range(len(productos)):
#                 print(f"{i+1}. {productos[i]}")
#             posicion = int(input("\n¿En qué posición deseas eliminar? "))
#             eliminar_producto(productos, posicion)
    
#     elif opcion == "4":
#         nombre = input("¿Qué producto buscas? ")
#         if buscar_productos(productos, nombre):  # ✅ Corregido
#             print(f"✓ '{nombre}' se encuentra en la lista")  # ✅ Corregido
#         else:
#             print(f"✗ '{nombre}' no se encuentra en la lista")
    
#     elif opcion == "5":
#         if len(productos) == 0:
#             print("❌ No hay productos")
#         else:
#             confirmacion = input("¿Seguro que deseas vaciar la lista? (s/n): ")
#             if confirmacion.lower() == "s":
#                 vaciar_lista(productos)
    
#     elif opcion == "6":
#         print("\n======================================")
#         print(f"Total de productos: {contar_productos(productos)}")
#         print("¡Hasta luego! 🛒")
#         break
    
#     else:
#         print("⚠️ Ingrese un número válido (1-6)")

#Lista de peliculas favoritas

# peliculas = []

# def  agregar_peliculas(lista, pelicula):
#     lista.append(pelicula)
#     print(f"La pelicula {pelicula} se agrego correctamente " )
    
# def  eliminar_peliculas(lista , posicion):
#     pelicula_eliminada = lista.pop(posicion -1)
#     print(f"La pelicula {pelicula_eliminada} se elimino correctamente ")
# def buscar_pelicula(lista, nombre):
#     for pelicula in lista:
#         if pelicula.lower() == nombre.lower():
#             return True
#     return False

# def contar_peliculas(lista):
#     return len(lista)

# def vaciar_lista(lista):
#     lista.clear()
#     print(f"las peliculas se elminaron correctamente ")

# while True:
#     print("1. Agregar peliculas")
#     print("2.Eliminar peliculas")
#     print("3.Buscar peliculas")
#     print("4.contar peliculas")
#     print("5.Vaciar lista")
#     print("6.Salir")

#     opcion = input("Ingresa un numero (1-6) ")

#     if opcion == "1":
#         pelicula = input("Ingrese el nombre de la pelicula ")
#         agregar_peliculas(peliculas, pelicula)

#     elif opcion == "2":
#         if len(peliculas) == 0:
#             print("No hay peliculas")
#         else:
#             for i in range(len(peliculas)):
#                 print(f"{i+1} {peliculas[i]}")
#             posicion = int(input("Ingresa la posicion que deseas elminar"))
#             eliminar_peliculas(peliculas , posicion)
#     elif opcion == "3":
#         nombre = input("Que nombre de pelicula estas buscando ")
#         if buscar_pelicula(peliculas, nombre):
#             print(f"La pelicula si se encuentra")
#         else:
#             print("No se ecuentra la pelicula con ese nombre ")
#     elif opcion == "4":
#         total = contar_peliculas(peliculas)
#         print(f"El total peliculas {total}")
#     elif opcion == "5":
#         if len(peliculas) == 0:
#             print("No hay peliculas")
#         else:
#             confirmacion = input("seguro que deseas vaciar la lista (s/n)")
#             if confirmacion.lower() == "s":
#                 vaciar_lista(peliculas)
#     elif opcion == "6":
#         print("\n======================")
#         print(f"Total de productos {contar_peliculas(peliculas)}")
#         print("ADIOS")
#         break
#     else:
#         print("Ingres un numero valido (1-6)")
        

# canciones = []
# def agregar_cancion(lista, cancion):
#     lista.append(cancion)
#     print(f"La cancion {cancion} se agrego correctamente ")

# def eliminar_canciones(lista, posicion):
#     cancion_eliminada = lista.pop(posicion -1)
#     print(f"Se elimino {cancion_eliminada} correctamente ") 

# def buscar_cancion(lista, nombre):
#     for cancion in lista:
#         if cancion.lower() == nombre.lower():
#             return True
#     else:
#         return False
# def monstrar_playlist(lista):
#     if len(lista) == 0:
#         print("No hay canciones")
#     else:
#         for i in range(len(lista)):
#             print(f"{i+1} - {lista[i]}")
#             total = len(canciones)

#         print(f"El total de canciones es: {total}")
# def cancion_favorita(lista):
#     if len(lista) == 0:
#         print("No hay canciones")
#     else:
#         favorita = lista[0]
#         print(f"La cancion favorita es {favorita}")

# def vaciar_playlist(lista):
#     lista.clear()
#     print("La musicas se borraron corretamente")

# while True:
#     print("\n============MY PLAYLIST==============")
#     print("1.Agregar canciones")
#     print("2.Eliminar canciones")
#     print("3.Buscar canciones")
#     print("4.Mosntrar playlist")
#     print("5.Monstrar cancio favorita")
#     print("6.Limpiar mi playlist")
#     print("7.Salir")

#     opcion = input("Ingresa una opcion de (1-7)")

#     if opcion == "1":
#         cancion = input("Ingresa una cancion ")
#         agregar_cancion(canciones, cancion)
#     elif opcion == "2":
#         if len(canciones) == 0:
#             print("No hay canciones")
#         else:
#             for i in range(len(canciones)):
#                 print(f"{i+1} - {canciones[i]}")
#             pocision = int(input("Ingresa la posicion de la cancion que deseas elminar "))
#             eliminar_canciones(canciones, pocision)
#     elif opcion == "3":
#         buscar = input("ingresa la cancion que buscas ")
#         if buscar_cancion(canciones, buscar):
#             print("La cancion si se encuentra ")
#         else:
#             print("No se encuntra la cancion ") 
#     elif opcion == "4":
#         monstrar_playlist(canciones)
#     elif opcion == "5":
#         cancion_favorita(canciones)
#     elif opcion == "6":
#         if len(canciones) == 0:
#             print("No hay canciones")
#         else:
#             confirmacion = input("Seguro que de deseas eliminar la playlist (s/n)")
#             if confirmacion.lower() == "s":
#                 vaciar_playlist(canciones)
#     elif opcion == "7":
#         print("\n======================")
#         print(f"Total de musicas {len(canciones)}")
#         print("ADIOS")
#         break
#     else:
#         print("Ingres un numero valido (1-6)")

            


# contactos = []

# def agregar_contacto(lista, nombre, telefono, email):
#     contacto = {
#         "nombre": nombre,
#         "telefono": telefono,
#         "email": email
#     }
#     lista.append(contacto)
#     print(f"✓ Contacto '{nombre}' agregado correctamente")

# def mostrar_contactos(lista):
#     if len(lista) == 0:
#         print("❌ No hay contactos")
#     else:
#         print("\n===== MIS CO++NTACTOS =====")
#         for i in range(len(lista)):
#             print(f"\n{i+1}. Nombre: {lista[i]['nombre']}")  # ✅ Corregido
#             print(f"   Teléfono: {lista[i]['telefono']}")
#             print(f"   Email: {lista[i]['email']}")
#         total = len(lista)
#         print(f"\nTotal: {total} contacto(s) 📇")

# def buscar_contacto(lista, nombre):
#     for contacto in lista:
#         if contacto["nombre"].lower() == nombre.lower():  # ✅ Corregido
#             print(f"\n📇 Contacto encontrado:")
#             print(f"   Nombre: {contacto['nombre']}")
#             print(f"   Teléfono: {contacto['telefono']}")
#             print(f"   Email: {contacto['email']}")
#             return
#     print(f"✗ No se encontró el contacto '{nombre}'")

# def eliminar_contacto(lista, posicion):
#     contacto_eliminado = lista.pop(posicion - 1)
#     print(f"✓ Contacto '{contacto_eliminado['nombre']}' eliminado correctamente")

# def editar_contacto(lista, nombre, nuevo_contacto):
#     for contacto in lista:
#         if contacto["nombre"].lower() == nombre.lower():
#             contacto["telefono"] = nuevo_contacto
#             print(f"✓ El número de '{nombre}' se actualizó correctamente")
#             return
#     print(f"✗ No se encuentra el contacto '{nombre}'")

# def contar_contactos(lista):
#     return len(lista)  # ✅ Corregido

# while True:
#     print("\n========== MI AGENDA ==========")
#     print("1. Agregar contacto")
#     print("2. Ver todos los contactos")
#     print("3. Buscar contacto por nombre")
#     print("4. Eliminar contacto")
#     print("5. Editar teléfono de contacto")
#     print("6. Ver total de contactos")
#     print("7. Salir")
#     print("===============================")

#     opcion = input("Ingresa una opción (1-7): ")
    
#     if opcion == "1":
#         nombre = input("Ingresa el nombre: ")
#         telefono = input("Ingresa el teléfono: ")
#         email = input("Ingresa el email: ")
#         agregar_contacto(contactos, nombre, telefono, email)
    
#     elif opcion == "2":
#         mostrar_contactos(contactos)
    
#     elif opcion == "3":
#         nombre = input("¿Qué contacto buscas? ")
#         buscar_contacto(contactos, nombre)
    
#     elif opcion == "4":
#         if len(contactos) == 0:
#             print("❌ No hay contactos")
#         else:
#             print("\n===== MIS CONTACTOS =====")
#             for i in range(len(contactos)):
#                 print(f"{i+1}. {contactos[i]['nombre']} - {contactos[i]['telefono']}")
#             posicion = int(input("\n¿Qué contacto deseas eliminar? (número): "))
#             eliminar_contacto(contactos, posicion)
    
#     elif opcion == "5":
#         if len(contactos) == 0:
#             print("❌ No hay contactos")
#         else:
#             nombre = input("¿De qué contacto deseas editar el teléfono? ")
#             nuevo_telefono = input("Ingresa el nuevo teléfono: ")
#             editar_contacto(contactos, nombre, nuevo_telefono)
    
#     elif opcion == "6":
#         total = contar_contactos(contactos)
#         print(f"\n📊 Total de contactos: {total}")
    
#     elif opcion == "7":
#         print("\n===============================")
#         print(f"Total de contactos guardados: {contar_contactos(contactos)}")
#         print("¡Hasta luego! 📇")
#         break
    
#     else:
#         print("⚠️ Ingresa un número válido (1-7)")





# inventario = []

# def agregar_producto(lista, nombre, precio, cantidad):
#     producto = {
#         "nombre": nombre,
#         "precio": precio,
#         "cantidad": cantidad
#     }
#     lista.append(producto)
#     print(f"✓ Producto '{nombre}' se agregó correctamente")

# def mostrar_inventario(lista):
#     if len(lista) == 0:
#         print("❌ No hay nada en el inventario")
#     else:
#         print("\n=============INVENTARIO===============")
#         total_inventario = 0
        
#         for i in range(len(lista)):
#             nombre = lista[i]["nombre"]
#             precio = lista[i]["precio"]
#             cantidad = lista[i]["cantidad"]
#             subtotal = precio * cantidad

#             print(f"\n{i+1}. Producto: {nombre}")
#             print(f"   Precio: ${precio}")
#             print(f"   Cantidad: {cantidad}")
#             print(f"   Subtotal: ${subtotal}")

#             total_inventario += subtotal
        
#         print("\n==================================")
#         print(f"💰 Valor total del inventario: ${total_inventario}")
#         print(f"Total de productos: {len(lista)}")
            
# def buscar_producto(lista, nombre):
#     for producto in lista:
#         if producto['nombre'].lower() == nombre.lower():
#             print("\n📦 Producto encontrado:")
#             print(f"   Nombre: {producto['nombre']}")
#             print(f"   Precio: ${producto['precio']}")
#             print(f"   Stock: {producto['cantidad']} unidades")
#             return
    
#     print(f"✗ No se encuentra el producto '{nombre}'")

# def actualizar_stock(lista, nombre, nueva_cantidad):
#     for producto in lista:
#         if producto['nombre'].lower() == nombre.lower():
#             producto['cantidad'] = nueva_cantidad
#             print(f"✓ Stock de '{nombre}' actualizado a {nueva_cantidad} unidades")
#             return
    
#     print(f"✗ No se encuentra el producto '{nombre}'")

# def eliminar_producto(lista, posicion):
#     producto_eliminado = lista.pop(posicion - 1)
#     print(f"✓ El producto '{producto_eliminado['nombre']}' se eliminó correctamente")

# def productos_agotados(lista):
#     if len(lista) == 0:
#         print("❌ No hay nada en el inventario")
#         return
    
#     contador_agotados = 0
#     print("\n⚠️ PRODUCTOS AGOTADOS:")

#     for producto in lista:
#         if producto["cantidad"] == 0:
#             print(f"   • {producto['nombre']} - ${producto['precio']} (Stock: 0)")
#             contador_agotados += 1
    
#     if contador_agotados == 0:
#         print("   ✓ No hay productos agotados")

# def producto_mas_caro(lista):
#     if len(lista) == 0:
#         print("❌ No hay nada en el inventario")
#         return
    
#     mas_caro = lista[0]
#     for producto in lista:
#         if producto["precio"] > mas_caro["precio"]:
#             mas_caro = producto

#     print("\n💎 Producto más caro:")
#     print(f"   Nombre: {mas_caro['nombre']}")
#     print(f"   Precio: ${mas_caro['precio']}")
#     print(f"   Stock: {mas_caro['cantidad']} unidades")

# # ============ MENÚ PRINCIPAL ============

# while True:
#     print("\n========== INVENTARIO DE TIENDA ==========")
#     print("1. Agregar producto")
#     print("2. Ver todo el inventario")
#     print("3. Buscar producto")
#     print("4. Actualizar stock de producto")
#     print("5. Eliminar producto")
#     print("6. Ver productos agotados")
#     print("7. Ver producto más caro")
#     print("8. Salir")
#     print("==========================================")

#     opcion = input("Ingresa una opción (1-8): ")

#     if opcion == "1":
#         nombre = input("Ingresa el nombre del producto: ")
#         precio = float(input("Ingresa el precio: $"))
#         cantidad = int(input("Ingresa la cantidad en stock: "))
#         agregar_producto(inventario, nombre, precio, cantidad)
    
#     elif opcion == "2":
#         mostrar_inventario(inventario)
    
#     elif opcion == "3":
#         nombre = input("¿Qué producto buscas? ")
#         buscar_producto(inventario, nombre)
    
#     elif opcion == "4":
#         if len(inventario) == 0:
#             print("❌ No hay productos en el inventario")
#         else:
#             nombre = input("¿De qué producto deseas actualizar el stock? ")
#             nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
#             actualizar_stock(inventario, nombre, nueva_cantidad)
    
#     elif opcion == "5":
#         if len(inventario) == 0:
#             print("❌ No hay productos en el inventario")
#         else:
#             print("\n===== INVENTARIO =====")
#             for i in range(len(inventario)):
#                 print(f"{i+1}. {inventario[i]['nombre']} - ${inventario[i]['precio']}")
#             posicion = int(input("\n¿Qué producto deseas eliminar? (número): "))
#             eliminar_producto(inventario, posicion)
    
#     elif opcion == "6":
#         productos_agotados(inventario)
    
#     elif opcion == "7":
#         producto_mas_caro(inventario)
    
#     elif opcion == "8":
#         print("\n==========================================")
#         print(f"Total de productos en inventario: {len(inventario)}")
        
#         total_final = 0
#         for producto in inventario:
#             total_final += producto["precio"] * producto["cantidad"]
        
#         print(f"Valor total del inventario: ${total_final}")
#         print("¡Hasta luego! 🏪")
#         break
    
#     else:
#         print("⚠️ Ingresa un número válido (1-8)")





# biblioteca = []

# def agregar_libro(lista, titulo, autor, año, paginas):
#     libro = {
#         "titulo":titulo,
#         "autor": autor,
#         "año": año,
#         "paginas": paginas
#     }
#     lista.append(libro)
#     print(f"El libro {titulo} se agrego correctamente ")

# def mosntrar_biblioteca(lista):
#     if len(lista) == 0:
#         print("No hay libros en la biblioteca ")
#         return
#     print("============BIBLIOTECA=============")
#     total_paginas = 0
#     for i in range(len(lista)):
#         titulo = lista[i]["titulo"]
#         autor = lista[i]["autor"]
#         año = lista[i]["año"]
#         paginas = lista[i]["paginas"]

#         print(f"\n{i+1}. titulo: {titulo} ")
#         print(f"Autor: {autor}")
#         print(f"Año: {año}")
#         print(f"Paginas: {paginas}") 
#         total_paginas += paginas
#     promedio = total_paginas / len(lista)

#     print("====================")
#     print(f"Total de libros {len(lista)}")
#     print(f"Total de paginas {total_paginas}")
#     print(f"Promedio de paginas por libro {promedio:.2f}")

# def buscar_libro(lista, titulo):
#     for libro in lista:
#         if libro["titulo"].lower() == titulo.lower():
#             print("Libro encontrado")
#             print(f"titulo: {libro['titulo']} ")
#             print(f"Autor: {libro['autor']}")
#             print(f"Año: {libro['año']}")
#             print(f"Paginas: {libro['paginas']}")
#     print(f"No se encontro el libro {titulo}") 

# def buscar_libro(lista, titulo):
#     for libro in lista:
#         if libro['titulo'].lower()== titulo.lower():
#             print("Libro encontrado")
#             print(f"Titulo:{libro['titulo']}")
#             print(f"Autor: {libro['autor']}")
#             print(f"Año: {libro['año']}")
#             print(f"Paginas: {libro['paginas']}")
#             return
#     print(f"No se encontro el libro {titulo}")

# def eliminar_posicion(lista, posicion):
#     borrar_libro = lista.pop(posicion -1)
#     print(f"El libro {borrar_libro['titulo']} se elimino correctamete ")

# def libros_por_autor(lista, autor):
#     contador = 0
#     print(f"Libros de autores {autor}")

#     for libro in lista:
#         if libro['autor'].lower() == autor.lower():
#             print("Libro encontrado")
#             print(f"Titulo:{libro['titulo']}")
#             print(f"Año: {libro['año']}")
#             print(f"Paginas: {libro['paginas']}")
#             contador += 1
#     if contador == 0:
#         print(f"No hay libros {autor}")
#     else:
#         print(f"Total de libros {contador}")

# def libros_mas_largo(lista):
#     if len(lista) == 0:
#         print("No hay libros en la biblioteca ")
#         return
#     mas_largo = lista[0]

#     for libro in lista:
#         if libro['paginas'] > mas_largo['paginas']:
#             mas_largo = libro
#     print("Libro mas largo:")
#     print(f"Titulo: {mas_largo['titulo']}")
#     print(f"Autor: {mas_largo['autor']}")
#     print(f"Año: {mas_largo['año']}")
#     print(f"Paginas: {mas_largo['paginas']}")

# def libros_antiguos(lista, año_limite):
#     if len(lista) == 0:
#         print("No hay libros en la biblioteca ")
#         return
#     contador = 0
#     for libro in lista:
#         if libro['año'] == año_limite:
#             print("Libros mas antiguos ")
#             print(f"Titulo:{libro['titulo']}")
#             print(f"Año: {libro['año']}")
#             print(f"Paginas: {libro['paginas']}")
#             contador += 1
#     if contador == 0:
#         print(f"No hay libros anteriores de {año_limite}")
#     else:
#         print(f"Total de libros {contador}")

# while True:
#     print("========== MI BIBLIOTECA ==========")
#     print("1. Agregar libro")
#     print("2. Ver toda la biblioteca")
#     print("3. Buscar libro por título")
#     print("4. Eliminar libro")
#     print("5. Buscar libros por autor")
#     print("6. Ver libro más largo")
#     print("7. Ver libros antiguos")
#     print("8. Salir")

#     opcion = input("Ingresa una opcion (1-8)")
#     if opcion == "1":
#         titulo = input("Ingresa el titulo del libro ") 
#         autor = input("Ingresa el autor ")
#         año = int(input("Ingresa el año de publicacion "))
#         paginas = int(input("Ingresa el numero de paginas "))
#         agregar_libro(biblioteca, titulo, autor, año, paginas)

#     elif opcion == "2":
#         mosntrar_biblioteca(biblioteca)
#     elif opcion == "3":
#         buscar = input("Que libro buscas? ")
#         buscar_libro(biblioteca, buscar)
#     elif opcion == "4":
#         if len(biblioteca) == 0:
#             print("❌ No hay libros en la biblioteca")
#         else:
#             print("\n===== MI BIBLIOTECA =====")
#             for i in range(len(biblioteca)):
#                 print(f"{i+1}. {biblioteca[i]['titulo']} - {biblioteca[i]['autor']}")
        
#         posicion = int(input("\n¿Qué libro deseas eliminar? (número): "))
#         eliminar_posicion(biblioteca, posicion)
    
#     elif opcion == "5":
#         ver_libro = input("De que autor deseas ver los libros? ")
#         libros_por_autor(biblioteca, ver_libro)

#     elif opcion == "6":
#         libros_mas_largo(biblioteca)
#     elif opcion == "7":
#         mas_antiguo = input("Ingresa el año limite: ")
#         libros_antiguos(biblioteca, mas_antiguo)
#     elif opcion == "8":
#         print("\n============================")
#         print(f"Total de libros en biblioteca: {len(biblioteca)}")
    
#     # Calcular total de páginas
#     total_paginas = 0
#     for libro in biblioteca:
#         total_paginas += libro["paginas"]
    
#     print(f"Total de páginas: {total_paginas}")
#     print("¡HASTA LUEGO! 📚")
#     break 



# videojuegos = []
# def agregar_juegos(lista, titulo, cosola, año, calificacion):
#     juegos = {
#         "titulo": titulo,
#         "consola": cosola,
#         "año": año,
#         "calificacion": calificacion
#     }
#     lista.append(juegos)
#     print(f"El videojuego {titulo} se agrego corretamente ")

# def mostrar_colecion(lista):
#     if len(lista)== 0:
#         print("No hay videojuegos")
#         return
#     print("======COLECION DE VIDEJUEGOS========")
#     promedio_calificaciones = 0
#     for i in range(len(lista)):
#         titulo = lista[i]['titulo']
#         consola = lista[i]['consola']
#         año = lista[i]['año']
#         calificacion = lista[i]['calificacion']

#         print(f"\n {i+1} Titulo: {titulo}")
#         print(f"Cosola: {consola}")
#         print(f"Año: {año}")
#         print(f"Calificaciones: {calificacion}")
#         promedio_calificaciones += calificacion
#     promedio = promedio_calificaciones / len(lista)
#     print("============================")
#     print(f"El total de juegos es: {len(lista)}")
#     print(f"Promedio ded calificaciones: {promedio:.2f}")

# def buscar_juego(lista, titulo):
#     for juego in lista:
#         if juego['titulo'].lower()== titulo.lower():
#             print("Juego encontrado ")
#             print(f"Titulo: {juego['titulo']}")
#             print(f"Consola_ {juego['consola']}")
#             print(f"Año: {juego['año']}")
#             print(f"Calificacion: {juego['calificacion']}")
#             return
    
#     print(f"No se econtro el juego {titulo}")

# def eliminar_juego(lista, posicion):
#     borrar_juego = lista.pop(posicion -1)
#     print(f"El juego {borrar_juego['titulo']} se elimino corretamente ")

# def juegos_por_cosola(lista, consola):
#     contador = 0
#     print(f"juegos por consola {consola}")

#     for juegos in lista:
#         if juegos['consola'].lower() == consola.lower():
#             print("Juegos encontrado ppr consola")
#             print(f"\nTitulo: {juegos['titulo']}")
#             print(f"Consola: {juegos['consola']}")
#             print(f"Año: {juegos['año']}")
#             print(f"Calificacion: {juegos['calificacion']}")
#             contador +=1
#     if contador == 0:
#         print(f"No se encuentra juegos por consola {consola}")
#     else:
#         print(f"Total de juegos encontrados {contador}")

# def mejor_juego(lista):
#     if len(lista) == 0:
#         print("No hay juegos en la lista ")
#         return
#     mejor = lista[0]
#     for juego in lista:
#         if juego['calificacion'] > mejor['calificacion']:
#             mejor += juego
    
#     print("=============MEJOR JUEGO==============")
#     print(f"Titulo: {mejor['titulo']}")
#     print(f"Consola: {mejor['consola']}")
#     print(f"Año: {mejor['año']}")
#     print(f"Calficacion: {mejor['calificacion']}")


# def jeugos_exelentes(lista):
#     if len(lista):
#         print("No hay juegos en la lista ")
#         return
#     contador = 0
#     print("Juegos exelentes (>=9)")
#     for juego in lista:
#         if juego['calificacion'] >=9:
#             print(f"\nTitulo: {juego['titulo']}")
#             print(f"Consola: {juego['consola']}")
#             print(f"Año: {juego['año']}")
#             print(f"Calificacion: {juego['calificacion']}")
#             contador += 1

#     if contador == 0:
#         print("No hay juegos Exelentes")
#     else:
#         print(f"Total de jeuegos exelentes: {contador}")
# while True:
#     print("================MI COLECION DE VIDEOJUEGOS==================")
#     print("1.Agregar videojuegos")
#     print("2.Ver toda la coleccion")
#     print("3.Buscar videojuego por titulo")
#     print("4.Eliminar videojuego")
#     print("5.Ver juegos por consola")
#     print("6.Ver mejor juego (mayor calificacion)")
#     print("7.Ver juegos exelentes (>=9)")
#     print("8.Salir")

#     opcion = input("Ingresa una opcion del 1-8: ")

#     if opcion == "1":
#         juego = input("Ingresa el titulo del juego: ")
#         consola = input("Ingresa la consola: ")
#         Año = int(input("Ingresa el año de lanzamiento: "))
#         calificacion = int(input("Ingresa la calificacion: "))
#         agregar_juegos(videojuegos, juego, consola, Año, calificacion)
#     elif opcion == "2":
#         mostrar_colecion(videojuegos)
#     elif opcion == "3":
#         buscar = input("Que juego buscas? ")
#         buscar_juego(videojuegos, buscar)

#     elif opcion == "4":
#         if len(videojuegos) == 0:
#             print("No  hay videojuegos ")
#         else:
#             print("===============MI COLECION=================")
#             for i in range(len(videojuegos)):
#                 print(f"{i+1} . {videojuegos[i]['titulo']} - {videojuegos[i]['consola']}")
#             posicion = int(input("\nIngresa la posicion que deseas elminar: "))
#             eliminar_juego(videojuegos, posicion)
#     elif opcion == "5":
#         Juego = input("De que juego consola quieres ver los juegos?")
#         juegos_por_cosola(videojuegos, Juego)
#     elif opcion == "6":
#         mejor_juego(videojuegos)
#     elif opcion == "7":
#         jeugos_exelentes(videojuegos)
#     elif opcion == "8":
#         print("================================")
#         print(f"Total de juegos por colecion {len(videojuegos)}")

#         if len(videojuegos) > 0:
#             total_calificaciones = 0
#             for juego in videojuegos:
#                 total_calificaciones+= juego['calificacion']
            
#             promedio = total_calificaciones / len(videojuegos)
#             print(f"El promedio es: {promedio:.2f}")
#         else:
#             print("Calificacion promedio 0 ")
#         print(("Hazta luego "))
#         break
        




rutina = []

def agregar_ejercicio(lista, nombre, grupo, series, repeticiones, dificultad):
    ejercicio ={
        "nombre": nombre,
        "grupo_muscular": grupo,
        "series": series,
        "repeticiones": repeticiones,
        "dificultad": dificultad
    }
    lista.append(ejercicio)
    print(f"El ejercicicio {nombre} agregado corretamente")

def monstrar_rutina(lista):
    if len(lista) == 0:
        print("No se encuentra ningun ejercicio en la rutina")
        return
    print("====================RUTINA===============")
    total_series = 0
    total_repeticiones = 0

    baja = 0
    media = 0
    alta = 0

    for i in range(len(lista)):
        nombre = lista[i]['nombre']
        grupo_muscular = lista[i]['grupo_muscular']
        series = lista[i]['series']
        repeticiones = lista[i]['repeticiones']
        dificultad = lista[i]['dificultad']

        volumen = series * repeticiones 

        print(f"\n{i+1} Nombre: {nombre}")
        print(f"Grupo: {grupo_muscular}")
        print(f"Series: {series}")
        print(f"Repeticiones: {repeticiones}")
        print(f"Dificultada: {dificultad}")
        print(f"   Volumen: {volumen}")
        total_series = series
        total_repeticiones = repeticiones

        if dificultad.lower() == "baja":
            baja +=1
        elif dificultad.lower() == "media":
            media +=1
        elif dificultad.lower() == "alta":
            alta +=1
    promedio = total_repeticiones / len(lista)

    print("=============================")
    print(f"Total de ejercicios {len(lista)}")
    print(f"Total de series {total_series}")
    print(f"Total de repeticiones {total_repeticiones}")
    print(f"Promedio de repeticiones {promedio:.1f}")
    print(f"Baja: {baja}, Media: {media} Alta: {alta}")


def buscar_ejercicio(lista, nombre):
    for ejercicio in lista:
        if ejercicio['nombre'].lower() == nombre.lower():
            print("Ejercicio econtrado")
            print(f"Nombre: {ejercicio['nombre']}")
            print(f"Grupo: {ejercicio['grupo_muscular']}")
            print(f"Series: {ejercicio['series']}")
            print(f"Repeticiones: {ejercicio['repeticiones']}")
            print(f"Dificultad: {ejercicio['dificultad']}")
            return
    print("No se encongtro el ejercicio")

def eliminar_ejercicio(lista, posicion):
    borrar_ejercicio = lista.pop(posicion -1)
    print(f"El siguiente ejercicio {borrar_ejercicio['nombre']} se borro correctamnete ")

def ejercicios_por_grupo(lista, grupo_muscular):
    if len(lista) == 0:
        print("❌ No hay ejercicios en la rutina")
        return
    
    contador = 0
    print(f"\n💪 Ejercicios de {grupo_muscular.upper()}:")  # ✅ Una sola vez
    
    for ejercicio in lista:
        if ejercicio['grupo_muscular'].lower() == grupo_muscular.lower():
            # ✅ Solo muestra los datos (sin repetir el mensaje)
            print(f"\n   • {ejercicio['nombre']}")
            print(f"     Series: {ejercicio['series']} x {ejercicio['repeticiones']}")
            print(f"     Dificultad: {ejercicio['dificultad']}")
            contador += 1
    
    if contador == 0:
        print(f"   ✗ No se encontraron ejercicios de {grupo_muscular}")
    else:
        print(f"\n   Total: {contador} ejercicio(s)")

def ejercicios_por_dificultad(lista, dificultad):
    if len(lista) == 0:
        print("❌ No hay ejercicios en la rutina")
        return
    
    contador = 0
    print(f"\n🔥 Ejercicios de dificultad {dificultad.upper()}:")
    
    for ejercicio in lista:
        if ejercicio['dificultad'].lower() == dificultad.lower():
            print(f"\n   • {ejercicio['nombre']}")
            print(f"     Series: {ejercicio['series']} x {ejercicio['repeticiones']}")
            print(f"     Grupo: {ejercicio['grupo_muscular']}")
            contador += 1
    
    if contador == 0:
        print(f"   ✗ No se encontraron ejercicios de dificultad {dificultad}")
    else:
        print(f"\n   Total: {contador} ejercicio(s)")


def ejercicio_mas_intenso(lista):
    if len(lista) == 0:
        print("❌ No hay ejercicios en la rutina")
        return
    mas_intenso = lista[0]
    volumen_max = lista[0]['series'] * lista[0]['repeticiones']

    for ejercicio in lista:
        volumen = ejercicio['series'] * ejercicio['repeticiones']

        if volumen > volumen_maximo:
            mas_intenso = ejercicio
            volumen_maximo = volumen

    print("\n🏆 EJERCICIO MÁS INTENSO:")
    print(f"   Nombre: {mas_intenso['nombre']}")
    print(f"   Grupo: {mas_intenso['grupo_muscular']}")
    print(f"   Series: {mas_intenso['series']} x {mas_intenso['repeticiones']} reps")
    print(f"   Volumen total: {volumen_max}")
    print(f"   Dificultad: {mas_intenso['dificultad']}")

def modificar_lista(lista, nombre, nueva_serie):
    if nueva_serie <= 0:
        print("El numero debe ser mayor a 0 ")
        return
    
    for ejercicio in lista:
        if ejercicio['nombre'].lower() == nombre.lower():
            series_antiguas = ejercicio['series']
            ejercicio['series'] = nueva_serie

            print(f"Series de {nombre} actuializadas: {series_antiguas} a {nueva_serie}")
            return
    print(f"No se encontro el ejercicio {nombre}")

def estadisticas_completas(lista):
    if len(lista) == 0:
        print("❌ No hay ejercicios en la rutina")
        return
    
    total_series = 0
    total_repeticiones = 0

    alta = 0
    media = 0
    baja = 0

    grupos = {}

    for ejercicio in lista:
        series = ejercicio['series']
        repeticiones = ejercicio['repeticiones']
        dificultad = ejercicio['dificultad']
        grupo = ejercicio['grupo_muscular']

        total_repeticiones += repeticiones
        total_series += series

        if dificultad == "alta":
            alta +=1
        elif dificultad == "media":
            media += 1
        elif dificultad == "baja":
            baja += 1
        
        if grupo in grupos:
            grupos[grupo] += 1
        else:
            grupos[grupo] = 1

    promedio_reps = total_repeticiones / len(lista)

    print("\n📊========== ESTADÍSTICAS COMPLETAS ==========")
    print(f"Total de ejercicios: {len(lista)}")
    print(f"Total de series acumuladas: {total_series}")
    print(f"Promedio de repeticiones: {promedio_reps:.1f}\n")

    print("📌 Ejercicios por dificultad:")
    print(f"   Baja: {baja}")
    print(f"   Media: {media}")
    print(f"   Alta: {alta}\n")

    print("💪 Ejercicios por grupo muscular:")
    for grupo, cantidad in grupos.items():
        print(f"   {grupo.capitalize()}: {cantidad}")

    print("============================================\n")


while True:
    print("\n=========== MENÚ RUTINA DE EJERCICIOS ===========")
    print("1. Agregar ejercicio")
    print("2. Mostrar rutina completa")
    print("3. Buscar ejercicio por nombre")
    print("4. Eliminar ejercicio por posición")
    print("5. Ejercicios por grupo muscular")
    print("6. Ejercicios por dificultad")
    print("7. Ejercicio más intenso")
    print("8. Modificar series de un ejercicio")
    print("9. Estadísticas completas")
    print("10. Salir")
    print("=================================================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del ejercicio: ")
        grupo = input("Ingresa el grupo  muscular: ")
        series = int(input("Ingresa el numero de las serries: "))
        repeticiones = int(input("Ingresa las repeticiones: "))
        dificultad = input("Ingresa la dificultad (Baja/Media/Alta):")
        agregar_ejercicio(rutina, nombre, grupo, series, repeticiones, dificultad)

    elif opcion == "2":
        monstrar_rutina(rutina)

    elif opcion == "3":
        nombre = input("Nombre del ejercicio: ")
        buscar_ejercicio(rutina, nombre)
    elif opcion == "4":
        if len(rutina) == 0:
            print("No hay ejercicios en la rutina")
        else:
            for i in range(len(rutina)):
                print(f"{i+1} - {rutina[i]['nombre']} - {rutina[i]['grupo_muscular']}")

        
            eliminar = int(input("Ingresa la posicion que deseas eliminar "))
            eliminar_ejercicio(rutina, eliminar)
    
    elif opcion == "5":
        buscar = input("Que grupo muscular deseas ver? ")
        ejercicios_por_grupo(rutina, buscar)
    
    elif opcion == "6":
        dificultad = input("Que dificultad deseas ver? ")
        ejercicios_por_dificultad(rutina, dificultad)
    
    elif opcion == "7":
        ejercicio_mas_intenso(rutina)

    elif opcion == "8":
        nombre = input("Que ejercicio deseas modificar? ")
        nuevo_numero = int(input("Ingresa el nuevo de la series: "))
        modificar_lista(rutina, nombre, nuevo_numero)

    elif opcion == "9":
        estadisticas_completas(rutina)

    elif opcion == "10":
        print("==================RESUMEN FINAL===========================")
        print(f"Total de ejercicios {len(rutina)}")

        total_series = sum(e['series'] for e in rutina)
        total_repe = sum(e['repeticiones'] for e in rutina)

        print(f"Total de series {total_series}")
        print(f"Total de repeticiones sumadas: {total_repe}")
        print("========================================")
        print("Saliendo del programa...................... ")
        break


id_contador = 1
productos_disponibles = []
carrito = []

def agregar_producto_catalogo(lista, nombre, precio, stock, categoria,  descuento):
    global id_contador

    if precio <=0:
        print("El precio debe ser mayor a cero ")
        return
    if stock <0:
        print("El stock no pude ser positivo ")
        return
    if descuento <0 or descuento >100:
        print("El descuento debe estar entre 0 a 100")
        return
    
    producto = {
        "id": id_contador,
        "nombre": nombre, 
        "precio": precio,
        "stock":stock,
        "categoria": categoria,
        "descuento": descuento
    }
    lista.append(producto)
    print(f"El producto {nombre} agregado con el {id_contador}")

    id_contador +=1

def mosntrar_catalogo(lista):
    if len(lista) == 0:
        print("No hay productos")
        return
    
    print("\n=========================CATALAGO DE PRODUCTOS=======================")

    for i in range(lista(lista)):
        id_pro = lista[i]['id']
        nombre = lista[i]['nombre']
        precio = lista[i]['precio']
        stock = lista[i]['stock']
        categoria = lista[i]['descuento']
        descuento = lista[i]['descuento']

        precio_final = precio * (1-descuento/100)

        print("====================")
        print(f"ID: {id_pro}")
        print(f"Nombre: {nombre}")
        print(f"Categoria: {categoria}")
        print(f"Precio original: {precio:.2f}")

        if descuento > 0:
            print(f"El descuento es de: {descuento}%")
            print(f"Precio final: {precio_final}")
        else:
            print("No aplica el descuento")

        print(f"Stocks disponible: {stock} unidades")

    print("==============================")
    print(f"Total de productos en el catologo: {len(lista)}")

def actualizar_stock(lista,id , nuevo_stock):
    if nuevo_stock < 0:
        print("El estock no puede ser negativo")
        return
    
    for producto in lista: 
        if producto['id'] == id:
            stock_antiguo = producto['stock']
            producto['stock'] = nuevo_stock

            print(f"stock actualizado: {stock_antiguo} a {nuevo_stock}")
            return
    print(f"No se ecuentra el producto con el ID: {id}")


def agregar_al_carrito(catalogo, carrito, id_producto, cantidad):

    # 1. Buscar producto
    producto_encontrado = None
    for producto in catalogo:
        if producto['id'] == id_producto:
            producto_encontrado = producto
            break

    # 2. Si no existe
    if producto_encontrado is None:
        print("Producto no encontrado")
        return

    # 3. Verificar stock
    if producto_encontrado['stock'] < cantidad:
        print(f"Stock insuficiente. Disponible: {producto_encontrado['stock']}")
        return

    # 4. Descontar stock
    producto_encontrado['stock'] -= cantidad

    # 5. Crear item del carrito
    item_carrito = {
        "Id_producto": id_producto,
        "nombre": producto_encontrado['nombre'],
        "cantidad": cantidad,
        "precio_unitario": producto_encontrado['precio'],
        "descuento": producto_encontrado['descuento']
    }

    carrito.append(item_carrito)
    print(f"{cantidad} {producto_encontrado['nombre']} agregados al carrito")

def monstrar_carrito(carrito):
    if len(carrito) == 0:
        print("No se encuentra productos en el carrito ")
        return
    print("===============MI CARRITO==================")
    total_general = 0
    for i in range(len(carrito)):
        nombre = carrito[i]['nombre']
        cantidad = carrito[i]['cantidad']
        precio_unitario = carrito[i]['precio_unitario']
        descuento = carrito[i]['descuento']

        subtotal_sin_descuento = precio_unitario * cantidad
        subtotal_con_descuento = subtotal_sin_descuento * (1- (descuento /100))

        print(f"\n{i+1} - {nombre} - {cantidad}")
        print(f"precio unitario: {precio_unitario:.2f}")
        if descuento > 0:
            print(f"El descuento es: {descuento}")
        print(f"subtotal con descuento: {subtotal_con_descuento}")

        total_general += subtotal_con_descuento
    print("=========Total general=============")
    print(f"El total es: {total_general}")

def eliminar_del_carrito(catalogo, carrito, posicion):
    itme_eliminado = carrito.pop(posicion -1)

    for producto in catalogo:
        if producto['id'] == itme_eliminado['id_producto']:
            producto['stock'] += itme_eliminado['cantidad']
            break
    print(f"{itme_eliminado['nombre']} eliminado del carrito ")
    print(f"Stock devuelto: {itme_eliminado['cantidad']} unidades ")


def vaciar_carrito(catalogo, carrito):
    if len(carrito) == 0:
        print("No hay productos en el carrito ")
        return
    
    for item in carrito:
        for producto in catalogo:
            if producto['id'] == item['id_producto']:
                producto['stock'] += item['cantidad']
                break

    carrito.clear()
    print("Carrito vaciado")
    print("Stock devuelto al catalogo ")

def buscar_producto_por_id(lista, id):
    for producto in lista:
        if producto['id'] == id:
            return  producto
    return None

def productos_sin_stock(catalogo):
    if len(catalogo) == 0:
        print("No hya productos en el carrito")
        return
    contador = 0
    print("============PRODUCTOS SIN STOCK================")
    
    for productos in catalogo:
        if productos['stock'] == 0:
            print(f"\nNombe: .{productos['nombre']}")
            print(f" Id: {productos('id')}")
            print(f" Categoria: {productos['categoria']}")
            print(f" Precio: {productos['precio']:.2f}")
            contador +=1
    if contador == 0:
        print("Todos los productos tienen stock")
    else:
        print(f"\nProductos sin stock: {contador}")

def productos_por_categoria(catalogo, categoria):
    if len(catalogo) == 0:
        print("No hay productos ")
        return
    
    contador = 0 
    print(f"\nProductos por categoria: {categoria.upper()}")

    for productos in categoria:
        if productos['categoria'].lower() == categoria.lower():
            print(f"\nNombe: .{productos['nombre']}")
            print(f" Id: {productos('id')}")
            print(f" Precio:{productos['precio']} ")
            print(f" Stock: {productos['stock']}")

            contador +=1
    if contador == 0:
        print(f"No hay productos en la categoria {categoria}")
    else:
        print(f"\nTotal {contador} de productos")

def producto_mas_caro(catalogo):
    if len(catalogo) == 0:
        print("No hay productos en el catalogo")
        return
    mas_caro = catalogo[0]

    for producto in catalogo:
        if producto['precio'] > mas_caro['precio']:
            mas_caro = producto
        
    print("PRODUCTO MAS CARO")
    print(f"Nombre: {mas_caro['nombre']}")
    print(f"Categoria: {mas_caro['categoria']}")
    print(f"Precio: {mas_caro['precio']}")
    print(f"Stock: {mas_caro['stock']}")

    if mas_caro['precio'] > 0:
        precio_con_desc = mas_caro["precio"] * (1 - mas_caro["descuento"]/100)
        print(f"   Con descuento ({mas_caro['descuento']}%): ${precio_con_desc:.2f}")
def finalizar_compra(carrito):
    if len(carrito) == 0:
        print("🛒 El carrito está vacío. No hay nada que comprar.")
        return
    
    print("\n" + "="*50)
    print("          🧾 TICKET DE COMPRA")
    print("="*50)
    print()
    
    subtotal_general = 0
    descuentos_totales = 0
    
    for item in carrito:
        nombre = item["nombre"]
        cantidad = item["cantidad"]
        precio_unit = item["precio_unitario"]
        descuento = item["descuento"]
        
        subtotal_sin_desc = precio_unit * cantidad
        subtotal_con_desc = subtotal_sin_desc * (1 - descuento/100)
        descuento_aplicado = subtotal_sin_desc - subtotal_con_desc
        
        print(f"{nombre} x{cantidad}")
        print(f"  ${precio_unit:.2f} c/u", end="")
        
        if descuento > 0:
            print(f" (Desc. {descuento}%)", end="")
        
        print(f" .................. ${subtotal_con_desc:.2f}")
        
        subtotal_general += subtotal_sin_desc
        descuentos_totales += descuento_aplicado
    
    total_final = subtotal_general - descuentos_totales
    
    print()
    print("─" * 50)
    print(f"{'Subtotal:':<30} ${subtotal_general:>15.2f}")
    
    if descuentos_totales > 0:
        print(f"{'Descuentos aplicados:':<30} -${descuentos_totales:>14.2f}")
    
    print("─" * 50)
    print(f"{'TOTAL A PAGAR:':<30} ${total_final:>15.2f}")
    print("=" * 50)
    print()
    
    confirmacion = input("¿Confirmar compra? (s/n): ")
    
    if confirmacion.lower() == "s":
        carrito.clear()
        print("\n✓ ¡Compra realizada con éxito!")
        print("✓ Gracias por tu compra 🛒")
    else:
        print("\n✗ Compra cancelada")

while True:
    print("\n" + "="*50)
    print("          🛒 TIENDA ONLINE")
    print("="*50)
    print("\n--- CATÁLOGO ---")
    print("1. Agregar producto al catálogo")
    print("2. Ver catálogo completo")
    print("3. Actualizar stock de producto")
    print("\n--- CARRITO ---")
    print("4. Agregar producto al carrito")
    print("5. Ver mi carrito")
    print("6. Eliminar del carrito")
    print("7. Vaciar carrito")
    print("\n--- CONSULTAS ---")
    print("8. Buscar producto por ID")
    print("9. Ver productos sin stock")
    print("10. Ver productos por categoría")
    print("11. Ver producto más caro")
    print("\n--- COMPRA ---")
    print("12. Finalizar compra")
    print("13. Salir")
    print("="*50)

    opcion = input("Ingresa una opcion del (1-12)")

    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        stock = int(input("Ingresa el stock disponible: "))
        categoria = input("Categoría: ")
        descuento = float(input("Descuento: "))
        agregar_producto_catalogo(productos_disponibles, nombre, precio, stock, categoria, descuento)

    elif opcion == "2":
       monstrar_carrito(productos_disponibles)

    elif opcion == "3":
        if len(productos_disponibles) == 0:
            print("No hay productos en el catálogo")

        else:
            for p in productos_disponibles:
                print(f"\nID: {p['id']} - {p['nombre']} stock actual: {p['stock']}")
        
        id_pro = int(input("Ingresa el id del producto: "))
        nuevo_stock = input("Ingresa el stock del nuevo producto: ")
        actualizar_stock(productos_disponibles, id_pro, nuevo_stock)

    elif opcion == "4":
        if len(productos_disponibles) == 0:
            print("❌ No hay productos en el catálogo")
        else:
            # Mostrar catálogo primero
            print("\n===== CATÁLOGO =====")
            for p in productos_disponibles:
                print(f"ID: {p['id']} - {p['nombre']} - ${p['precio']:.2f} (Stock: {p['stock']})")
            
            id_prod = int(input("\nIngresa el ID del producto: "))
            cantidad = int(input("¿Cuántas unidades? "))
            agregar_al_carrito(productos_disponibles, carrito, id_prod, cantidad)
