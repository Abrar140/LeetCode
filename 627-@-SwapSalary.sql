# Write your MySQL query statement below
UPDATE Salary
set sex=Case
  when sex='m' then 'f' 
  else 'm' 
end;
