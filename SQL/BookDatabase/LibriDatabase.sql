CREATE DATABASE libri_database;
USE libri_database;


CREATE TABLE books_2024 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE
);

-- Inserimento dei primi due libri
INSERT INTO books_2024 (id, name, author, read)
VALUES 
(1, 'Memorie, sogni, riflessioni', 'Carl Gustav Jung', '2024-12-30');

-- Aggiunta della colonna rating con valore numerico predefinito
ALTER TABLE books_2024
ADD COLUMN rating FLOAT DEFAULT NULL;

-- Aggiornamento delle valutazioni per il primo libro
UPDATE books_2024
SET rating = 9 
WHERE id = 1;

-- Inserimento dei libri letti
INSERT INTO books_2024 (id, name, author, read, rating)
VALUES 
(2, 'Io, te e amore', 'Stefania Andreoli', '2024-07-26', 7),
(3, 'Diagnosi psicodinamica e tecnica analitica', 'Alfred Adler', '2024-03-26', 7),
(4, 'Lo squalificato', 'Osamu Dazai', '2024-02-15', 9)
(5, 'Python Crash Course', 'Eric Matthes', '2024-11-29');


CREATE TABLE books_2023 (
  id INTEGER PRIMARY KEY,
  name TEXT,
  author TEXT,
  read DATE,
  rating FLOAT
  );

INSERT INTO books_2023 (id, name, author, read, rating)
VALUES
(1, 'Lettere al padre', 'Franz Kafka', null, 9),
(2, 'Metamorfosi', 'Franz Kafka', null, 9),
(3, 'Lettere a Milena', 'Franz Kafka', '2023-06-20', 9),
(4, 'Cecità', 'Josè Saramago', null, 9.5),
(5, 'The laws of human nature', 'Robert Greene', null, 8),
(6, 'Il viaggio di Eros e Psiche', 'Orietta Cecchini', null, 6.5),
(7, 'Daily Stoic', 'Ryan Holiday', '2023-12-31', 8);

CREATE TABLE books_2022 (
  id INTEGER PRIMARY KEY,
  name TEXT,
  author TEXT,
  read DATE,
  rating FLOAT
  );

INSERT INTO books_2022 (id, name, author, read, rating)
VALUES
(1, 'Le notti bianche', 'Fëdor Dostoevskij', null, 8),
(2, 'Lo faccio per me', 'Stefania Andreoli', null, 7),
(3, 'Mio figlio è normale?', 'Stefania Andreoli', null, 7),
(4, 'Profumologia', 'Sinister', null, 5);

CREATE TABLE books_2021 (
  id integer primary key,
  name text,
  author text,
  read date,
  rating float
  );

INSERT INTO books_2021 (id, name, author, read, rating)
VALUES
(1, 'Le affinità elettive', 'Goethe', null, 8),
(2, 'I dolori del giovane Werther', 'Goethe' null, 9),
(3, 'La coscienza di Zeno', 'Italo Svevo', null, 9),
(4, 'Il fu Mattia Pascal', 'Luigi Pirandello', null, 9);

CREATE TABLE books_2020 (
  id integer primary key,
  name text,
  author text,
  read date,
  rating float
  );

INSERT INTO books_2020 (id, name, author, read, rating)
VALUES
(1, 'Il ritratto di Dorian Gray', 'Oscar Wilde', null, 9),
(2, 'La teoria del tutto', 'Stephen Awking', null, 7),
(3, 'Delitto e castigo', 'Fëdor Dostoevskij', null, 9);
