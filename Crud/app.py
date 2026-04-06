from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ──────────────────────────────────────────
#  BASE DE DATOS FALSA  (lista en memoria)
#  Se reinicia cada vez que reinicias Flask
# ──────────────────────────────────────────
productos = [
    {"id": 1, "nombre": "cuaderno", "marca": "norma", "cantidad":60, "precio": 2.50},
    {"id": 2, "nombre": "lápiz", "marca":   "berol", "cantidad":40, "precio": 2.50},
    {"id": 3, "nombre": "corrector", "marca": "puma", "cantidad":70, "precio": 2.50},
    {"id": 4, "nombre": "regla", "marca":   "gloria", "cantidad":100, "precio": 2.50},
    {"id": 5, "nombre": "marcador", "marca": "paper", "cantidad":110, "precio": 2.50},
    {"id": 6, "nombre": "tijera", "marca": "tigger", "cantidad":70, "precio": 2.50},
    {"id": 7, "nombre": "lapicero", "marca": "office", "cantidad":90, "precio": 2.50},
    {"id": 8, "nombre": "colbón", "marca": "pegamás", "cantidad":60, "precio": 2.50},
    {"id": 9, "nombre": "colores", "marca": "recreo", "cantidad":170, "precio": 2.50},
    {"id": 10, "nombre": "block", "marca": "carvajal", "cantidad":100, "precio": 2.50},
    
]
siguiente_id = 4


# ── READ ──────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", productos=productos)


# ── CREATE ────────────────────────────────
@app.route("/agregar", methods=["POST"])
def agregar():
    global siguiente_id
    productos.append({
        "id":       siguiente_id,
        "nombre":   request.form["nombre"],
        "cantidad": int(request.form["cantidad"]),
        "precio":   float(request.form["precio"]),
    })
    siguiente_id += 1
    return redirect(url_for("index"))


# ── UPDATE ────────────────────────────────
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    for p in productos:
        if p["id"] == id:
            p["nombre"]   = request.form["nombre"]
            p["cantidad"] = int(request.form["cantidad"])
            p["precio"]   = float(request.form["precio"])
    return redirect(url_for("index"))


# ── DELETE ────────────────────────────────
@app.route("/eliminar/<int:id>")
def eliminar(id):
    productos[:] = [p for p in productos if p["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
