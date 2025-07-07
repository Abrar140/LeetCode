# Write your MySQL query statement below
Select p.project_id , Round(Avg(e.experience_years),2)as average_years
from Project p, Employee e where  e.employee_id=p.employee_id group by p.project_id