WITH ranked AS (
    SELECT
        departmentId,
        name,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee
)
SELECT
    d.name AS Department,
    r.name AS Employee,
    r.salary AS Salary
FROM ranked r
JOIN Department d
    ON r.departmentId = d.id
WHERE r.rnk <= 3;