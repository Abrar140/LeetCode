# Write your MySQL query statement below
Select query_name , Round(AVG(rating/position),2) as quality,
 Round(SUm(case when rating<3 then 1 else 0 end) *100.0 /count(*),2)   as poor_query_percentage from Queries group by query_name

