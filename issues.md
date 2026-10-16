# Static Code Analysis Findings

## 1. Pylint Findings

| Original finding | Resolution |
|---|---|
| Missing module docstring (C0114) | Added a module docstring |
| Missing function docstrings (C0116) | Added docstrings to functions |
| Invalid naming style (C0103) | Renamed functions and arguments using snake_case |
| Mutable default argument (W0102) | Replaced `{}` with `None` and initialized the dictionary inside the function |
| Unnecessary range and len (C0200) | Used `enumerate()` |
| Unnecessary elif after return (R1705) | Simplified the conditional statements |

**Before:** 5.65/10

**After:** 10.00/10

## 2. Bandit Findings

| Finding | Resolution |
|---|---|
| B105: Hardcoded password | Removed the unused hardcoded password |
| B324: Weak MD5 hash | Replaced hashing with normalized string comparison |
| B311: Standard pseudo-random generator | Used `secrets.choice()` |
| B605: Shell command execution | Removed the unused unsafe `os.system()` helper |

**Before:** 4 findings in the project source.

**After:** No issues identified when scanning `online_exam.py`.

## 3. Flake8 Findings

| Finding | Resolution |
|---|---|
| E302: Incorrect blank lines | Corrected function spacing |
| E225: Missing whitespace around operator | Added appropriate whitespace |
| E261: Inline comment spacing | Corrected comment spacing |
| E501: Line too long | Split the long statement across multiple lines |

**Before:** 4 reported violations.

**After:** No reported violations.

## 4. Verification

The program was executed after the changes. The student scores, class average, and topper matched the expected results. The final reports are stored in `reports/after/`, and the original reports are preserved in `reports/before/`.