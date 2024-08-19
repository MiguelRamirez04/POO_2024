import mysql.connector

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca'
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Ocurrió un error al conectar a la base de datos: {err}")
        return None

def get_cursor(conexion):
    if conexion:
        try:
            cursor = conexion.cursor(buffered=True)
            return cursor
        except mysql.connector.Error as err:
            print(f"Ocurrió un error al crear el cursor: {err}")
            return None
    return None

"""
CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    tel VARCHAR(15) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    tipo ENUM('Empleado', 'Cliente') NOT NULL
);

CREATE TABLE IF NOT EXISTS empleados (
    id INT PRIMARY KEY,
    puesto VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id) REFERENCES personas(id)
);

CREATE TABLE IF NOT EXISTS clientes (
    id INT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES personas(id)
);

CREATE TABLE IF NOT EXISTS material (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    tipo ENUM('Revista', 'DVD', 'Libro') NOT NULL,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS revistas (
    id INT PRIMARY KEY,
    numero INT NOT NULL,
    FOREIGN KEY (id) REFERENCES material(id)
);

CREATE TABLE IF NOT EXISTS dvds (
    id INT PRIMARY KEY,
    duracion INT NOT NULL,
    FOREIGN KEY (id) REFERENCES material(id)
);

CREATE TABLE IF NOT EXISTS libros (
    id INT PRIMARY KEY,
    num_paginas INT NOT NULL,
    FOREIGN KEY (id) REFERENCES material(id)
);

CREATE TABLE IF NOT EXISTS prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT NOT NULL,
    fecha_prestamo DATETIME NOT NULL,
    fecha_entrega DATETIME NOT NULL,
    cliente_id INT NOT NULL,
    empleado_id INT NOT NULL,
    FOREIGN KEY (material_id) REFERENCES material(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);
"""