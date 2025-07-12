-- -- # Write your MySQL query statement below

-- Select e.employee_id , e.name  ,count(e.reports_to) as reports_count, avg(e.age) as average_age from Employees  e where e.employee_id IN (Select e1.reports_to from Employees e1 where e1.reports_to =e.employee_id ) is not null group by e.employee_id


SELECT 
  e.employee_id,
  e.name,
  COUNT(r.employee_id) AS reports_count,
  ROUND(AVG(r.age)) AS average_age
FROM Employees e
JOIN Employees r
  ON e.employee_id = r.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id;


