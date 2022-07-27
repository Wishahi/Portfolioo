--1+2
-- CREATE TABLE product_orders(
-- product_id SERIAL,
-- product_name VARCHAR(20),
-- product_inStock BOOLEAN,
-- PRIMARY KEY (product_id)    
-- )

-- CREATE TABLE items(
-- item_id SERIAL,
-- fk_product_id INTEGER NOT NULL,    
-- product VARCHAR(50) NOT NULL,
-- price FLOAT NOT NULL,    
-- PRIMARY KEY (item_id),
-- FOREIGN KEY (fk_product_id) REFERENCES product_orders(product_id) ON DELETE CASCADE
-- )

-- INSERT INTO product_orders(product_name, product_inStock) 
-- VALUES 
-- ('Cornflakes', TRUE),
-- ('Chips',TRUE),
-- ('Pasta',TRUE),
-- ('Rice',FALSE),
-- ('Cookies',FALSE),
-- ('Bread',TRUE )

-- INSERT INTO items (fk_product_id, product, price)
-- VALUES 
-- ((SELECT product_id FROM product_orders where product_id = 1 ), 'Cornflakes', 15), 
-- ((SELECT product_id FROM product_orders where product_id = 2 ), 'Chips', 3), 
-- ((SELECT product_id FROM product_orders where product_id = 3 ), 'Pasta', 10), 
-- ((SELECT product_id FROM product_orders where product_id = 4 ), 'Rice', 7), 
-- ((SELECT product_id FROM product_orders where product_id = 5 ), 'Cookies', 5), 
-- ((SELECT product_id FROM product_orders where product_id= 6 ), 'Bread', 4)


--3
-- CREATE or REPLACE FUNCTION total_price(prct varchar(50))
-- RETURNS INT AS $totalprice$
-- BEGIN
--    RETURN(SELECT SUM(items.price) FROM items WHERE items.product = prct);
-- END;
-- $totalprice$ LANGUAGE plpgsql;

-- SELECT * FROM total_price('Cornflakes')

--4:BONUS
--1+2
-- CREATE TABLE users(
-- user_id serial,
-- fk_product_id INTEGER NOT NULL,    
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL, 
-- PRIMARY KEY (user_id),
-- FOREIGN KEY (fk_product_id) REFERENCES product_orders(product_id) ON DELETE CASCADE
-- )

-- INSERT INTO users (fk_product_id, first_name, last_name)
-- VALUES
-- ((SELECT product_id FROM product_orders where product_id = 1 ), 'John', 'Smith'), 
-- ((SELECT product_id FROM product_orders where product_id = 2 ), 'Leen', 'Wishahi'), 
-- ((SELECT product_id FROM product_orders where product_id = 3 ), 'Lea', 'Lalu'), 
-- ((SELECT product_id FROM product_orders where product_id = 4 ), 'Scott', 'Travis'), 
-- ((SELECT product_id FROM product_orders where product_id = 5 ), 'Jerome', 'Cohen'), 
-- ((SELECT product_id FROM product_orders where product_id = 6 ), 'Ziv', 'Yossi') 


--3: Does not work 
-- CREATE or REPLACE FUNCTION total_price2(prct varchar(50), fn varchar(50), lan varchar(100))
-- RETURNS INT AS $totalprice$
-- BEGIN
--    RETURN(SELECT items.price FROM items WHERE items.product = prct),
--    INNER JOIN users
--    ON users.fk_product_id = product_orders.product_id,
--   INNER JOIN items
--    ON items.fk_product_id =  product_orders.product_id
-- (SELECT users.first_name = fn AND users.last_name=lan FROM users);

-- END;
-- $totalprice$ LANGUAGE plpgsql;

-- SELECT * FROM total_price2('Cornflakes', 'John', 'Smith')

