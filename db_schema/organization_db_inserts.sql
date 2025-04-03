INSERT INTO Departments (DepartmentName, Location) VALUES
('Engineering', 'New York'),
('Marketing', 'Los Angeles'),
('HR', 'San Francisco'),
('Sales', 'Chicago');

INSERT INTO Roles (RoleName, Salary) VALUES
('Software Engineer', 90000.00),
('Marketing Manager', 85000.00),
('HR Specialist', 75000.00),
('Sales Associate', 65000.00);

INSERT INTO Employees (FirstName, LastName, Email, Phone, HireDate, DepartmentID, RoleID) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2020-05-15', 1, 1),
('Jane', 'Smith', 'jane.smith@example.com', '123-456-7891', '2019-08-21', 2, 2),
('Robert', 'Brown', 'robert.brown@example.com', '123-456-7892', '2021-02-11', 3, 3),
('Emily', 'Davis', 'emily.davis@example.com', '123-456-7893', '2018-07-30', 4, 4),
('Michael', 'Wilson', 'michael.wilson@example.com', '123-456-7894', '2022-01-10', 1, 1),
('Sarah', 'Miller', 'sarah.miller@example.com', '123-456-7895', '2020-09-05', 2, 2),
('David', 'Anderson', 'david.anderson@example.com', '123-456-7896', '2021-06-18', 3, 3),
('Laura', 'Thomas', 'laura.thomas@example.com', '123-456-7897', '2019-11-25', 4, 4);

INSERT INTO Projects (ProjectName, StartDate, EndDate, Budget) VALUES
('AI Research', '2023-01-01', '2024-01-01', 500000.00),
('Marketing Campaign', '2022-06-15', '2023-06-15', 200000.00),
('Employee Onboarding', '2021-03-01', '2022-03-01', 100000.00),
('Sales Expansion', '2023-07-10', '2024-07-10', 300000.00);

INSERT INTO Employee_Project (EmployeeID, ProjectID, AssignmentDate) VALUES
(1, 1, '2023-01-10'),
(2, 2, '2022-07-01'),
(3, 3, '2021-04-01'),
(4, 4, '2023-08-01'),
(5, 1, '2023-02-15'),
(6, 2, '2022-08-05'),
(7, 3, '2021-05-10'),
(8, 4, '2023-09-15');
