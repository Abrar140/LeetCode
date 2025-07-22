# Write your MySQL query statement below

Select  customer_id from  Customer  group by customer_id Having count(distinct product_key)= (Select count(*) from Product)
