-- 1. List the following details of each employee: employee number, last name, first name,
--gender, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees AS e
LEFT JOIN salaries AS s
ON (e.emp_no = s.emp_no)
ORDER BY e.emp_no;

-- 2. List employees who were hired in 1986.
SELECT employees.emp_no, employees.last_name, employees.first_name
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number,
--last name, first name, and start and end employment dates.
SELECT mng.dept_no, dept.dept_name, mng.emp_no, e.last_name, e.first_name, mng.from_date, mng.to_date
FROM dept_manager AS mng
LEFT JOIN employees AS e
	ON (mng.emp_no = e.emp_no)
LEFT JOIN departments AS dept
	ON (mng.dept_no = dept.dept_no);

--4. List the department of each employee with the following information
--employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, dp.dept_name
FROM employees AS e
INNER JOIN dept_emp AS d ON
e.emp_no = d.emp_no
INNER JOIN departments AS dp ON
dp.dept_no = d.dept_no;

--5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT e.first_name, e.last_name
FROM employees AS e
where first_name like 'Hercules'
and last_name like 'B%';

--6. List all employees in the Sales department
--including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, dp.dept_name
FROM employees AS e
INNER JOIN dept_emp AS d ON
e.emp_no = d.emp_no
INNER JOIN departments AS dp ON
dp.dept_no = d.dept_no
where dept_name like 'Sales';

--7. List all employees in the Sales and Development departments
--including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, dp.dept_name
FROM employees AS e
INNER JOIN dept_emp AS d ON
e.emp_no = d.emp_no
INNER JOIN departments AS dp ON
dp.dept_no = d.dept_no
where dept_name like 'Sales'
or dept_name like 'Development';

--8.In descending order, list the frequency count of employee last names,
--i.e., how many employees share each last name.
SELECT last_name, COUNT(*) AS frequency
FROM employees
GROUP BY last_name
ORDER BY frequency DESC;
