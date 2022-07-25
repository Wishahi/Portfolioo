-- SELECT * FROM customer

-- SELECT CONCAT(first_name,' ',last_name) AS full_name FROM customer

-- SELECT DISTINCT create_date from customer

-- SELECT * FROM customer ORDER BY first_name DESC

-- SELECT film_id, title, description, release_year, rental_rate 
-- FROM film
-- ORDER BY rental_rate ASC 

-- SELECT address, phone FROM address WHERE district = 'Texas'

-- SELECT * FROM film WHERE film_id = 15 OR film_id = 150 

-- SELECT film_id, title, description, length, rental_rate from film WHERE title = 'Devil Wears Prada'

-- SELECT film_id, title, description, length, rental_rate from film WHERE title LIKE 'De%'

-- -- SELECT * FROM film
--  WHERE rental_rate = (SELECT MIN(rental_rate) FROM film) 
--  LIMIT 10;

-- SELECT * FROM film
--  WHERE rental_rate = (SELECT MIN(rental_rate) FROM film) 
--  LIMIT 10 OFFSET 10;

-- SELECT amount, payment_date
-- FROM payment
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- ORDER BY payment.customer_id ASC

--  SELECT city.city, country
-- FROM country
-- INNER JOIN city
-- ON country.country_id = city.country_id

--  SELECT customer.customer_id, customer.first_name, customer.last_name, amount, payment_date, staff.staff_id
-- FROM payment
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- INNER JOIN staff
-- ON payment.staff_id = staff.staff_id
-- ORDER BY staff.staff_id 

