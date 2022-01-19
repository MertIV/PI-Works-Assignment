SELECT e.FirstName, e.LastName,sum(value) as total_amount
FROM Employee as e
INner JOIN Payments as p on e.employee_id == p.Employee_ID
GROUP By e.Employee_ID