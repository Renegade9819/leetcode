/*
able: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Name        | varchar |
| Salary      | int     |
| ManagerId   | int     |
+-------------+---------+
Id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

 

Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

*/

Solution 1 - 

select e1.name as employee
from employee e1
where salary > (select e2.salary
            from employee e2
               where e1.ManagerId = e2.Id)
               

