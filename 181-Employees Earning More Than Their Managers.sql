# Write your MySQL query statement below
Select e.name as Employee from Employee e where e.salary> (Select e1.salary from Employee e1 where e.managerId=e1.id )