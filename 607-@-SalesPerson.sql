# Write your MySQL query statement below
Select  name from SalesPerson where sales_id NOT IN(Select o.sales_id from Orders o join Company c     on c.com_id=o.com_id where c.name="RED"  )