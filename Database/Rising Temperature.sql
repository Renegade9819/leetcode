SELECT 
    w1.Id
FROM  Weather w1 INNER JOIN Weather w2
    ON 
        (w1.recordDate - 1) = w2.recordDate AND
        w1.Temperature > w2. Temperature;
    
