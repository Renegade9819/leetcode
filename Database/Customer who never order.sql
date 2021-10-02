Solution 1 - 

SELECT
    Name as Customers
FROM
    Customers c
WHERE
    c.Id NOT IN (
            SELECT o.CustomerId
            FROM Orders o
            )

Solution 2 - 

SELECT
    Name as Customers
FROM
    Customers c LEFT JOIN Orders o
    ON c.Id = o.CustomerId
WHERE
    o.CustomerID IS NULL
