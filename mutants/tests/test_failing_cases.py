"""
Demonstration of Test Failure for PyTest Unit Testing (Lab Step 4)
This test module contains intentional assertion failures to demonstrate PyTest error reporting.
"""

import pytest
import weather_analytics as wa


def test_positive_intentional_failure():
    """Demonstrates assertion failure when expected output differs from actual."""
    str1 = "I have done unit testing"
    str2 = "I have not done unit testing"
    # Intentional failure to reproduce page 3 step 4 scenario from lab manual
    assert str1 == str2, f"AssertionFailed: '{str1}' != '{str2}'"


def test_incorrect_anomaly_expectation():
    """Demonstrates mathematical calculation expectation failure."""
    anomaly = wa.calculate_temperature_anomaly(44.5, 39.3)  # actual: 5.2
    expected_anomaly = 10.0
    assert anomaly == expected_anomaly, f"Expected anomaly {expected_anomaly}, got {anomaly}"
