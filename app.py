from flask import Flask, render_template, request, redirect
from datetime import datetime
import pyodbc

app = Flask(__name__)

# Conexión a SQL Server
try:
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'  # Ajusta este valor si tu servidor tiene un nombre diferente
        'DATABASE=crud_biblioteca;'      # Asegúrate de que el nombre de la base de datos sea correcto
    )
    print("Conexión exitosa a SQL Server")
except pyodbc.Error as e:
    print("Error de conexión:", e)

# Función para ejecutar consultas
def ejecutar_consulta(query, parametros=None):
    try:
        cursor = conexion.cursor()
        if parametros:
            cursor.execute(query, parametros)
        else:
            cursor.execute(query)
        if query.strip().lower().startswith("select"):
            resultados = cursor.fetchall()  # Recopila resultados para SELECT
        else:
            conexion.commit()  # Confirmar cambios para consultas que modifican datos
            resultados = None
        cursor.close()  # Cierra el cursor después de usarlo
        return resultados
    except pyodbc.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

# Ruta del índice
@app.route('/')
def index():
    return render_template('index.html')

# CRUD de Usuarios
@app.route('/usuarios')
def listar_usuarios():
    print("Ruta '/usuarios' ejecutada")
    usuarios = ejecutar_consulta("SELECT * FROM usuarios")
    if usuarios is None:
        usuarios = []
    return render_template('usuario_crud.html', usuarios=usuarios)

@app.route('/usuarios/agregar', methods=['POST'])
def agregar_usuario():
    datos = (
        request.form['nombre'],
        request.form['apellido'],
        request.form['email'],
        request.form['direccion'],
        request.form['fechaNacimiento']
    )
    print("Datos recibidos para agregar usuario:", datos)  # Para depuración
    ejecutar_consulta(
        "INSERT INTO usuarios (nombre, apellido, email, direccion, fechaNacimiento) VALUES (?, ?, ?, ?, ?)",
        datos
    )
    return redirect('/usuarios')

@app.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    ejecutar_consulta("DELETE FROM usuarios WHERE id=?", (id,))
    return redirect('/usuarios')

# CRUD de Libros
@app.route('/libros')
def listar_libros():
    print("Ruta '/libros' ejecutada")
    libros = ejecutar_consulta("SELECT * FROM libros")
    if libros is None:
        libros = []
    return render_template('libro_crud.html', libros=libros)

@app.route('/libros/agregar', methods=['POST'])
def agregar_libro():
    datos = (
        request.form['titulo'],
        request.form['autor'],
        request.form['isbn'],
        request.form['categoria'],
        request.form['ejemplares']
    )
    print("Datos recibidos para agregar libro:", datos)  # Para depuración
    ejecutar_consulta(
        "INSERT INTO libros (titulo, autor, isbn, categoria, ejemplares) VALUES (?, ?, ?, ?, ?)",
        datos
    )
    return redirect('/libros')

@app.route('/libros/editar/<int:id>', methods=['POST'])
def editar_libro(id):
    datos = (
        request.form['titulo'],
        request.form['autor'],
        request.form['isbn'],
        request.form['categoria'],
        request.form['ejemplares'],
        id
    )
    print("Datos recibidos para editar libro:", datos)  # Para depuración
    ejecutar_consulta(
        "UPDATE libros SET titulo=?, autor=?, isbn=?, categoria=?, ejemplares=? WHERE id=?",
        datos
    )
    return redirect('/libros')

@app.route('/libros/eliminar/<int:id>')
def eliminar_libro(id):
    ejecutar_consulta("DELETE FROM libros WHERE id=?", (id,))
    return redirect('/libros')

# CRUD de Préstamos
@app.route('/prestamos')
def listar_prestamos():
    print("Ruta '/prestamos' ejecutada")
    prestamos = ejecutar_consulta("SELECT * FROM prestamos")
    usuarios = ejecutar_consulta("SELECT * FROM usuarios")  # Obtener usuarios
    libros = ejecutar_consulta("SELECT * FROM libros")      # Obtener libros
    if prestamos is None:
        prestamos = []
    if usuarios is None:
        usuarios = []
    if libros is None:
        libros = []
    return render_template('prestamo_crud.html', prestamos=prestamos, usuarios=usuarios, libros=libros)

@app.route('/prestamos/agregar', methods=['POST'])
def agregar_prestamo():
    datos = (
        request.form['usuario_id'],
        request.form['libro_id'],
        datetime.strptime(request.form['fechaPrestamos'], '%Y-%m-%d'),
        datetime.strptime(request.form['fechaDevolucion'], '%Y-%m-%d'),
        request.form['estado']
    )
    print("Datos recibidos para agregar préstamo:", datos)  # Para depuración
    ejecutar_consulta(
        "INSERT INTO prestamos (usuario_id, libro_id, fechaPrestamos, fechaDevolucion, estado) VALUES (?, ?, ?, ?, ?)",
        datos
    )
    return redirect('/prestamos')

@app.route('/prestamos/eliminar/<int:id>')
def eliminar_prestamo(id):
    ejecutar_consulta("DELETE FROM prestamos WHERE id=?", (id,))
    return redirect('/prestamos')

# CRUD de Reservas
@app.route('/reservas')
def listar_reservas():
    print("Ruta '/reservas' ejecutada")
    reservas = ejecutar_consulta("SELECT * FROM reservas")
    usuarios = ejecutar_consulta("SELECT * FROM usuarios")  # Obtener usuarios
    libros = ejecutar_consulta("SELECT * FROM libros")      # Obtener libros
    if reservas is None:
        reservas = []
    if usuarios is None:
        usuarios = []
    if libros is None:
        libros = []
    return render_template('reserva_crud.html', reservas=reservas, usuarios=usuarios, libros=libros)

@app.route('/reservas/agregar', methods=['POST'])
def agregar_reserva():
    datos = (
        request.form['usuario_id'],
        request.form['libro_id'],
        datetime.strptime(request.form['fechaReserva'], '%Y-%m-%d')
    )
    print("Datos recibidos para agregar reserva:", datos)  # Para depuración
    ejecutar_consulta(
        "INSERT INTO reservas (usuario_id, libro_id, fechaReserva) VALUES (?, ?, ?)",
        datos
    )
    return redirect('/reservas')

@app.route('/reservas/eliminar/<int:id>')
def eliminar_reserva(id):
    ejecutar_consulta("DELETE FROM reservas WHERE id=?", (id,))
    return redirect('/reservas')

@app.route('/favicon.ico')
def favicon():
    return "", 204  # Evitamos el error de favicon

if __name__ == '__main__':
    app.run(debug=True)