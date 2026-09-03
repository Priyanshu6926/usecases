"""
Weather Analytics Engine & Unit Testing Target Module
Provides core mathematical, telemetry, and advisory calculation functions
for the Heatwave Forecast Watch & Climate Intelligence Portal.
"""

from typing import Dict, List, Union, Any, Optional

def calculate_temperature_anomaly(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or isinstance(current_temp, bool) or \
       not isinstance(baseline_temp, (int, float)) or isinstance(baseline_temp, bool):
        raise TypeError("Temperature values must be numeric (int or float) and not boolean.")
    return round(float(current_temp) - float(baseline_temp), 1)


def classify_heatwave_risk(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def calculate_heat_index(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9/5) + 32
    RH = relative_humidity

    # Simple heat index formula for ambient temps
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def generate_stakeholder_advisory(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["Extreme Alert", "Severe Heat"]:
            return f"CRITICAL [{region}]: Implement emergency crop shading & double irrigation frequency."
        return f"ADVISORY [{region}]: Monitor soil moisture levels closely."
    elif category == "urban_health":
        if risk_level in ["Extreme Alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def filter_telemetry_data(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records
