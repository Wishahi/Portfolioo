--1
-- CREATE TABLE customer (
-- id serial PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL    
-- )

--  CREATE TABLE customer_profile(
-- customer_profile_id SERIAL,
-- customer_id INTEGER NOT NULL,     
-- isLoggedIn BOOLEAN default false,  
-- PRIMARY KEY (customer_profile_id, customer_id),
-- FOREIGN KEY (customer_id) REFERENCES customer(id) ON UPDATE CASCADE ON DELETE CASCADE
-- )

--2
--  INSERT into customer(first_name, last_name) VALUES 
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

--3
--  INSERT into customer_profile(customer_id, isLoggedIn) VALUES 
-- ((SELECT id FROM customer where id = 1 ), 'TRUE'), 
-- ((SELECT id FROM customer where id = 2 ), 'FALSE') 

-- select * from customer
-- select * from  customer_profile

--4
-- SELECT first_name 
-- FROM customer
-- INNER JOIN customer_profile
-- ON customer.id = customer_profile.customer_id
-- WHERE isLoggedIn IS TRUE

-- SELECT first_name, isLoggedIn 
-- FROM customer
-- FULL OUTER JOIN customer_profile
-- ON customer.id = customer_profile.customer_id

--Should be 2?
-- SELECT COUNT(customer.id)
-- FROM customer
-- LEFT JOIN customer_profile
-- ON customer.id = customer_profile.customer_id
-- WHERE isLoggedIn IS false


----------PART 2----------------
--1
-- CREATE TABLE book(
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR(100) NOT NULL,
-- author VARCHAR(100) NOT NULL    
-- )

--2
-- INSERT INTO book(title, author) 
-- VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To Kill A Mockingbird', 'Harper Lee')

--3
-- CREATE TABLE Student(
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR(50) NOT NULL UNIQUE,
-- AGE int CHECK(Age<=15)    
-- )

--4
-- INSERT INTO Student(name, age)
-- VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14)

--5
-- CREATE TABLE library (
-- book_fk_id INTEGER NOT NULL,
-- student_fk_id INTEGER NOT NULL, 
-- borrowed_date DATE,
-- PRIMARY KEY(book_fk_id,student_fk_id),
-- FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON UPDATE CASCADE ON DELETE CASCADE,   
-- FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON UPDATE CASCADE ON DELETE CASCADE    
-- )

--6
-- INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES 
-- ((SELECT book_id FROM book where book_id = 1 ), 
-- (SELECT student_id FROM student where student_id = 6), '2022-02-15')

-- INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES 
-- ((SELECT book_id FROM book where book_id = 3 ), 
-- (SELECT student_id FROM student where student_id = 9), '2021-03-03')

-- INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES 
-- ((SELECT book_id FROM book where book_id = 1 ), 
-- (SELECT student_id FROM student where student_id = 7), '2021-05-23')

-- INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES 
-- ((SELECT book_id FROM book where book_id = 2 ), 
-- (SELECT student_id FROM student where student_id = 9), '2021-08-12')

-- select * from library

--7
-- select student.name, book.title
-- from student
-- inner join library
-- ON student.student_id = library.student_fk_id
-- inner join book
-- on book.book_id = library.book_fk_id

-- SELECT avg(age) 
-- from student
-- inner join library
-- ON student.student_id = library.student_fk_id
-- inner join book
-- on book.book_id = library.book_fk_id
-- WHERE book.title ='Alice In Wonderland'

-- DELETE FROM student where student_id = 6
--The whole row that was associated with student_id=6 was deleted 

-- select*from student
-- select * from library

