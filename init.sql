CREATE TABLE personas (
    id_personas INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO personas (nombre,email) VALUES
('Dejah Thoris', 'dejah@email.com'),
('John Carter', 'john@email.com');