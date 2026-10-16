# Reflection

## 1. Why is static code analysis important?

Static code analysis helps identify code-quality problems, security vulnerabilities, and formatting violations without executing the program. It makes code easier to maintain and reduces potential errors.

## 2. What improvements were made to the program?

I added documentation, improved function and variable naming, removed the mutable default argument, simplified the grading logic, and corrected formatting issues. I also addressed security concerns involving MD5 hashing, random selection, hardcoded credentials, and shell command execution.

## 3. What did the tools report before and after the fixes?

- **Pylint:** The score improved from 5.65/10 to 10.00/10.
- **Bandit:** The original source had four security findings; the final scan of `online_exam.py` reported no issues.
- **Flake8:** Four formatting violations were reported initially, and no violations were reported after the fixes.

## 4. What did I learn from this assignment?

I learned how to use Pylint, Bandit, and Flake8 to assess Python code. I also learned that static analysis can identify maintainability and security problems early, and that saving before-and-after reports helps demonstrate the improvements made.