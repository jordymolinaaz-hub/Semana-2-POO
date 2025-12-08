import datetime

print("MENU DE OPCIONES")
print("1.saludar")
print("2.Dar la fecha actual")
print("3.Decir adios")

opciones = int(input("Ingrese una opciones (1-3): "))

match opciones:
    case 1:
        print("espero que tengas un exelente dia")
    case 2:
        fecha_actual = datetime.date.today()
        print("La fecha es: " , fecha_actual)
    case 3:
        print("Adios velve pronto")