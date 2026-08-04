"""
Unit Test Suite for Weather Analytics Module
Uses PyTest framework & unittest assertion patterns.
"""

import pytest
import weather_analytics as wa


class TestTemperatureAnomaly:
    """Test cases for calculate_temperature_anomaly function."""

    def test_positive_anomaly(self):
        """Test positive temperature anomaly calculation."""
        result = wa.calculate_temperature_anomaly(44.5, 39.3)
        assert result == 5.2

    def test_zero_anomaly(self):
        """Test zero temperature anomaly (current equals baseline)."""
        result = wa.calculate_temperature_anomaly(38.0, 38.0)
        assert result == 0.0

    def test_negative_anomaly(self):
        """Test negative temperature anomaly (below average)."""
        result = wa.calculate_temperature_anomaly(32.4, 35.0)
        assert result == -2.6

    def test_invalid_type_raises_exception(self):
        """Test that passing non-numeric types raises TypeError."""
        with pytest.raises(TypeError):
            wa.calculate_temperature_anomaly("44.5", 39.3)


class TestHeatwaveRiskClassification:
    """Test cases for classify_heatwave_risk function."""

    @pytest.mark.parametrize("temp, anomaly, expected_status, expected_level", [
        (44.5, 5.2, "Extreme Alert", 4),
        (41.5, 3.5, "Severe Heat", 3),
        (38.8, 1.8, "Mild Heat", 2),
        (34.5, 0.5, "Normal Risk", 1),
    ])
    def test_risk_classification_levels(self, temp, anomaly, expected_status, expected_level):
        """Parametrized test verifying all risk classification tiers."""
        result = wa.classify_heatwave_risk(temp, anomaly)
        assert result["status"] == expected_status
        assert result["level"] == expected_level

    def test_extreme_alert_boundary(self):
        """Test boundary condition for Extreme Alert."""
        result = wa.classify_heatwave_risk(43.0, 1.0)
        assert result["status"] == "Extreme Alert"
        assert result["badge_class"] == "badge-extreme"


class TestHeatIndex:
    """Test cases for calculate_heat_index function."""

    def test_moderate_heat_index(self):
        """Test standard temperature and humidity calculation."""
        hi = wa.calculate_heat_index(30.0, 70.0)
        assert hi > 30.0
        assert isinstance(hi, float)

    def test_invalid_humidity_bounds(self):
        """Test that humidity outside 0-100 raises ValueError."""
        with pytest.raises(ValueError):
            wa.calculate_heat_index(35.0, 110.0)

        with pytest.raises(ValueError):
            wa.calculate_heat_index(35.0, -5.0)


class TestStakeholderAdvisories:
    """Test cases for generate_stakeholder_advisory function."""

    def test_agriculture_extreme_advisory(self):
        msg = wa.generate_stakeholder_advisory("Northwest India", "Extreme Alert", "agriculture")
        assert "CRITICAL [Northwest India]" in msg
        assert "irrigation" in msg

    def test_urban_health_advisory(self):
        msg = wa.generate_stakeholder_advisory("Delhi NCR", "Severe Heat", "urban_health")
        assert "WARNING [Delhi NCR]" in msg
        assert "cooling centers" in msg

    def test_empty_input_raises_value_error(self):
        with pytest.raises(ValueError):
            wa.generate_stakeholder_advisory("", "Extreme Alert", "general")


class TestTelemetryFiltering:
    """Test cases for filter_telemetry_data function."""

    @pytest.fixture
    def sample_telemetry(self):
        """Fixture supplying mock weather station records."""
        return [
            {"station_id": "AWS-101", "location": "Jaipur", "temperature": 44.5},
            {"station_id": "AWS-102", "location": "Manali", "temperature": 22.0},
            {"station_id": "AWS-103", "location": "FaultySensor", "temperature": "INVALID"},
            {"location": "NoID", "temperature": 39.0},
        ]

    def test_filter_valid_records(self, sample_telemetry):
        filtered = wa.filter_telemetry_data(sample_telemetry, min_temp=30.0)
        assert len(filtered) == 1
        assert filtered[0]["station_id"] == "AWS-101"

    def test_filter_all_valid(self, sample_telemetry):
        filtered = wa.filter_telemetry_data(sample_telemetry, min_temp=0.0)
        assert len(filtered) == 2
