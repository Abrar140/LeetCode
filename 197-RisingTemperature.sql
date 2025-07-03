# Write your MySQL query statement below

Select w.id from Weather w where w.temperature> (Select temperature from Weather where recordDate =DATE_SUB(w.recordDate, INTERVAL 1 DAY));
