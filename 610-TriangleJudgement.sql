# Write your MySQL query statement below
Select *, (If(x+y>z and x+z>y and y+z>x, "Yes","No")) as triangle from Triangle