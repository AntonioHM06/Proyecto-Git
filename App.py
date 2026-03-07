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
         
         if tipo == "temperatura":
            resultado = convertir_temperatura(valor, origen, destino)
         elif tipo == "distancia":
            resultado = convertir_distancia(valor, origen, destino)
         elif tipo == "peso":
            resultado = convertir_peso(valor, origen, destino)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)    