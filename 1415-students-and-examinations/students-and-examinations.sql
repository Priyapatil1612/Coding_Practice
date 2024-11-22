# Write your MySQL query statement below
SELECT 
    ST.student_id,
    ST.student_name,
    S.subject_name,
    COUNT(E.subject_name) AS attended_exams
FROM 
    Students ST
CROSS JOIN
    Subjects S
LEFT JOIN
    Examinations E
ON 
    ST.student_id = E.student_id AND S.subject_name = E.subject_name
GROUP BY
    ST.student_name, ST.student_id,S.subject_name
ORDER BY
    ST.student_id, S.subject_name