# PIN de acceso (puedes cambiarlo por el que tú quieras)
PIN_CORRECTO = "1234"
intentos = 3

# Verificación del PIN
while intentos > 0:
    pin_ingresado = input("🔒 Ingresa tu PIN de 4 dígitos: ")
    if pin_ingresado == PIN_CORRECTO:
        print("✅ PIN correcto. Accediendo al cajero...\n")
        break
    else:
        intentos -= 1
        print(f"❌ PIN incorrecto. Te quedan {intentos} intento(s).")

if intentos == 0:
    print("🚫 Has excedido el número de intentos. Tarjeta bloqueada.")
else:
    # Código del cajero
    saldo = 1000  # Saldo inicial

    while True:
        print("\n=== CAJERO AUTOMÁTICO ===")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. SALIR")

        opcion = input("Elige una opción (1/4): ")

        if opcion == "1":
            print(f"💰 Tu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                cantidad = float(input("¿Cuánto deseas depositar? "))
                if cantidad > 0:
                    saldo += cantidad
                    print(f"✅ Depósito exitoso. Saldo actualizado: ${saldo:.2f}")
                else:
                    print("⚠️ La cantidad debe ser mayor a cero.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingresa un número.")

        elif opcion == "3":
            try:
                cantidad = float(input("¿Cuánto deseas retirar? "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a cero.")
                elif cantidad > saldo:
                    print("⚠️ Fondos insuficientes.")
                else:
                    saldo -= cantidad
                    print(f"✅ Retiro exitoso. Saldo restante: ${saldo:.2f}")
            except ValueError:
                print("⚠️ Entrada inválida. Ingresa un número.")

        elif opcion == "4":
            print("👋 Gracias por usar el cajero. ¡Vuelve pronto!")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")
