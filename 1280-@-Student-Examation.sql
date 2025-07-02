# Write your MySQL query statement below
Select s.student_id, s.student_name, sub.subject_name , count(ex.student_id) as attended_exams from Students s Cross Join Subjects sub Left join  Examinations ex on s.student_id=ex.student_id  and sub.subject_name=ex.subject_name group by  s.student_id,sub.subject_name, ex.subject_name order by s.student_id,  sub.subject_name Asc ;

