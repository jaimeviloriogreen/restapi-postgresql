DROP DATABASE IF EXISTS products_rest_api;

CREATE DATABASE products_rest_api;

DROP TABLE IF EXISTS products;

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(6,2) NOT NULL,
    qty SMALLINT NOT NULL
);

INSERT INTO products(
    name, 
    price, 
    qty
)VALUES
    ('Laptop', 899.99, 8); 