# Write your MySQL query statement below
SELECT
    Q.query_name,
    ROUND(AVG(Q.rating/Q.position),2) AS quality,
    ROUND(AVG(Q.rating<3)*100,2) AS poor_query_percentage
FROM
    Queries Q
GROUP BY
    Q.query_name