SELECT employee_id, 
       IF(MOD(employee_id, 2) = 1 and name NOT LIKE 'M%', salary, 0) AS bonus 
FROM Employees Order by employee_id Asc;
