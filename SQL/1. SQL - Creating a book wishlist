-- Creazione della tabella books_wishlist
CREATE TABLE books_wishlist (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    read DATE DEFAULT NULL
);

-- Inserimento dei primi due libri
INSERT INTO books_wishlist (id, name, author, read)
VALUES 
(1, 'The Metamorphosis', 'Kafka', '2023-08-12'),
(2, 'Memories, Dreams, Reflections', 'Jung', '2024-09-15');

-- Aggiunta della colonna rating con valore numerico predefinito
ALTER TABLE books_wishlist
ADD COLUMN rating INTEGER DEFAULT NULL;

-- Aggiornamento delle valutazioni per i primi due libri
UPDATE books_wishlist
SET rating = 9 
WHERE id = 1;

UPDATE books_wishlist
SET rating = 8 
WHERE id = 2;

-- Inserimento dei libri letti e non letti
INSERT INTO books_wishlist (id, name, author, read, rating)
VALUES 
(3, 'Thus Spoke Zarathustra', 'Friedrich Nietzsche', '2023-01-01', NULL),
(4, 'Beyond Good and Evil', 'Friedrich Nietzsche', '2023-01-01', NULL),
(5, 'The Gay Science', 'Friedrich Nietzsche', NULL, NULL),
(6, 'On the Genealogy of Morality', 'Friedrich Nietzsche', NULL, NULL),
(7, 'The Dawn of Day', 'Friedrich Nietzsche', NULL, NULL),
(8, 'The Will to Power', 'Friedrich Nietzsche', NULL, NULL),
(9, 'Letters to Milena', 'Kafka', NULL, NULL),
(10, 'Letters to His Father', 'Kafka', NULL, NULL),
(11, 'The Trial', 'Kafka', NULL, NULL);

-- Aggiunta di una colonna wishlist (1 = nella wishlist, 0 = non nella wishlist)
ALTER TABLE books_wishlist
ADD COLUMN wishlist BOOLEAN DEFAULT 1;

-- Impostazione della wishlist a 0 per i libri che sono già stati letti
UPDATE books_wishlist
SET wishlist = 0
WHERE read IS NOT NULL;

-- Inserimento di libri di Sapolsky e altri libri mescolati
INSERT INTO books_wishlist (id, name, author, read, rating, wishlist)
VALUES 
(12, 'Behave: The Biology of Humans at Our Best and Worst', 'Robert Sapolsky', NULL, NULL),
(13, 'Why Zebras Don’t Get Ulcers', 'Robert Sapolsky', NULL, NULL),
(14, 'A Primate’s Memoir', 'Robert Sapolsky', NULL, NULL),
(15, 'The Portrait of Dorian Gray', 'Oscar Wilde', NULL, NULL),
(16, 'Blindness', 'José Saramago', NULL, NULL),
(17, 'The Theory of Everything', 'Stephen Hawking', NULL, NULL),
(18, 'One, No One and One Hundred Thousand', 'Luigi Pirandello', NULL, NULL),
(19, 'The Late Mattia Pascal', 'Luigi Pirandello', NULL, NULL),
(20, 'The Man Who Mistook His Wife for a Hat', 'Oliver Sacks', NULL, NULL);


SELECT id, name, author, read, rating, wishlist
       CASE 
           WHEN wishlist = 1 THEN 'Sì'
           WHEN wishlist = 0 THEN 'No'
       END AS wishlist_status
FROM books_wishlist;



