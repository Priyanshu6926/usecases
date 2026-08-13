"""
Standard Python unittest.TestCase Class Implementation
Matches Experiment 02 Manual Step 1 & Step 3.
"""

import unittest
import weather_analytics as wa


class Tests(unittest.TestCase):
    """
    Standard Python unittest class named Tests as specified in Experiment 02.
    """

    def test_positive(self):
        """Test function to check equality of strings (Passing case)."""
        str_val = "I have done unit testing"
        self.assertEqual(str_val, "I have done unit testing")

    def test_heatwave_risk_extreme(self):
        """Test extreme heatwave classification."""
        result = wa.classify_heatwave_risk(44.5, 5.2)
        self.assertEqual(result["status"], "Extreme Alert")

    def test_temperature_anomaly_calculation(self):
        """Test numeric anomaly calculation assertion."""
        anomaly = wa.calculate_temperature_anomaly(43.8, 39.0)
        self.assertEqual(anomaly, 4.8)


if __name__ == '__main__':
    unittest.main()
