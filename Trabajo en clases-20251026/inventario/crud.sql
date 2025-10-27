-- Crear base de datos
CREATE DATABASE IF NOT EXISTS CRUD CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Crear la tabla
USE CRUD;

-- =========================================================
-- TABLA + FUNCIÓN + CRUD (simple y para primer nivel)
-- =========================================================

-- 1) Tabla producto (con borrado lógico y nombre único)
DROP TABLE IF EXISTS producto;

CREATE TABLE producto(
    id      INT AUTO_INCREMENT PRIMARY KEY,
    nombre  VARCHAR(20) NOT NULL,
    precio  DECIMAL(10,2) NOT NULL,
    stock   INT NOT NULL,
    activo  TINYINT(1) NOT NULL DEFAULT 1,
    UNIQUE KEY uq_producto_nombre (nombre)
);

-- 2) Función: devuelve id por nombre (solo si está activo) o -1 si no existe
DROP FUNCTION IF EXISTS fn_producto_id_por_nombre;
DELIMITER $$
CREATE FUNCTION fn_producto_id_por_nombre(p_nombre VARCHAR(20))
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE v_id INT;
    SELECT id INTO v_id
    FROM producto
    WHERE nombre = p_nombre AND activo = 1
    LIMIT 1;

    IF v_id IS NULL THEN
        RETURN -1;
    END IF;
    RETURN v_id;
END$$
DELIMITER ;

-- 3) Crear producto:
--    - Inserta si no existe
--    - Si existe (activo o inactivo), actualiza datos y lo deja activo
DROP PROCEDURE IF EXISTS sp_producto_crear;
DELIMITER $$
CREATE PROCEDURE sp_producto_crear(
    IN  p_nombre VARCHAR(20),
    IN  p_precio DECIMAL(10,2),
    IN  p_stock  INT,
    OUT p_id_nuevo INT
)
BEGIN
    DECLARE v_id INT;

    SELECT id INTO v_id FROM producto WHERE nombre = p_nombre LIMIT 1;

    IF v_id IS NULL THEN
        INSERT INTO producto(nombre, precio, stock, activo)
        VALUES (p_nombre, p_precio, p_stock, 1);
        SET p_id_nuevo = LAST_INSERT_ID();
    ELSE
        UPDATE producto
        SET precio = p_precio,
            stock  = p_stock,
            activo = 1
        WHERE id = v_id;
        SET p_id_nuevo = v_id;
    END IF;
END$$
DELIMITER ;

-- 4) Listar productos activos (ordenados por nombre)
DROP PROCEDURE IF EXISTS sp_producto_listar_activos;
DELIMITER $$
CREATE PROCEDURE sp_producto_listar_activos()
BEGIN
    SELECT id, nombre, precio, stock
    FROM producto
    WHERE activo = 1
    ORDER BY nombre;
END$$
DELIMITER ;

-- 5) Actualizar por nombre (pasa NULL para no cambiar un campo)
DROP PROCEDURE IF EXISTS sp_producto_actualizar_por_nombre;
DELIMITER $$
CREATE PROCEDURE sp_producto_actualizar_por_nombre(
    IN p_nombre VARCHAR(20),
    IN p_precio DECIMAL(10,2),  -- NULL = no cambiar
    IN p_stock  INT             -- NULL = no cambiar
)
BEGIN
    UPDATE producto
    SET
        precio = COALESCE(p_precio, precio),
        stock  = COALESCE(p_stock,  stock)
    WHERE nombre = p_nombre AND activo = 1;
END$$
DELIMITER ;

-- 6) Borrado lógico por nombre (marca activo=0)
DROP PROCEDURE IF EXISTS sp_producto_borrar_logico_por_nombre;
DELIMITER $$
CREATE PROCEDURE sp_producto_borrar_logico_por_nombre(
    IN p_nombre VARCHAR(20)
)
BEGIN
    UPDATE producto
    SET activo = 0
    WHERE nombre = p_nombre AND activo = 1;
END$$
DELIMITER ;

-- ============================================
-- EJEMPLOS DE USO RÁPIDOS (opcionales):
-- SET @id := 0; CALL sp_producto_crear('Lapiz', 100.00, 50, @id); SELECT @id;
-- CALL sp_producto_listar_activos();
-- CALL sp_producto_actualizar_por_nombre('Lapiz', NULL, 80);  -- solo stock
-- CALL sp_producto_borrar_logico_por_nombre('Lapiz');
-- SELECT fn_producto_id_por_nombre('Lapiz') AS id_activo;    -- -1 si no existe activo
-- ============================================

/*
Notas rápidas
¿Qué hacen DELIMITER $$ y DELIMITER ;?
	El cliente (p. ej., mysql) usa ; para saber “aquí termina la sentencia”. Como dentro de un procedimiento usas muchos ;, cambiar el delimitador temporalmente a $$ evita que el cliente “corte” antes de tiempo.

La UNIQUE (nombre) garantiza que el nombre identifica al producto para tus SP (si no quieres unicidad, avísame y ajusto los SP para manejar múltiples coincidencias).

En sp_producto_crear se “reactiva” si ya existía con ese nombre pero estaba inactivo.

En sp_producto_actualizar_por_nombre usa NULL para “no tocar” ese campo. Ej.: actualizar solo stock: CALL sp_producto_actualizar_por_nombre('Lapiz', NULL, 100);

La función fn_producto_id_por_nombre('Lapiz') devuelve -1 si no existe activo.
*/
