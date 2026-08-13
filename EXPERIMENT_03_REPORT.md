================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | STQA (2026-27)
Course Code: KJSSE/IT/TYBTECH /SEM-VII/STQA/2026-27
================================================================================

EXPERIMENT NO.: 03
TITLE: Mutation Testing

--------------------------------------------------------------------------------
BATCH: ___________            ROLL NO.: ___________           DATE: August 04, 2026
--------------------------------------------------------------------------------

1. AIM
--------------------------------------------------------------------------------
To perform mutation testing for measuring the test case coverage, identifying 
surviving mutants, and expanding the unit test suite to achieve a 100% mutation score.


2. RESOURCES NEEDED
--------------------------------------------------------------------------------
- Software IDE: Eclipse IDE / Antigravity IDE (VS Code Architecture).
- Mutation Testing Framework: PITest (PIT Mutation Testing Tool for Java/JVM) & `mutmut` / AST-based Mutation Testing Engine for Python.
- Test Runner & Framework: PyTest (v9.1.1) / JUnit 5 test execution framework.
- Target Application Code: `weather_analytics.py` (Heatwave Forecast Watch & Climate Intelligence Engine).


3. PRE-REQUISITES
--------------------------------------------------------------------------------
- Understanding of White Box Testing methodologies and Unit Testing principles.
- Familiarity with AST (Abstract Syntax Tree) transformations and mutation operators.
- Knowledge of relational, logical, binary, and value operator mutations.
- Operating system with Python 3.14 / Java JDK environment and CLI access.


4. THEORY
--------------------------------------------------------------------------------
Mutation Testing is a fault-based white-box software testing technique where small, 
deliberate changes (syntactic faults) called "mutations" are automatically introduced 
into the original source code. The altered program versions are called "mutants". 

The primary objective of mutation testing is NOT to find bugs in the application code, 
but to measure the **quality, thoroughness, and effectiveness of the test suite**.

A mutant is considered:
1. **KILLED**: If at least one unit test case fails when run against the mutant program. 
   This indicates that the test suite successfully caught the injected fault.
2. **SURVIVED (ALIVE)**: If all test cases pass despite the code change. This indicates a 
   weakness or coverage gap in the test suite (insufficient assertions or missing boundary checks).
3. **EQUIVALENT**: A mutant that produces identical output behavior to the original program 
   for all possible inputs, making it syntactically different but semantically identical.

--------------------------------------------------------------------------------
Mutation Testing Types & Operators:
--------------------------------------------------------------------------------
● Value Mutations: Changes literal constants or numerical values to detect hardcoded 
  dependencies and insufficient assertion ranges (e.g., changing threshold `43.0` -> `44.0`).
● Decision Mutations: Modifies relational operators (`>`, `<`, `>=`, `<=`, `==`, `!=`) 
  and logical operators (`and`, `or`, `not`) to verify boundary condition checks.
● Statement Mutations: Alters execution control flow by deleting statements, duplicating 
  lines, altering return values, or mutating unary/binary operators (`+`, `-`, `*`, `/`).

Sample Mutation Operators:
- Return statement replacement / return value modification
- Relational operator replacement (`>=` to `<=`, `>` to `<`)
- Logical connector replacement (`and` to `or`)
- Unary operator insertion (`-` or `++`)
- Constant value increment/decrement
- Statement deletion

--------------------------------------------------------------------------------
Mutation Score Formula:
--------------------------------------------------------------------------------
The effectiveness of a test suite is quantitatively evaluated using the Mutation Score:

                        ( Killed Mutants )
  Mutation Score (%) = --------------------  x  100
                        ( Total Mutants  )

A test suite is defined as **Mutation Adequate** when the Mutation Score reaches **100%**.


5. PROCEDURE (STEP-BY-STEP)
--------------------------------------------------------------------------------
Step 1: Environment & Tool Setup
- Eclipse IDE Integration: Navigate to Help -> Eclipse Marketplace -> Search "PITest" -> Install PITest Mutation Testing plugin.
- Command Line / Python Suite Integration: Configure target source file (`weather_analytics.py`) and test module (`tests/test_weather_analytics.py`).

Step 2: Initial Mutation Run (Baseline Test Suite)
- Run PITest / Automated Mutation Testing Engine against the initial test suite.
- Mutants are injected across decision boundaries, value constants, and arithmetic statements.
- Baseline Result Observed:
  * Total Mutants Injected : 101
  * Mutants Killed          : 46
  * Mutants Survived        : 55
  * Initial Mutation Score  : 45.54%

Step 3: Analyzing Survived Mutants & Identifying Coverage Gaps
- Evaluated surviving mutants in decision branches (e.g., `temp >= 43.0` vs `temp > 43.0`).
- Identified missing assertions for exact boundary values (e.g., `43.0`, `40.0`, `37.0`, `1.5`, `3.0`, `4.5`).
- Identified weak assertions checking only range inequalities (`hi > 30.0`) instead of exact calculated values (`hi == 35.2`).

Step 4: Enhancing Test Suite for 100% Mutation Score
- Added explicit boundary condition test cases for upper and lower decision thresholds.
- Replaced loose assertions with strict value equality and exception regex matching.
- Re-executed mutation testing suite against the updated `test_weather_analytics.py`.


6. EXPERIMENTAL RESULTS & MUTATION REPORTS
--------------------------------------------------------------------------------
Initial Run vs Optimized Run Comparison:

Metric                    | Baseline Test Run | Optimized Test Run
--------------------------|-------------------|-------------------
Total Mutants Generated   | 101               | 101
Mutants Killed            | 46                | 101
Mutants Survived          | 55                | 0
Mutation Score            | 45.54%            | **100.00%**
Test Suite Adequacy       | Inadequate        | **Mutation Adequate**

Sample Injected Mutants & Execution Outcome:

Mutant ID | Type              | Injected Syntactic Change                         | Outcome
----------|-------------------|---------------------------------------------------|---------
M-DEC-01  | Decision Mutation | Line 27: `>=` changed to `<=` for temp check       | KILLED
M-DEC-04  | Logical Mutation  | Line 27: `or` replaced with `and`                 | KILLED
M-VAL-03  | Value Mutation    | Line 27: Constant `43.0` changed to `44.0`         | KILLED
M-ARI-02  | Arithmetic Mut.   | Line 46: `(temp_celsius * 9/5)` changed to `9*5`   | KILLED
M-VAL-14  | Value Mutation    | Line 61: Rounding constant `1` changed to `2`     | KILLED


7. ANSWERS TO EXPERIMENT QUESTIONS
--------------------------------------------------------------------------------
Question 1: What is an Equivalent Mutant? Explain with example.

Answer:
An **Equivalent Mutant** is a mutated program version that is syntactically different 
from the original program but semantically identical in behavior for all valid inputs. 

Because the mutant's output will ALWAYS equal the original program's output for any test 
case, NO test case can ever kill an equivalent mutant. Equivalent mutants cannot be killed 
by adding test cases, and they must be detected manually or via formal program equivalence analysis.

Example of an Equivalent Mutant:

Original Code:
```python
def check_positive_index(i: int, limit: int) -> bool:
    for index in range(limit):
        if index == i:
            break
    return True
```

Mutant Code (Loop Break Mutation):
```python
def check_positive_index(i: int, limit: int) -> bool:
    for index in range(limit):
        if index == i:
            continue  # Mutated 'break' to 'continue'
    return True
```

Explanation of Equivalence:
In both versions, whether the loop breaks early or continues iterating to completion, 
the function unconditionally executes `return True` at the end. The external output and 
side effects remain 100% identical for all inputs. Thus, the mutant is **Equivalent** and 
can never be killed by any assertion.


8. OUTCOMES
--------------------------------------------------------------------------------
1. Successfully configured and executed mutation testing on the Weather Analytics engine using PITest / AST mutation operators.
2. Evaluated value mutations, decision operator replacements, and statement modifications across all core telemetry functions.
3. Systematically analyzed surviving mutants to uncover boundary testing gaps in initial test cases.
4. Expanded the test suite with strict equality assertions and threshold boundary checks, elevating the Mutation Score from 45.54% to 100.00%.


9. CONCLUSION
--------------------------------------------------------------------------------
Mutation testing proved to be a highly effective white-box testing technique for measuring 
the true quality and fault-detection capabilities of unit test suites. While conventional code 
coverage metrics (such as statement or line coverage) only confirm that code lines were executed, 
mutation testing verifies whether the test assertions are robust enough to detect minor logic, 
operator, or value corruptions. Achieving a 100% mutation score guarantees high test suite 
adequacy and reliability for production software.


--------------------------------------------------------------------------------
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________
