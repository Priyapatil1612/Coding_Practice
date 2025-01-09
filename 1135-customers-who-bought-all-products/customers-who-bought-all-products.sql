# Write your MySQL query statement below
SELECT 
    C.customer_id
FROM
    Product P
LEFT JOIN
    Customer C
ON 
    P.product_key = C.product_key
GROUP BY 
    C.customer_id
HAVING
    COUNT(DISTINCT C.product_key) = (SELECT COUNT(*) FROM Product);