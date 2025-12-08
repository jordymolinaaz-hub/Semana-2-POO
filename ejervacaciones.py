historial = []
while True :
    print("Calculadora basica de en python")
    print("1.suma")
    print("2.resta")
    print("3.Multiplicacion")
    print("4.Divicion")
    print("5.SALIR")

    opcion = input("Elegi una opcion de (1-5) ")

    if opcion == "5":
        print("SALIENDO DE LA CALCULADORA .......")
        break
    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            suma = num1+num2
            print(f"Resultado de la suma es {suma} taran.")
        elif opcion == "2":
            resultado = num1-num2
            print(f"Resultado: {num1} - {num2} = {resultado} ")
        elif opcion == "3":
            resultado = num1*num2
            print(f"Resultado: {num1} * {num2} = {resultado} ")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado} ")
            else: 
                print("No se puede divir entre ceros")
    else:
        print("Opcion vo valida vayase ALV")

# Mostrar historial al salir
print("\n📜 Historial de operaciones:")
if historial:
    for item in historial:
        print("- " + item)
else:
    print("No se realizaron operaciones.")

            

    


