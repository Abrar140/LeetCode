# Write your MySQL query statement below
Select max(num) as num from (Select num from MyNumbers group by num having count(num)=1) AS unique_nums;



