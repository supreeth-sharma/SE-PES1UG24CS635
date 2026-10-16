# Lab 5: Static Code Analysis — Issues Report

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution | Security — High | 69 | `os.system()` constructed a shell command using phone-list input, creating a command-injection risk. | Removed the unused SMS helper and its subprocess execution path. |
| Unsafe temporary-file creation | Security — Medium | 61 | `tempfile.mktemp()` generated a filename without securely creating the file. | Replaced it with `tempfile.NamedTemporaryFile()` using `delete=False`. |
| Hardcoded password | Security — Low | 5 | A password was stored directly in the source code. | Removed the hardcoded credential. |
| Assertion used for validation | Security / reliability — Low | 18 | `assert` could be disabled under Python optimization. | Replaced it with an explicit `ValueError` check. |
| Mutable default argument | Bug / code quality | 17 | `notes=[]` reused a list across function calls. | Used `notes=None` and initialized a fresh list inside the function. |
| Broad exception handling | Code quality | 45–46 | `except Exception` hid unexpected errors and returned zero. | Validated the patient blood group before accessing compatibility data. |
| Inconsistent naming | Code quality | Multiple | CamelCase function and argument names did not follow Python naming conventions. | Renamed functions and arguments using `snake_case` and updated their callers. |
| Missing docstrings | Code quality | Multiple | The module and functions lacked descriptive documentation. | Added module and function docstrings. |
| Formatting violations | Style | Multiple | Long lines, excessive blank lines, and missing whitespace violated Flake8 rules. | Corrected formatting and verified the final file with Flake8. |
| Incomplete blood compatibility mapping | Functional correctness | Original lines 8–13 | Several valid patient blood groups were missing from the compatibility dictionary. | Added compatibility entries for all eight blood groups. |
| Incorrect universal-donor logic | Functional correctness | Original line 50 | The function classified AB+ as a universal donor for red blood cells. | Updated the function to identify O− as the universal red blood cell donor. |

## Verification

- Pylint final score: 10.00/10.
- Bandit: No issues identified.
- Flake8: No violations reported.
- The demonstration program ran successfully after the changes.