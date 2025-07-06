# Write your MySQL query statement below

Select p.product_name , sum(o.unit) as unit from Products p JOIN Orders o ON p.product_id = o.product_id 
where o.order_date LIke '2020-02-%' 
group by p.product_id 
having sum(o.unit)>=100
