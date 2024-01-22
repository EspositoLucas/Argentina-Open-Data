CREATE TABLE IF NOT EXISTS raw( 
    job_date date PRIMARY KEY, 
    cod_localidad Integer NOT NULL, 
    id_provincia Integer NOT NULL, 
    id_departamento Integer NOT NULL, 
    categoria VARCHAR(255) NOT NULL, 
    provincia VARCHAR(255) NOT NULL, 
    localidad VARCHAR(255) NOT NULL, 
    nombre VARCHAR(255) NOT NULL, 
    domicilio VARCHAR(255) NOT NULL, 
    codigo VARCHAR(255) NOT NULL, 
    número VARCHAR(255) NOT NULL, 
    mail VARCHAR(255) NOT NULL, 
    web VARCHAR(255) NOT NULL
);