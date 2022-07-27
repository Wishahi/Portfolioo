---------------FIRST PART: BASIC SELECT STATEMENT--------------
--1
-- SELECT first_name AS "First Name", last_name AS "Last Name"
-- FROM employees

--2
-- SELECT distinct department_id FROM employees

--3
-- SELECT * FROM employees
-- ORDER BY first_name DESC

--4
-- SELECT first_name, last_name, salary, salary*.15 AS PF
-- FROM employees

--5
-- SELECT employee_ID, first_name || ' ' || last_name as Names, salary
-- FROM employees
-- ORDER BY salary ASC

--6
-- SELECT SUM(salary) as "Total Salary"
-- FROM employees

--7
-- SELECT MAX(salary), MIN(salary)
-- FROM employees

--8
-- SELECT AVG(salary)
-- FROM employees

--9 
-- SELECT COUNT(employee_id)
-- FROM employees

--10
-- SELECT UPPER(first_name)
-- FROM employees

--11
-- SELECT SUBSTRING(first_name,1,3)
-- FROM employees

--12
-- SELECT first_name, last_name, first_name || ' ' || last_name AS "Full Name"
-- FROM employees

--13
-- SELECT first_name, last_name, length(first_name) + LENGTH(last_name) "Length of Name"
-- FROM employees

--14
-- SELECT first_name 
-- FROM employees 
-- WHERE  first_name ~  '[0-9]';

--15
-- SELECT employee_id, first_name, last_name
-- FROM employees
-- LIMIT 10


------------SECOND PART: RESTRICTING AND SORTING---------------

--1
-- SELECT first_name, last_name, salary 
-- FROM employees
-- WHERE salary BETWEEN 10000 AND 15000

--2
-- SELECT first_name, last_name, hire_date	
-- FROM employees
-- WHERE EXTRACT(YEAR FROM hire_date) IN (1987);

--3
-- SELECT  employee_id,first_name, last_name
-- FROM employees
-- WHERE first_name like '%c%' AND first_name like '%e%';

--4
-- SELECT employees.last_name, jobs.job_title, employees.salary
-- FROM employees
-- INNER JOIN jobs
-- ON employees.job_id = jobs.job_id
-- WHERE jobs.job_title IN ('Programmer', 'Shipping Clerk')
-- AND employees.salary NOT IN(4500, 10000, 15000)

--5 
-- SELECT last_name
-- FROM employees
-- WHERE LENGTH(last_name) = 6 

--6
-- SELECT last_name
-- FROM employees
-- WHERE last_name LIKE '__e%'

--7
-- SELECT distinct jobs.job_title
-- FROM employees
-- INNER JOIN jobs
-- ON employees.job_id = jobs.job_id


--8
-- SELECT *
-- FROM employees
-- WHERE last_name IN('Jones', 'Blake', 'Scott', 'King', 'Ford')



