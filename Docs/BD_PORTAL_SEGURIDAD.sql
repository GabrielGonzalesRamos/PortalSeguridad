CREATE TABLE IF NOT EXISTS tb_usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    correo VARCHAR(120) NOT NULL,
    password TEXT NOT NULL,
    CONSTRAINT constraint_correo CHECK (correo ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    CONSTRAINT constraint_correo_unique UNIQUE (correo)
);

CREATE TABLE IF NOT EXISTS tb_sesion (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    vencimiento DATE NOT NULL
);
