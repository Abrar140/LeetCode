# Write your MySQL query statement below
Select *  from products where 
description REGEXP '\\bSN[0-9]{4}-[0-9]{4}\\b'
order by product_id

