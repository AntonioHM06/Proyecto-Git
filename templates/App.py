from flask import Flask, render_template, request

app= Flask(__name__)


# ================= CONVERSIONES =================

# =================  TEMPERATURA =================


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


# =================    PESO   =================
factores_peso = {
    "onzas": 28.3495,
    "gramos": 1,
    "kilogramos": 1000
}


def mostrar_menu_peso_origen():
    print("\n--- CONVERSIÓN DE PESO ---")
    print("1. Onzas")
    print("2. Gramos")
    print("3. Kilogramos")
    print("4. Volver al menú principal")


def unidad_por_opcion_peso(op):
    return {"1": "onzas", "2": "gramos", "3": "kilogramos"}.get(op)


def mostrar_menu_peso_destino(unidad_origen):
    print("\n-- Seleccione unidad destino --")
    disponibles = {}
    i = 1
    for u in factores_peso.keys():
        if u != unidad_origen:
            print(f"{i}. {u}")
            disponibles[str(i)] = u
            i += 1
    print(f"{i}. Volver")
    return disponibles, str(i)


def convertir_peso(valor, origen, destino):
    gramos = valor * factores_peso[origen]
    return gramos / factores_peso[destino]


def menu_peso():
    while True:
        mostrar_menu_peso_origen()
        op_origen = input("Seleccione la unidad de origen (1-4): ").strip()

        if op_origen == "4":
            return

        unidad_origen = unidad_por_opcion_peso(op_origen)
        if not unidad_origen:
            print("Opción inválida.")
            continue

        try:
            valor = float(input(f"Ingrese el valor en {unidad_origen}: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        while True:
            disponibles, opcion_volver = mostrar_menu_peso_destino(unidad_origen)
            op_destino = input("Seleccione unidad destino: ").strip()

            if op_destino == opcion_volver:
                break

            if op_destino not in disponibles:
                print("Opción inválida.")
                continue

            unidad_destino = disponibles[op_destino]
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)

            print(f"\n➡ {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}\n")

            if input("¿Convertir a otra unidad destino? (s/n): ").lower() != "s":
                break


# ================= FIN DE CONVERSI =================



# ================= RUTA WEB =================




