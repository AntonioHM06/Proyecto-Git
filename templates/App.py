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



# =================    PESO   =================



# ================= FIN DE CONVERSI =================



# ================= RUTA WEB =================




