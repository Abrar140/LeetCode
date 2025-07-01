# Write your MySQL query statement below

SELECT e.employee_id 
FROM Employees e 
LEFT JOIN Salaries s ON e.employee_id = s.employee_id
where s.salary is NULL

UNION

SELECT s.employee_id 
FROM Employees e 
RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
where e.name is NULL

Order by employee_id;


1


-- select employee_id from employees where employee_id not in (select employee_id from salaries )
-- union
-- select employee_id from salaries where employee_id not in (select employee_id from employees)
-- order by employee_id;