CREATE TABLE IF NOT EXISTS size_by_category( 
    job_date date PRIMARY KEY, 
    categoria VARCHAR(255) NOT NULL, 
    size VARCHAR(255) NOT NULL 
);