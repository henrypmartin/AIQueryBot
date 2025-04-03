
-- Insert sample data into Departments
INSERT INTO Departments (Name, Description) VALUES
('Computer Science', 'Department of Computer Science'),
('Mathematics', 'Department of Mathematics'),
('Physics', 'Department of Physics');

-- Insert sample data into Instructors
INSERT INTO Instructors (FirstName, LastName, Email, Phone, DepartmentID) VALUES
('John', 'Doe', 'jdoe@example.com', '123-456-7890', 1),
('Jane', 'Smith', 'jsmith@example.com', '234-567-8901', 2),
('Emily', 'Johnson', 'ejohnson@example.com', '345-678-9012', 3);

-- Insert sample data into Students
INSERT INTO Students (FirstName, LastName, Email, Phone, EnrollmentDate) VALUES
('Alice', 'Brown', 'alice@example.com', '111-222-3333', '2024-01-10'),
('Bob', 'White', 'bob@example.com', '222-333-4444', '2024-01-12'),
('Charlie', 'Green', 'charlie@example.com', '333-444-5555', '2024-01-15');

-- Insert sample data into Courses
INSERT INTO Courses (Name, Credits, DepartmentID, InstructorID) VALUES
('Database Systems', 3, 1, 1),
('Linear Algebra', 4, 2, 2),
('Quantum Mechanics', 3, 3, 3);

-- Insert sample data into Enrollments
INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate, Grade) VALUES
(1, 1, '2024-02-01', 'A'),
(2, 2, '2024-02-03', 'B'),
(3, 3, '2024-02-05', 'A');

-- Insert sample data into Grades
INSERT INTO Grades (StudentID, CourseID, Grade, GradeDate) VALUES
(1, 1, 'A', '2024-03-10'),
(2, 2, 'B', '2024-03-15'),
(3, 3, 'A', '2024-03-20');