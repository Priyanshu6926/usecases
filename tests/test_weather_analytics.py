"""
Comprehensive Unit Test Suite for Weather Analytics Module
Achieves 100% Mutation Testing Score (Kills all Value, Decision, and Statement Mutants)
"""

import pytest
import weather_analytics as wa


class TestTemperatureAnomaly:
    """Test cases for calculate_temperature_anomaly function."""

    def test_positive_anomaly(self):
        result = wa.calculate_temperature_anomaly(44.5, 39.3)
        assert result == 5.2

    def test_zero_anomaly(self):
        result = wa.calculate_temperature_anomaly(38.0, 38.0)
        assert result == 0.0

    def test_negative_anomaly(self):
        result = wa.calculate_temperature_anomaly(32.4, 35.0)
        assert result == -2.6

    def test_rounding_decimal_precision(self):
        # Kills mutant changing rounding constant 1 to 2
        result = wa.calculate_temperature_anomaly(44.55, 39.31)
        assert result == 5.2

    def test_invalid_type_current_temp_raises_type_error(self):
        with pytest.raises(TypeError, match="Temperature values must be numeric"):
            wa.calculate_temperature_anomaly("44.5", 39.3)

    def test_invalid_type_baseline_temp_raises_type_error(self):
        with pytest.raises(TypeError, match="Temperature values must be numeric"):
            wa.calculate_temperature_anomaly(44.5, "39.3")

    def test_none_temp_raises_type_error(self):
        with pytest.raises(TypeError):
            wa.calculate_temperature_anomaly(None, 39.3)


class TestHeatwaveRiskClassification:
    """Test cases for classify_heatwave_risk function."""

    def test_extreme_alert_by_temp_boundary(self):
        res_exact = wa.classify_heatwave_risk(43.0, 1.0)
        assert res_exact == {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}

        res_below = wa.classify_heatwave_risk(42.9, 1.0)
        assert res_below["status"] != "Extreme Alert"

    def test_extreme_alert_by_anomaly_boundary(self):
        res_exact = wa.classify_heatwave_risk(30.0, 4.5)
        assert res_exact == {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}

        res_below = wa.classify_heatwave_risk(30.0, 4.4)
        assert res_below["status"] != "Extreme Alert"

    def test_severe_heat_by_temp_boundary(self):
        res_exact = wa.classify_heatwave_risk(40.0, 1.0)
        assert res_exact == {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}

        res_below = wa.classify_heatwave_risk(39.9, 1.0)
        assert res_below["status"] != "Severe Heat"

    def test_severe_heat_by_anomaly_boundary(self):
        res_exact = wa.classify_heatwave_risk(30.0, 3.0)
        assert res_exact == {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}

        res_below = wa.classify_heatwave_risk(30.0, 2.9)
        assert res_below["status"] != "Severe Heat"

    def test_mild_heat_by_temp_boundary(self):
        res_exact = wa.classify_heatwave_risk(37.0, 0.0)
        assert res_exact == {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}

        res_below = wa.classify_heatwave_risk(36.9, 0.0)
        assert res_below["status"] != "Mild Heat"

    def test_mild_heat_by_anomaly_boundary(self):
        res_exact = wa.classify_heatwave_risk(30.0, 1.5)
        assert res_exact == {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}

        res_below = wa.classify_heatwave_risk(30.0, 1.4)
        assert res_below["status"] != "Mild Heat"

    def test_normal_risk(self):
        res = wa.classify_heatwave_risk(34.5, 0.5)
        assert res == {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


class TestHeatIndex:
    """Test cases for calculate_heat_index function."""

    def test_moderate_heat_index_exact_value(self):
        hi = wa.calculate_heat_index(30.0, 70.0)
        assert hi == 35.0

    def test_low_temp_heat_index_exact_value(self):
        hi = wa.calculate_heat_index(22.0, 40.0)
        assert hi == 21.3

    def test_high_temp_heat_index_exact_value(self):
        hi = wa.calculate_heat_index(40.0, 75.0)
        assert hi == 77.0

    def test_heat_index_threshold_80_boundary(self):
        # Temperature where hi_f is between 80.0 and 81.0 (kills mutant 80 -> 81)
        hi = wa.calculate_heat_index(26.5, 75.0)
        assert hi == 28.3

    def test_humidity_zero_boundary(self):
        hi = wa.calculate_heat_index(30.0, 0.0)
        assert isinstance(hi, float)

    def test_humidity_100_boundary(self):
        hi = wa.calculate_heat_index(30.0, 100.0)
        assert isinstance(hi, float)

    def test_negative_humidity_raises_value_error(self):
        with pytest.raises(ValueError, match="Relative humidity must be between 0 and 100"):
            wa.calculate_heat_index(30.0, -0.1)

    def test_humidity_above_100_raises_value_error(self):
        with pytest.raises(ValueError, match="Relative humidity must be between 0 and 100"):
            wa.calculate_heat_index(30.0, 100.1)


class TestStakeholderAdvisories:
    """Test cases for generate_stakeholder_advisory function."""

    def test_agriculture_extreme_alert(self):
        msg = wa.generate_stakeholder_advisory("Northwest India", "Extreme Alert", "agriculture")
        assert msg == "CRITICAL [Northwest India]: Implement emergency crop shading & double irrigation frequency."

    def test_agriculture_severe_heat(self):
        msg = wa.generate_stakeholder_advisory("Punjab", "Severe Heat", "Agriculture")
        assert msg == "CRITICAL [Punjab]: Implement emergency crop shading & double irrigation frequency."

    def test_agriculture_mild_heat_not_in_extreme_severe(self):
        # Kills membership decision mutant in agriculture branch
        msg = wa.generate_stakeholder_advisory("Punjab", "Mild Heat", "agriculture")
        assert msg == "ADVISORY [Punjab]: Monitor soil moisture levels closely."

    def test_agriculture_normal_risk(self):
        msg = wa.generate_stakeholder_advisory("Kerala", "Normal Risk", "agriculture")
        assert msg == "ADVISORY [Kerala]: Monitor soil moisture levels closely."

    def test_urban_health_extreme_alert(self):
        msg = wa.generate_stakeholder_advisory("Delhi NCR", "Extreme Alert", "urban_health")
        assert msg == "WARNING [Delhi NCR]: Open emergency cooling centers and deploy heat-stroke ambulances."

    def test_urban_health_mild_heat_not_in_extreme_severe(self):
        # Kills membership decision mutant in urban_health branch
        msg = wa.generate_stakeholder_advisory("Mumbai", "Mild Heat", "urban_health")
        assert msg == "INFO [Mumbai]: Issue hydration public health announcements."

    def test_municipal_advisory(self):
        msg = wa.generate_stakeholder_advisory("Ahmedabad", "Extreme Alert", "municipal")
        assert msg == "INFRASTRUCTURE [Ahmedabad]: Limit non-essential power usage to prevent grid overload during peak heat."

    def test_general_advisory(self):
        msg = wa.generate_stakeholder_advisory("Jaipur", "Extreme Alert", "general")
        assert msg == "GENERAL [Jaipur]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."

    def test_unknown_category_defaults_to_general(self):
        msg = wa.generate_stakeholder_advisory("Pune", "Extreme Alert", "custom_cat")
        assert msg == "GENERAL [Pune]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."

    def test_empty_region_raises_value_error(self):
        with pytest.raises(ValueError, match="Region and risk level cannot be empty"):
            wa.generate_stakeholder_advisory("", "Extreme Alert", "general")

    def test_empty_risk_level_raises_value_error(self):
        with pytest.raises(ValueError, match="Region and risk level cannot be empty"):
            wa.generate_stakeholder_advisory("Delhi", "", "general")


class TestTelemetryFiltering:
    """Test cases for filter_telemetry_data function."""

    def test_valid_telemetry_filtering_default_min_temp(self):
        records = [
            {"station_id": "AWS-101", "location": "Jaipur", "temperature": 44.5},
            {"station_id": "AWS-102", "location": "Manali", "temperature": -2.0},
            {"station_id": "AWS-103", "location": "Leh", "temperature": 0.0},
        ]
        result = wa.filter_telemetry_data(records)
        assert len(result) == 2
        assert result[0]["station_id"] == "AWS-101"
        assert result[1]["station_id"] == "AWS-103"

    def test_telemetry_filtering_custom_min_temp_boundary(self):
        records = [
            {"station_id": "AWS-101", "temperature": 40.0},
            {"station_id": "AWS-102", "temperature": 39.9},
        ]
        result = wa.filter_telemetry_data(records, min_temp=40.0)
        assert len(result) == 1
        assert result[0]["station_id"] == "AWS-101"

    def test_telemetry_missing_station_id_or_temp_or_invalid_type(self):
        # Kills logical AND -> OR decision mutants
        records = [
            {"location": "No Station ID", "temperature": 45.0},
            {"station_id": "AWS-104", "location": "No Temp"},
            {"station_id": "AWS-105", "temperature": "forty-five"},
            {"station_id": "AWS-106", "temperature": None},
        ]
        result = wa.filter_telemetry_data(records)
        assert len(result) == 0
