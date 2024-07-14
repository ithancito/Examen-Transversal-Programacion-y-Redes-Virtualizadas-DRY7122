import hashlib
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'usuarios.db'
PORT = 5800

# Crear base de datos y tabla de usuarios
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            contrasena_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    # Agregar usuarios predefinidos
    add_user("ithan", "contrasena_ithan")
    add_user("gonzalo", "contrasena_gonzalo")
    add_user("luis", "contrasena_luis")

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Agregar usuario a la base de datos
def add_user(nombre, contrasena):
    contrasena_hash = hash_password(contrasena)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, contrasena_hash) VALUES (?, ?)', (nombre, contrasena_hash))
    conn.commit()
    conn.close()

# Validar usuario
def validate_user(nombre, contrasena):
    contrasena_hash = hash_password(contrasena)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nombre = ? AND contrasena_hash = ?', (nombre, contrasena_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Rutas de la aplicación Flask
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    add_user(nombre, contrasena)
    return jsonify({'message': 'Usuario registrado exitosamente'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    if validate_user(nombre, contrasena):
        return jsonify({'message': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'message': 'Nombre de usuario o contraseña incorrectos'}), 401

if __name__ == '__main__':
    init_db()
    app.run(port=PORT)

