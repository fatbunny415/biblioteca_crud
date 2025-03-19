from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.bibliotecas

# Colecciones
usuarios = db.usuarios
libros = db.Libros
prestamos = db.Prestamos
reservas = db.Reservas 

@app.route("/")
def index():
    return render_template("index.html")

# Registrar usuarios
@app.route("/registrar_usuario", methods=["GET", "POST"])
def registrar_usuario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        usuarios.insert_one({"nombre": nombre, "correo": correo})
        return redirect(url_for("index"))
    return render_template("registrar_usuario.html")

# Ingresar libros nuevos
@app.route("/ingresar_libro", methods=["GET", "POST"])
def ingresar_libro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ejemplares = int(request.form["ejemplares"])
        libros.insert_one({"titulo": titulo, "autor": autor, "ejemplares": ejemplares, "prestados": 0})
        return redirect(url_for("index"))
    return render_template("ingresar_libro.html")

@app.route("/consultar_libros")
def consultar_libros():
    libros = list(db.Libros.find())  # Convertir el Cursor en una lista
    return render_template("consultar_libros.html", libros=libros)



# Asignar reservas
@app.route("/reservar_libro", methods=["GET", "POST"])
def reservar_libro():
    if request.method == "POST":
        usuario_id = request.form["usuario_id"]
        libro_id = request.form["libro_id"]
        libro = libros.find_one({"_id": libro_id})
        if libro["ejemplares"] > libro["prestados"]:
            prestamos.insert_one({"usuario_id": usuario_id, "libro_id": libro_id})
            libros.update_one({"_id": libro_id}, {"$inc": {"prestados": 1}})
        return redirect(url_for("index"))
    return render_template("reservar_libro.html", usuarios=usuarios.find(), libros=libros.find())

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/prestar_libro", methods=["GET", "POST"])
# def prestar_libro():
#     if request.method == "POST":
#         usuario_id = request.form["usuario_id"]
#         libro_id = request.form["libro_id"]
#         libro = db.Libros.find_one({"_id": libro_id})

#         # Verificar si el libro tiene ejemplares disponibles
#         if libro and (libro["ejemplares"] > libro["prestados"]):
#             # Registrar el préstamo en la colección
#             db.prestamos.insert_one({"usuario_id": usuario_id, "libro_id": libro_id})
#             # Actualizar el número de ejemplares prestados
#             db.Libros.update_one({"_id": libro_id}, {"$inc": {"prestados": 1}})
#             mensaje = "Préstamo realizado con éxito."
#         else:
#             mensaje = "No hay ejemplares disponibles para préstamo."
#         return render_template("prestar_libro.html", usuarios=db.usuarios.find(), libros=db.Libros.find(), mensaje=mensaje)

#     # GET: Renderiza la página con la lista de usuarios y libros
#     return render_template("prestar_libro.html", usuarios=db.usuarios.find(), libros=db.Libros.find())

