# Write your MySQL query statement below
Select machine_id, Round(AVG(times),3) as processing_time from 
(Select machine_id, process_id,
Max(Case when activity_type='end' then timestamp end)-Min(Case when activity_type='start' then timestamp end) as 
times from Activity group by machine_id, process_id) As sub group by machine_id

