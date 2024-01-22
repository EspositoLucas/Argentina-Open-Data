CREATE TABLE IF NOT EXISTS cine_insights( 
    job_date date PRIMARY KEY, 
    provincia VARCHAR(255) NOT NULL, 
    cant_pantallas VARCHAR(255) NOT NULL,
    cant_butacas VARCHAR(255) NOT NULL,
    cant_espacios_incaa VARCHAR(255) NOT NULL  
);