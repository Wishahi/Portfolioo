


-- CREATE DATABASE "Hollywood"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United Kingdom.1252'
--     LC_CTYPE = 'English_United Kingdom.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- CREATE TABLE actors(
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL    
-- )



-- INSERT INTO actors (first_name, last_name, age, number_oscars)

-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Meeryl','Streep','1949-06-22', 3);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Katherine','Hepburn','1907-05-12', 4);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Denzel','Washington','1954-12-28', 3),
-- ('Will', 'Smith','1968-09-25',4),
-- ('Renee', 'Zellweger', '1969-04-25', 2)

-- SELECT * FROM actors


-- SELECT * FROM actors LIMIT 4;
-- SELECT * FROM actors ORDER BY last_name DESC LIMIT 4;
-- SELECT * FROM actors WHERE first_name LIKE '%e%';
-- SELECT * FROM actors WHERE number_oscars >= '5'


-- SELECT count (*) from actors;

--GIVES SYNTAX ERROR
--  INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('','','', );





