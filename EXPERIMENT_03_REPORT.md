================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | STQA (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/STQA/2026-27
================================================================================

Batch: A2                Roll No.: 16010423075                Experiment No.: 03
Title: Mutation Testing

________________________________________________________________________________
Aim: To perform mutation testing for measuring the test case coverage.
________________________________________________________________________________
Resources needed: Eclipse IDE, PIT Mutation Testing / Antigravity IDE (Python AST Mutation Testing Engine & PyTest).
________________________________________________________________________________

Theory:

Mutation Testing is a type of software testing where we mutate (change) certain statements in
the source code and check if the test cases are able to find the errors. It is a type of White
Box Testing which is mainly used for Unit Testing.

```
+------------------+         Fault          +------------------+
| Original Program | ---------------------> |  Mutant Program  |
+------------------+      Introduction      +------------------+
        |                                             |
        v                                             v
+--------------------------------------------------------------+
|             Test Cases Applied to Both Programs              |
+--------------------------------------------------------------+
                               |
                               v
                     Compare Output Results
                               |
            +------------------+------------------+
            |                                     |
     Outputs Differ                       Outputs Match
            |                                     |
            v                                     v
   [ MUTANT IS KILLED ]                 [ MUTANT SURVIVES ]
```

Mutation Testing Types:
● Value Mutations: An attempt to change the values to detect errors in the programs. We
  usually change one value to a much larger value or one value to a much smaller value.
  The most common strategy is to change the constants (e.g., threshold `43.0` -> `44.0`).
● Decision Mutations: The decisions/conditions are changed to check for the design
  errors. Typically, one changes the arithmetic operators to locate the defects and also we
  can consider mutating all relational operators (`>`, `<`, `>=`, `<=`, `==`, `!=`) and
  logical operators (`and`, `or`, `not`).
● Statement Mutations: Changes done to the statements by deleting or duplicating the
  line which might arise when a developer is copy pasting the code from somewhere else.

How to Create Mutant Programs?
A mutation is nothing but a single syntactic change that is made to the program statement. Each
mutant program should differ from the original program by one mutation.

Some of sample mutation operators:
● GOTO label replacement
● Return statement replacement
● Statement deletion
● Unary operator insertion (Like - and ++)
● Logical connector replacement
● Comparable array name replacement
● Removing of else part in the if-else statement
● Adding or replacement of operators
● Statement replacement by changing the data
● Data Modification for the variables
● Modification of data types in the program

Example 1:
+------------------------------------+------------------------------------+
| Original Program                   | Mutant Program                     |
+------------------------------------+------------------------------------+
| If (x > y):                        | If (x < y):                        |
|     Print "Hello"                  |     Print "Hello"                  |
| Else:                              | Else:                              |
|     Print "Hi"                     |     Print "Hi"                     |
+------------------------------------+------------------------------------+

Example 2:
+------------------------------------+------------------------------------+
| Original Program                   | Mutant Program                     |
+------------------------------------+------------------------------------+
| If (x == y):                       | If (x >= y):                       |
|     return x                       |     return ++x                     |
+------------------------------------+------------------------------------+

How to execute mutation testing?
Following are the steps to execute mutation testing:
Step 1: Faults are introduced into the source code of the program by creating many versions
called mutants. Each mutant should contain a single fault, and the goal is to cause the mutant
version to fail which demonstrates the effectiveness of the test cases.
Step 2: Test cases are applied to the original program and also to the mutant program. A test
case should be adequate, and it is tweaked to detect faults in a program.
Step 3: Compare the results of original and mutant program.
Step 4: If the original program and mutant programs generate the different output, then that the
mutant is killed by the test case. Hence the test case is good enough to detect the change
between the original and the mutant program.
Step 5: If the original program and mutant program generate same output, Mutant is kept alive.
In such cases, more effective test cases need to be created that kill all mutants.

Automation of Mutation Testing:
Mutation testing is extremely time consuming and complicated to execute manually. To speed
up the process, it is advisable to go for automation tools. Automation tools reduce cost of
testing as well.

List of tools available:
● Ninja Turtles: .NET mutation testing tool
● Mutagenesis: PHP mutation testing framework
● Jester: Mutation testing tool for Java
● PITest: Mutation testing tool for Java and the JVM
● Mutmut / AST Mutation Engine: Mutation testing framework for Python

Mutation Score:
The mutation score is defined as the percentage of killed mutants with the total number of mutants.

● Mutation Score = (Killed Mutants / Total number of Mutants) * 100

Test cases are mutation adequate if the score is 100%. Experimental results have shown that
mutation testing is an effective approach for measuring the adequacy of test cases.

________________________________________________________________________________
Procedure:
Step 1: To download PITest- Mutation Testing [Eclipse -> Help -> Eclipse Marketplace -> type "PITest" -> select PITest -> install] or configure AST mutation runner in IDE.
Step 2: Write the test cases and run [right click on test case file -> Run As -> PITest / python3 mutation_runner.py].
Step 3: Observe the result and write additional test cases to achieve 100% score.

================================================================================
PROJECT-SPECIFIC IMPLEMENTATION & MUTATION TESTING EXECUTION
================================================================================

As our project is a Climate Intelligence & Heatwave Early Warning System (`weather_analytics`),
we used modern integrated testing tools for mutation testing:

● PyTest (v9.1.1): Used to execute the unit test suites.
● Python AST Mutation Engine (`mutation_runner.py`): Used to introduce artificial syntactic code changes across Decision, Value, and Arithmetic operators.

--------------------------------------------------------------------------------
1. Selected the Target Functions in `weather_analytics.py`
--------------------------------------------------------------------------------
Instead of testing the entire web presentation layer directly, we selected core analytical and mathematical telemetry logic functions that could be tested independently with precision:

1. `calculate_temperature_anomaly(current_temp, baseline_temp)`:
   Calculates temperature deviations from long-term baseline averages.
2. `classify_heatwave_risk(temp, anomaly)`:
   Classifies severity risk levels (Extreme Alert, Severe Heat, Mild Heat, Normal Risk) based on multi-variable decision thresholds.
3. `calculate_heat_index(temp_celsius, relative_humidity)`:
   Implements the NOAA Rothfusz regression equation for atmospheric heat stress.
4. `generate_stakeholder_advisory(region, risk_level, category)`:
   Generates targeted sector-specific advisories for agriculture, urban health, and municipal infrastructure.
5. `filter_telemetry_data(sensor_records, min_temp)`:
   Filters incoming weather station feeds based on structural validity and temperature thresholds.

--------------------------------------------------------------------------------
2. Created a Separate Utility Module (`weather_analytics.py`)
--------------------------------------------------------------------------------
We isolated the analytical computation logic into a standalone module:
`weather_analytics.py`

The purpose was to decouple mathematical telemetry calculations from UI rendering. This makes the logic deterministic, fast, and ideal for automated mutation testing.

--------------------------------------------------------------------------------
3. Created Unit Tests (`tests/test_weather_analytics.py`)
--------------------------------------------------------------------------------
We created a comprehensive unit test suite:
`tests/test_weather_analytics.py`

The test file imports the target functions directly:
```python
import weather_analytics as wa
import pytest
```

--------------------------------------------------------------------------------
4. Tested Different Conditions and Decision Boundaries
--------------------------------------------------------------------------------
We created tests for critical behaviors and edge conditions across all functions:

Test Name                                        | What it checks
-------------------------------------------------|------------------------------------------------------------
`test_positive_anomaly`                          | Validates positive temperature deviation calculation
`test_zero_anomaly`                              | Checks zero anomaly when current equals baseline
`test_negative_anomaly`                          | Checks negative anomaly calculation
`test_rounding_decimal_precision`                | Verifies single-decimal rounding precision
`test_invalid_type_raises_type_error`            | Tests type validation for non-numeric inputs
`test_extreme_alert_by_temp_boundary`            | Tests exact threshold `temp >= 43.0` and `temp < 43.0`
`test_extreme_alert_by_anomaly_boundary`         | Tests exact threshold `anomaly >= 4.5` and `anomaly < 4.5`
`test_severe_heat_by_temp_boundary`              | Tests exact threshold `temp >= 40.0` and `temp < 40.0`
`test_severe_heat_by_anomaly_boundary`           | Tests exact threshold `anomaly >= 3.0` and `anomaly < 3.0`
`test_mild_heat_by_temp_boundary`                | Tests exact threshold `temp >= 37.0` and `temp < 37.0`
`test_mild_heat_by_anomaly_boundary`             | Tests exact threshold `anomaly >= 1.5` and `anomaly < 1.5`
`test_normal_risk`                               | Validates fallback normal classification
`test_moderate_heat_index_exact_value`           | Checks exact Rothfusz heat index calculation at 30°C/70%RH
`test_low_temp_heat_index_exact_value`            | Checks exact heat index calculation for lower temperatures
`test_high_temp_heat_index_exact_value`           | Checks exact heat index calculation for extreme temperatures
`test_heat_index_threshold_80_boundary`          | Validates boundary condition when Heat Index Fahrenheit >= 80
`test_humidity_zero_boundary`                    | Tests lower humidity boundary (0%)
`test_humidity_100_boundary`                     | Tests upper humidity boundary (100%)
`test_invalid_humidity_raises_value_error`       | Tests range validation for humidity < 0 or > 100
`test_agriculture_extreme_alert`                 | Checks agricultural advisory generation for extreme heat
`test_urban_health_extreme_alert`                | Checks urban healthcare cooling alerts
`test_municipal_advisory`                        | Checks municipal power grid warning generation
`test_unknown_category_defaults_to_general`      | Validates default general population advisory fallback
`test_valid_telemetry_filtering`                 | Validates multi-station sensor record filtering

--------------------------------------------------------------------------------
5. Ran Baseline Unit Tests
--------------------------------------------------------------------------------
We executed the unit tests using PyTest:
```bash
pytest
```

Output:
```text
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/priyanshu/Desktop/Projects/usecases
configfile: pytest.ini
testpaths: tests
collected 39 items

tests/test_standard_unittest.py ...                                      [  7%]
tests/test_weather_analytics.py ....................................     [100%]

============================== 39 passed in 0.02s ==============================
```

All 39 unit tests passed successfully on the original unmutated codebase.

--------------------------------------------------------------------------------
6. Configured the Mutation Testing Engine (`mutation_runner.py`)
--------------------------------------------------------------------------------
We implemented an automated AST (Abstract Syntax Tree) mutation testing engine:
`mutation_runner.py`

The engine applies three core transformer classes:
1. `DecisionMutator`: Replaces relational (`>=` to `<=`, `>` to `<`, `==` to `!=`) and logical operators (`and` to `or`, `in` to `not in`).
2. `ValueMutator`: Modifies numeric constants (`value = value + 1.0`).
3. `ArithmeticMutator`: Inverts binary arithmetic operators (`+` to `-`, `*` to `/`).

--------------------------------------------------------------------------------
7. Performed the First Mutation Test (Baseline Suite)
--------------------------------------------------------------------------------
We ran the initial mutation test:
```bash
python3 mutation_runner.py
```

The engine generated 101 mutants across the codebase.

Sample Injected Mutants:
- Line 27: `temp >= 43.0` mutated to `temp <= 43.0`
- Line 27: `43.0` mutated to `44.0`
- Line 46: `(temp_celsius * 9/5)` mutated to `(temp_celsius * 9*5)`
- Line 52: `hi_f >= 80` mutated to `hi_f >= 81`

--------------------------------------------------------------------------------
8. First Mutation Testing Result
--------------------------------------------------------------------------------
The initial baseline run result was:
- Total Mutants: 101
- Killed: 46
- Survived: 55
- Mutation Score: 45.54%

$$\text{Initial Mutation Score} = \frac{46}{101} \times 100 = 45.54\%$$

This revealed that although standard line coverage was high, the assertions were insufficient to detect critical boundary shifts.

--------------------------------------------------------------------------------
9. Analyzed the Surviving Mutants
--------------------------------------------------------------------------------
The mutation runner identified 55 surviving mutants:
1. **Loose Range Assertions**: In `calculate_heat_index`, tests only asserted `assert hi > 25.0` instead of the exact calculated value `assert hi == 35.0`. Thus, arithmetic mutations altering polynomial coefficients survived.
2. **Missing Exact Boundary Checks**: In `classify_heatwave_risk`, testing with `temp = 45.0` passed for both `temp >= 43.0` and the mutated `temp >= 44.0`. The exact boundary `temp = 43.0` was unverified.
3. **Threshold Transition Gaps**: In `hi_f >= 80`, temperatures between 80.0°F and 81.0°F were not tested, allowing value mutations on `80` to survive.

--------------------------------------------------------------------------------
10. Improved the Test Cases
--------------------------------------------------------------------------------
We enhanced `tests/test_weather_analytics.py` with rigorous boundary checks and strict equality assertions:

1. **Exact Value Assertions**:
   ```python
   # Replaced loose range assertion with exact calculated float:
   hi = wa.calculate_heat_index(30.0, 70.0)
   assert hi == 35.0  # Kills all arithmetic polynomial coefficient mutants
   ```

2. **Upper & Lower Boundary Pairs**:
   ```python
   # Exact boundary pair to kill threshold constant mutations (43.0 -> 44.0):
   res_exact = wa.classify_heatwave_risk(43.0, 1.0)
   assert res_exact["status"] == "Extreme Alert"

   res_below = wa.classify_heatwave_risk(42.9, 1.0)
   assert res_below["status"] != "Extreme Alert"
   ```

3. **Sub-Degree Humidity & Heat Index Transitions**:
   ```python
   # Boundary temperature where hi_f is exactly in the (80.0, 81.0) window:
   hi = wa.calculate_heat_index(26.5, 75.0)
   assert hi == 28.3  # Kills mutant 80 -> 81
   ```

--------------------------------------------------------------------------------
11. Ran Unit Tests Again
--------------------------------------------------------------------------------
We re-ran PyTest to verify all enhanced test cases pass against clean code:
```bash
pytest
```
Result: **39 passed in 0.02s**

--------------------------------------------------------------------------------
12. Ran Mutation Testing Again
--------------------------------------------------------------------------------
We re-executed the automated mutation testing engine:
```bash
python3 mutation_runner.py
```

Final Result:
- Total Mutants Generated : 101
- Mutants Killed          : 101
- Mutants Survived        : 0
- **Final Mutation Score   : 100.00%**

$$\text{Final Mutation Score} = \frac{101}{101} \times 100 = 100.00\%$$

--------------------------------------------------------------------------------
13. Mutation Run Summary & Category Table
--------------------------------------------------------------------------------

Mutant Category       | Injected Operators                                 | Generated | Killed | Survived | Score
----------------------|----------------------------------------------------|-----------|--------|----------|-------
Decision Mutations    | `>=`, `<=`, `>`, `<`, `==`, `!=`, `in`, `not in`   | 24        | 24     | 0        | 100%
Logical Mutations     | `and` <-> `or`                                     | 12        | 12     | 0        | 100%
Value Mutations       | Numerical Constants (`43.0`, `40.0`, `1.5`, etc.) | 47        | 47     | 0        | 100%
Arithmetic Mutations  | `+`, `-`, `*`, `/`                                 | 18        | 18     | 0        | 100%
----------------------|----------------------------------------------------|-----------|--------|----------|-------
**Total**             |                                                    | **101**   | **101**| **0**    | **100.00%**

================================================================================
QUESTIONS & ANSWERS
================================================================================

1. What is an Equivalent Mutant? Explain with example.

Answer:
An **Equivalent Mutant** is a mutated version of a program that, even though its source 
code is syntactically changed, behaves exactly the same as the original program for every 
possible valid input.

In mutation testing, mutants are deliberately created by making syntactic changes to the 
source code. Normally, an adequate test suite detects these modifications and kills the mutant. 
However, if a mutation produces no observable change in program output or state, no test input 
can distinguish the mutant from the original program. Such a mutant is called an equivalent mutant.

Definition:
An equivalent mutant is a mutant whose behavior is functionally identical to the original 
program across the entire domain of inputs, meaning that no test case can ever kill it.

---

### Non-Equivalent Mutant Example:
Consider original code:
```python
def check_heatwave(temp: float) -> str:
    if temp > 40:
        return "Heatwave"
    return "Normal"
```

Suppose a mutation changes the relational operator:
```python
def check_heatwave(temp: float) -> str:
    if temp >= 40:
        return "Heatwave"
    return "Normal"
```

This is **NOT** an equivalent mutant because when `temp = 40`:
- Original returns `"Normal"`
- Mutant returns `"Heatwave"`
Therefore, a test case with input `40` will catch the difference and kill the mutant.

---

### Actual Equivalent Mutant Example:
Consider original code:
```python
def generate_status(region: str) -> str:
    status = "Active"
    return status
```

Suppose a mutation changes the return expression:
```python
def generate_status(region: str) -> str:
    status = "Active"
    return status + ""
```

Both `"Active"` and `"Active" + ""` evaluate to the exact same string value `"Active"` for all executions. 
No test assertion can ever detect a difference. Hence, this is an **Equivalent Mutant**.

________________________________________________________________________________
Outcomes:
CO2: Demonstrate designing and execution of test cases using testing techniques.
________________________________________________________________________________
Conclusion: (Conclusion to be based on outcomes)

The experiment successfully demonstrated mutation testing on the Weather Analytics & Climate 
Intelligence module (`weather_analytics.py`) using PyTest and an AST Mutation Testing Engine. 
The initial test suite scored 45.54% with 55 surviving mutants due to loose assertions and missing 
boundary tests. By analyzing mutant survival patterns, we enhanced the test suite with exact value 
comparisons and strict boundary conditions. In the final run, all 101 generated mutants across 
Decision, Logical, Value, and Arithmetic operators were killed, achieving a **100.00% Mutation Score**, 
verifying that the test suite is mutation adequate and robust against code defects.
________________________________________________________________________________
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________
________________________________________________________________________________

Reference Websites:
1. Mutation Testing Tutorial:
   https://www.tutorialspoint.com/software_testing_dictionary/mutation_testing.htm
   https://www.guru99.com/mutation-testing.html
2. Mutation Testing:
   https://www.youtube.com/watch?v=1DvJeMmKrUE
3. Mutation Testing With PIT:
   https://www.youtube.com/watch?v=3Al1tHE8z64
