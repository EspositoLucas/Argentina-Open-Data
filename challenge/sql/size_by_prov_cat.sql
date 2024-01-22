CREATE TABLE IF NOT EXISTS size_by_prov_cat( 
    job_date date PRIMARY KEY, 
    categoria VARCHAR(255) NOT NULL, 
    provincia VARCHAR(255) NOT NULL, 
    size VARCHAR(255) NOT NULL
);