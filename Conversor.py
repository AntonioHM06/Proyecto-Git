def titulo():
    print("\n" + "-" * 40)
    print(" " * 10 + "CONVERSOR DE UNIDADES")
    print("-" * 40 + "\n")


# ================= MENÚ PRINCIPAL =================
def mostrar_menu_principal():
    print("MENÚ PRINCIPAL:")
    print("1. Temperatura")
    print("2. Distancia")
    print("3. Peso")
    print("4. Salir")


# ================= TEMPERATURA =================
def mostrar_menu_temperatura_origen():
    print("CONVERSIÓN DE TEMPERATURA")
    print("1. Celsius (°C)")
    print("2. Kelvin (K)")
    print("3. Fahrenheit (°F)")
    print("4. Volver al menú principal")


def mostrar_menu_temperatura_destino(unidad_origen):
    print("Elija la unidad destino ")
    opciones = {"C": "Celsius (°C)", "K": "Kelvin (K)", "F": "Fahrenheit (°F)"}
    disponibles = {}
    i = 1
    for cod, nombre in opciones.items():
        if cod != unidad_origen:
            print(f"{i}. {nombre}")
            disponibles[str(i)] = cod
            i += 1
    print(f"{i}. Volver")
    return disponibles, str(i)


def unidad_por_opcion_temperatura(op):
    return {"1": "C", "2": "K", "3": "F"}.get(op)
    


def nombre_unidad_temperatura(cod):
    return {"C": "Celsius (°C)", "K": "Kelvin (K)", "F": "Fahrenheit (°F)"}.get(cod)


def to_celsius(valor, unidad_origen):
    if unidad_origen == "C":
        return valor
    elif unidad_origen == "K":
        return valor - 273.15
    elif unidad_origen == "F":
        return (valor - 32) * 5/9


def from_celsius(celsius_val, unidad_destino):
    if unidad_destino == "C":
        return celsius_val
    elif unidad_destino == "K":
        return celsius_val + 273.15
    elif unidad_destino == "F":
        return (celsius_val * 9/5) + 32


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    c = to_celsius(valor, unidad_origen)
    return from_celsius(c, unidad_destino)


def pedir_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None


def menu_temperatura():
    while True:
        mostrar_menu_temperatura_origen()
        op_origen = input("Seleccione unidad de origen (1-4): ").strip()

        if op_origen == "4":
            return

        unidad_origen = unidad_por_opcion_temperatura(op_origen)
        if not unidad_origen:
            print("Opción inválida.")
            continue

        valor = pedir_float(f"Ingrese el valor en {nombre_unidad_temperatura(unidad_origen)}: ")
        if valor is None:
            print("Debe ingresar un valor numérico.")
            continue

        while True:
            disponibles, opcion_volver = mostrar_menu_temperatura_destino(unidad_origen)
            op_destino = input("Seleccione unidad destino: ").strip()

            if op_destino == opcion_volver:
                break

            if op_destino not in disponibles:
                print("Opción inválida.")
                continue

            unidad_destino = disponibles[op_destino]
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)

            print(f"\n➡ {valor:.2f} {nombre_unidad_temperatura(unidad_origen)} = {resultado:.2f} {nombre_unidad_temperatura(unidad_destino)}\n")

            if input("¿Convertir a otra unidad destino? (s/n): ").lower() != "s":
                break

# ================= DISTANCIA =================
factores_distancia = {
    "milímetros": 0.001,
    "centímetros": 0.01,
    "pulgadas": 0.0254,
    "pies": 0.3048,
    "metros": 1,
    "kilómetros": 1000,
    "millas": 1609.34
}


def mostrar_menu_distancia_origen():
    print("\n--- CONVERSIÓN DE DISTANCIA ---")
    print("1. Milímetros")
    print("2. Centímetros")
    print("3. Pulgadas")
    print("4. Pies")
    print("5. Metros")
    print("6. Kilómetros")
    print("7. Millas")
    print("8. Volver al menú principal")


def unidad_por_opcion_distancia(op):
    opciones = {
        "1": "milímetros",
        "2": "centímetros",
        "3": "pulgadas",
        "4": "pies",
        "5": "metros",
        "6": "kilómetros",
        "7": "millas"
    }
    return opciones.get(op)


def mostrar_menu_distancia_destino(unidad_origen):
    print("\n-- Seleccione unidad destino --")
    disponibles = {}
    i = 1
    for u in factores_distancia.keys():
        if u != unidad_origen:
            print(f"{i}. {u}")
            disponibles[str(i)] = u
            i += 1
    print(f"{i}. Volver")
    return disponibles, str(i)


def convertir_distancia(valor, origen, destino):
    metros = valor * factores_distancia[origen]
    return metros / factores_distancia[destino]


def menu_distancia():
    while True:
        mostrar_menu_distancia_origen()
        op_origen = input("Seleccione la unidad de origen (1-8): ").strip()

        if op_origen == "8":
            return

        unidad_origen = unidad_por_opcion_distancia(op_origen)
        if not unidad_origen:
            print("Opción inválida.")
            continue

        try:
            valor = float(input(f"Ingrese el valor en {unidad_origen}: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        while True:
            disponibles, opcion_volver = mostrar_menu_distancia_destino(unidad_origen)
            op_destino = input("Seleccione unidad destino: ").strip()

            if op_destino == opcion_volver:
                break

            if op_destino not in disponibles:
                print("Opción inválida.")
                continue

            unidad_destino = disponibles[op_destino]
            resultado = convertir_distancia(valor, unidad_origen, unidad_destino)

            print(f"\n➡ {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}\n")

            if input("¿Convertir a otra unidad destino? (s/n): ").lower() != "s":
                break



# ================= INICIO DEL PROGRAMA =================
def main():
    titulo()
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            menu_temperatura()
            titulo()
        elif opcion == "4":
            print("\nAdios perras, Me saludan a su mamá...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()