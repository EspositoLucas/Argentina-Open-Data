CREATE TABLE IF NOT EXISTS size_by_datasource( 
    job_date date PRIMARY KEY, 
    source VARCHAR(255) NOT NULL,
    count VARCHAR(255) NOT NULL  
);