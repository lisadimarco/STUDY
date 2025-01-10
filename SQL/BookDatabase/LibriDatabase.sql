-- Creazione del database e utilizzo
CREATE DATABASE libri_database;
USE libri_database;

-- Creazione della tabella books_2024
CREATE TABLE books_2024 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE,
    rating REAL DEFAULT NULL
);

-- Inserimento dei libri del 2024
INSERT INTO books_2024 (id, name, author, read, rating)
VALUES 
(1, 'Memorie, sogni, riflessioni', 'Carl Gustav Jung', '2024-12-30', 9),
(2, 'Io, te e amore', 'Stefania Andreoli', '2024-07-26', 7),
(3, 'Diagnosi psicodinamica e tecnica analitica', 'Alfred Adler', '2024-03-26', 7),
(4, 'Lo squalificato', 'Osamu Dazai', '2024-02-15', 9),
(5, 'Python Crash Course', 'Eric Matthes', '2024-11-29', NULL);

-- Creazione della tabella books_2023
CREATE TABLE books_2023 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE,
    rating REAL
);

-- Inserimento dei libri del 2023
INSERT INTO books_2023 (id, name, author, read, rating)
VALUES
(1, 'Lettere al padre', 'Franz Kafka', NULL, 9),
(2, 'Metamorfosi', 'Franz Kafka', NULL, 9),
(3, 'Lettere a Milena', 'Franz Kafka', '2023-06-20', 9),
(4, 'Cecità', 'José Saramago', NULL, 9.5),
(5, 'The Laws of Human Nature', 'Robert Greene', NULL, 8),
(6, 'Il viaggio di Eros e Psiche', 'Orietta Cecchini', NULL, 6.5),
(7, 'Daily Stoic', 'Ryan Holiday', '2023-12-31', 8);

-- Creazione della tabella books_2022
CREATE TABLE books_2022 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE,
    rating REAL
);

-- Inserimento dei libri del 2022
INSERT INTO books_2022 (id, name, author, read, rating)
VALUES
(1, 'Le notti bianche', 'Fëdor Dostoevskij', NULL, 8),
(2, 'Lo faccio per me', 'Stefania Andreoli', NULL, 7),
(3, 'Mio figlio è normale?', 'Stefania Andreoli', NULL, 7),
(4, 'Profumologia', 'Sinister', NULL, 5);

-- Creazione della tabella books_2021
CREATE TABLE books_2021 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE,
    rating REAL
);

-- Inserimento dei libri del 2021
INSERT INTO books_2021 (id, name, author, read, rating)
VALUES
(1, 'Le affinità elettive', 'Goethe', NULL, 8),
(2, 'I dolori del giovane Werther', 'Goethe', NULL, 9),
(3, 'La coscienza di Zeno', 'Italo Svevo', NULL, 9),
(4, 'Il fu Mattia Pascal', 'Luigi Pirandello', NULL, 9);

-- Creazione della tabella books_2020
CREATE TABLE books_2020 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE,
    rating REAL
);

-- Inserimento dei libri del 2020
INSERT INTO books_2020 (id, name, author, read, rating)
VALUES
(1, 'Il ritratto di Dorian Gray', 'Oscar Wilde', NULL, 9),
(2, 'La teoria del tutto', 'Stephen Hawking', NULL, 7),
(3, 'Delitto e castigo', 'Fëdor Dostoevskij', NULL, 9)
