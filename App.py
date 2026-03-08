from flask import Flask, render_template, request

app= Flask(__name__)


# ================= CONVERSIONES =================
#================== VOLUMEN =================
def to_litros(valor, unidad_origen):
    if unidad_origen == "L":       # Litros
        return valor
    elif unidad_origen == "ml":    # Mililitros
        return valor / 1000
    elif unidad_origen == "gal":   # Galones (EE.UU.)
        return valor * 3.78541
    elif unidad_origen == "m3":    # Metros cúbicos
        return valor * 1000
    else:
        raise ValueError("Unidad de origen no soportada")

def from_litros(litros_val, unidad_destino):
    if unidad_destino == "L":
        return litros_val
    elif unidad_destino == "mL":
        return litros_val * 1000
    elif unidad_destino == "gal":
        return litros_val / 3.78541
    elif unidad_destino == "m3":
        return litros_val / 1000
    else:
        raise ValueError("Unidad de destino no soportada")

def convertir_volumen(valor, unidad_origen, unidad_destino):
    l = to_litros(valor, unidad_origen)
    return from_litros(l, unidad_destino)


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
    "mm": 0.001,
    "cm": 0.01,
    "in": 0.0254,
    "ft": 0.3048,
    "m": 1,
    "km": 1000,
    "mi": 1609.34   
}


def convertir_distancia(valor, origen, destino):
    metros = valor * factores_distancia[origen]
    return metros / factores_distancia[destino]


# =================    PESO   =================
factores_peso = {
    "oz": 28.3495,
    "g": 1,
    "kg": 1000,
    "lb": 453.592
}

def convertir_peso(valor, origen, destino):
    gramos = valor * factores_peso[origen]
    return gramos / factores_peso[destino]


# ================= FIN DE CONVERSIONes =================



# ================= RUTA WEB =================
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
         tipo = request.form["tipo"]
         valor = float(request.form["valor"])
         origen = request.form["origen"]
         destino = request.form["destino"]
         
         if tipo == "volumen":
            resultado = convertir_volumen(valor, origen, destino)
         elif tipo == "temperatura":
            resultado = convertir_temperatura(valor, origen, destino)
         elif tipo == "distancia":
            resultado = convertir_distancia(valor, origen, destino)
         elif tipo == "peso":
            resultado = convertir_peso(valor, origen, destino)


    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)    