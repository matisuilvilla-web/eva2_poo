-- Crear base de datos
CREATE DATABASE IF NOT EXISTS ap_170 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Crear la tabla
USE ap_170;

CREATE TABLE producto(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    precio FLOAT NOT NULL,
    stock INT NOT NULL);