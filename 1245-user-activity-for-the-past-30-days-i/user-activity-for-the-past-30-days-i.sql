# Write your MySQL query statement below
SELECT 
    A.activity_date as day,
    COUNT(DISTINCT A.user_id) as active_users
FROM
    Activity A
WHERE 
    DATEDIFF('2019-07-27',A.activity_date) < 30 AND DATEDIFF('2019-07-27',A.activity_date) >= 0
GROUP BY
    A.activity_date