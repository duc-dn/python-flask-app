
DROP DATABASE IF EXISTS ProductManagement;
CREATE DATABASE ProductManagement;
USE ProductManagement;

CREATE TABLE tblProduct 
(
    pro_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description VARCHAR(255)
);

INSERT INTO tblProduct (name, description) VALUES
('Banh', 'banh ngon banh ngon'),
('Keo', 'keo thom'),
('Nuoc ngot', 'tinh tao tinh than');