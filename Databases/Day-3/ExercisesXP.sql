--1
-- SELECT name FROM language


--2 films with no langauges
--  SELECT film.title, film.description, language.name
--  FROM film
--  RIGHT JOIN language
--  ON film.language_id = language.language_id
--  WHERE language.name is NULL


--no films in languages -- starts after row 1001
-- SELECT film.title, film.description language.name, 
-- FROM language 
-- FULL OUTER JOIN film 
-- ON language.language_id = film.language_id

-- OR 

-- SELECT film.title,film.description, language.name
-- FROM language 
-- LEFT JOIN film 
-- ON language.language_id = film.language_id

--3
-- CREATE TABLE new_film (
-- id SERIAL PRIMARY KEY,
-- name VARCHAR(50) NOT NULL
-- )

-- INSERT INTO new_film (name)
-- VALUES ('A Beautiful Mind'),
-- ('Wolf of Wall Street'),
-- ('Devil Wears Prada')

--4
-- CREATE TABLE customer_review(
-- review_id SERIAL NOT NULL,
-- film_id INTEGER NOT NULL,
-- language_id INTEGER NOT NULL,
-- title VARCHAR(50) NOT NULL,
-- score INT,
-- review TEXT NOT NULL,
-- last_update DATE,
-- PRIMARY KEY (review_id,film_id, language_id),
-- FOREIGN KEY (film_id) REFERENCES new_film(id) ON UPDATE CASCADE ON DELETE CASCADE,
-- FOREIGN KEY (language_id) REFERENCES language(language_id) ON UPDATE CASCADE    
-- )

--5
-- INSERT into customer_review(film_id, language_id, title, score, review, last_update) VALUES 
-- ((SELECT id FROM new_film where id = 2 ), 
-- (SELECT language_id FROM language where language_id = 4), 'A Beauiful Mind', 10, 'Amazing movie and very touching', '2022-07-26')

-- INSERT into customer_review(film_id, language_id, title, score, review, last_update) VALUES 
-- ((SELECT id FROM new_film where id = 3 ), 
-- (SELECT language_id FROM language where language_id = 5), '12 Years a Slave', 10, 'Amazing movie and very touching', '2022-07-26')

--6
-- DELETE FROM new_film where id = 2
-- A row in with a film id = 2 was deleted from the customer review table


-------------------EXERCISE 2----------------------------
--1
-- UPDATE language SET name = 'Arabic' WHERE language_id = 6;

--2


--3
-- DROP TABLE IF EXISTS customer_review;

--4
-- SELECT COUNT(inventory_id)
-- FROM rental
-- WHERE return_date IS NULL;

--5
-- SELECT rental.inventory_id, film.rental_rate, film.title
-- FROM rental
-- INNER JOIN inventory
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN film
-- ON film.film_id = inventory.film_id
-- WHERE film.rental_rate = (SELECT MAX(rental_rate) FROM film)
-- AND return_date IS NULL
-- GROUP BY film.rental_rate, rental.inventory_id, film.title
-- LIMIT 30;

--6
--First film = Park Citizen
--  SELECT film.film_id, film.title 
-- FROM film
-- INNER JOIN film_actor
-- ON film.film_id = film_actor.film_id
-- INNER JOIN actor
-- ON film_actor.actor_id = actor.actor_id
-- WHERE first_name = 'Penelope' AND last_name = 'Monroe'
-- AND description ILIKE '%sumo%'



--Second film = Crossing Divorce
-- SELECT title, rating, length
-- FROM film 
-- WHERE rating = 'R'
-- AND description ILIKE '%documentary%'
-- AND length < 60


--Third film = Sugar Wonka
--  SELECT title
-- FROM film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN payment
-- ON payment.rental_id = rental.rental_id
-- INNER JOIN customer
-- ON customer.customer_id = payment.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND payment.amount > 4.00
-- AND return_date between '2005-07-28' and '2005-08-01'

--Fourth Film: Probably Stone Fire
-- max replacement_cost query line 140 not working
-- SELECT film.title, MAX(film.replacement_cost)
-- from film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN customer
-- ON customer.customer_id =  rental.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- -- AND film.title ILIKE '%boat%'
-- AND film.description ILIKE '%boat%'
-- -- AND film.replacement_cost = (SELECT MAX(replacement_cost) FROM film)
-- GROUP BY film.title, film.replacement_cost

