"""
Weather Analytics Engine & Unit Testing Target Module
Provides core mathematical, telemetry, and advisory calculation functions
for the Heatwave Forecast Watch & Climate Intelligence Portal.
"""

from typing import Dict, List, Union, Any, Optional


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_calculate_temperature_anomaly__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_calculate_temperature_anomaly__mutmut)
def calculate_temperature_anomaly(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_orig(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_1(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) and not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_2(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_3(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_4(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError(None)
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_5(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("XXTemperature values must be numeric (int or float).XX")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_6(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_7(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("TEMPERATURE VALUES MUST BE NUMERIC (INT OR FLOAT).")
    return round(float(current_temp) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_8(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(None, 1)

def x_calculate_temperature_anomaly__mutmut_9(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), None)

def x_calculate_temperature_anomaly__mutmut_10(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(1)

def x_calculate_temperature_anomaly__mutmut_11(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), )

def x_calculate_temperature_anomaly__mutmut_12(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) + float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_13(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(None) - float(baseline_temp), 1)

def x_calculate_temperature_anomaly__mutmut_14(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(None), 1)

def x_calculate_temperature_anomaly__mutmut_15(current_temp: float, baseline_temp: float) -> float:
    """
    Calculates the temperature anomaly against baseline climate averages.
    Returns anomaly rounded to 1 decimal place.
    """
    if not isinstance(current_temp, (int, float)) or not isinstance(baseline_temp, (int, float)):
        raise TypeError("Temperature values must be numeric (int or float).")
    return round(float(current_temp) - float(baseline_temp), 2)

mutants_x_calculate_temperature_anomaly__mutmut['_mutmut_orig'] = x_calculate_temperature_anomaly__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_1'] = x_calculate_temperature_anomaly__mutmut_1 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_2'] = x_calculate_temperature_anomaly__mutmut_2 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_3'] = x_calculate_temperature_anomaly__mutmut_3 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_4'] = x_calculate_temperature_anomaly__mutmut_4 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_5'] = x_calculate_temperature_anomaly__mutmut_5 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_6'] = x_calculate_temperature_anomaly__mutmut_6 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_7'] = x_calculate_temperature_anomaly__mutmut_7 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_8'] = x_calculate_temperature_anomaly__mutmut_8 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_9'] = x_calculate_temperature_anomaly__mutmut_9 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_10'] = x_calculate_temperature_anomaly__mutmut_10 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_11'] = x_calculate_temperature_anomaly__mutmut_11 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_12'] = x_calculate_temperature_anomaly__mutmut_12 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_13'] = x_calculate_temperature_anomaly__mutmut_13 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_14'] = x_calculate_temperature_anomaly__mutmut_14 # type: ignore # mutmut generated
mutants_x_calculate_temperature_anomaly__mutmut['x_calculate_temperature_anomaly__mutmut_15'] = x_calculate_temperature_anomaly__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_heatwave_risk__mutmut)
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


def x_classify_heatwave_risk__mutmut_orig(temp: float, anomaly: float) -> Dict[str, str]:
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


def x_classify_heatwave_risk__mutmut_1(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 and anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_2(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp > 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_3(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 44.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_4(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly > 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_5(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 5.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_6(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"XXstatusXX": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_7(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"STATUS": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_8(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "XXExtreme AlertXX", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_9(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "extreme alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_10(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "EXTREME ALERT", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_11(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "XXbadge_classXX": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_12(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "BADGE_CLASS": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_13(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "XXbadge-extremeXX", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_14(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "BADGE-EXTREME", "level": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_15(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "XXlevelXX": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_16(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "LEVEL": 4}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_17(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 5}
    elif temp >= 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_18(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 and anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_19(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp > 40.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_20(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 41.0 or anomaly >= 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_21(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly > 3.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_22(temp: float, anomaly: float) -> Dict[str, str]:
    """
    Classifies heatwave risk level based on temperature and anomaly thresholds:
    - Extreme Alert: temp >= 43.0 or anomaly >= 4.5
    - Severe Heat: temp >= 40.0 or anomaly >= 3.0
    - Mild Heat: temp >= 37.0 or anomaly >= 1.5
    - Normal Risk: otherwise
    """
    if temp >= 43.0 or anomaly >= 4.5:
        return {"status": "Extreme Alert", "badge_class": "badge-extreme", "level": 4}
    elif temp >= 40.0 or anomaly >= 4.0:
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_23(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"XXstatusXX": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_24(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"STATUS": "Severe Heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_25(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "XXSevere HeatXX", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_26(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "severe heat", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_27(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "SEVERE HEAT", "badge_class": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_28(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "XXbadge_classXX": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_29(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "BADGE_CLASS": "badge-high", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_30(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "badge_class": "XXbadge-highXX", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_31(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "badge_class": "BADGE-HIGH", "level": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_32(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "badge_class": "badge-high", "XXlevelXX": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_33(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "badge_class": "badge-high", "LEVEL": 3}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_34(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Severe Heat", "badge_class": "badge-high", "level": 4}
    elif temp >= 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_35(temp: float, anomaly: float) -> Dict[str, str]:
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
    elif temp >= 37.0 and anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_36(temp: float, anomaly: float) -> Dict[str, str]:
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
    elif temp > 37.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_37(temp: float, anomaly: float) -> Dict[str, str]:
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
    elif temp >= 38.0 or anomaly >= 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_38(temp: float, anomaly: float) -> Dict[str, str]:
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
    elif temp >= 37.0 or anomaly > 1.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_39(temp: float, anomaly: float) -> Dict[str, str]:
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
    elif temp >= 37.0 or anomaly >= 2.5:
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_40(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"XXstatusXX": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_41(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"STATUS": "Mild Heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_42(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "XXMild HeatXX", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_43(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "mild heat", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_44(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "MILD HEAT", "badge_class": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_45(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "XXbadge_classXX": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_46(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "BADGE_CLASS": "badge-low", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_47(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "badge_class": "XXbadge-lowXX", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_48(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "badge_class": "BADGE-LOW", "level": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_49(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "badge_class": "badge-low", "XXlevelXX": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_50(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "badge_class": "badge-low", "LEVEL": 2}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_51(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Mild Heat", "badge_class": "badge-low", "level": 3}
    else:
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_52(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"XXstatusXX": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_53(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"STATUS": "Normal Risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_54(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "XXNormal RiskXX", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_55(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "normal risk", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_56(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "NORMAL RISK", "badge_class": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_57(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "XXbadge_classXX": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_58(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "BADGE_CLASS": "badge-normal", "level": 1}


def x_classify_heatwave_risk__mutmut_59(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "badge_class": "XXbadge-normalXX", "level": 1}


def x_classify_heatwave_risk__mutmut_60(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "badge_class": "BADGE-NORMAL", "level": 1}


def x_classify_heatwave_risk__mutmut_61(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "badge_class": "badge-normal", "XXlevelXX": 1}


def x_classify_heatwave_risk__mutmut_62(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "badge_class": "badge-normal", "LEVEL": 1}


def x_classify_heatwave_risk__mutmut_63(temp: float, anomaly: float) -> Dict[str, str]:
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
        return {"status": "Normal Risk", "badge_class": "badge-normal", "level": 2}

mutants_x_classify_heatwave_risk__mutmut['_mutmut_orig'] = x_classify_heatwave_risk__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_1'] = x_classify_heatwave_risk__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_2'] = x_classify_heatwave_risk__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_3'] = x_classify_heatwave_risk__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_4'] = x_classify_heatwave_risk__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_5'] = x_classify_heatwave_risk__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_6'] = x_classify_heatwave_risk__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_7'] = x_classify_heatwave_risk__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_8'] = x_classify_heatwave_risk__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_9'] = x_classify_heatwave_risk__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_10'] = x_classify_heatwave_risk__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_11'] = x_classify_heatwave_risk__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_12'] = x_classify_heatwave_risk__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_13'] = x_classify_heatwave_risk__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_14'] = x_classify_heatwave_risk__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_15'] = x_classify_heatwave_risk__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_16'] = x_classify_heatwave_risk__mutmut_16 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_17'] = x_classify_heatwave_risk__mutmut_17 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_18'] = x_classify_heatwave_risk__mutmut_18 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_19'] = x_classify_heatwave_risk__mutmut_19 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_20'] = x_classify_heatwave_risk__mutmut_20 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_21'] = x_classify_heatwave_risk__mutmut_21 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_22'] = x_classify_heatwave_risk__mutmut_22 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_23'] = x_classify_heatwave_risk__mutmut_23 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_24'] = x_classify_heatwave_risk__mutmut_24 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_25'] = x_classify_heatwave_risk__mutmut_25 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_26'] = x_classify_heatwave_risk__mutmut_26 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_27'] = x_classify_heatwave_risk__mutmut_27 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_28'] = x_classify_heatwave_risk__mutmut_28 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_29'] = x_classify_heatwave_risk__mutmut_29 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_30'] = x_classify_heatwave_risk__mutmut_30 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_31'] = x_classify_heatwave_risk__mutmut_31 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_32'] = x_classify_heatwave_risk__mutmut_32 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_33'] = x_classify_heatwave_risk__mutmut_33 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_34'] = x_classify_heatwave_risk__mutmut_34 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_35'] = x_classify_heatwave_risk__mutmut_35 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_36'] = x_classify_heatwave_risk__mutmut_36 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_37'] = x_classify_heatwave_risk__mutmut_37 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_38'] = x_classify_heatwave_risk__mutmut_38 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_39'] = x_classify_heatwave_risk__mutmut_39 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_40'] = x_classify_heatwave_risk__mutmut_40 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_41'] = x_classify_heatwave_risk__mutmut_41 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_42'] = x_classify_heatwave_risk__mutmut_42 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_43'] = x_classify_heatwave_risk__mutmut_43 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_44'] = x_classify_heatwave_risk__mutmut_44 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_45'] = x_classify_heatwave_risk__mutmut_45 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_46'] = x_classify_heatwave_risk__mutmut_46 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_47'] = x_classify_heatwave_risk__mutmut_47 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_48'] = x_classify_heatwave_risk__mutmut_48 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_49'] = x_classify_heatwave_risk__mutmut_49 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_50'] = x_classify_heatwave_risk__mutmut_50 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_51'] = x_classify_heatwave_risk__mutmut_51 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_52'] = x_classify_heatwave_risk__mutmut_52 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_53'] = x_classify_heatwave_risk__mutmut_53 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_54'] = x_classify_heatwave_risk__mutmut_54 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_55'] = x_classify_heatwave_risk__mutmut_55 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_56'] = x_classify_heatwave_risk__mutmut_56 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_57'] = x_classify_heatwave_risk__mutmut_57 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_58'] = x_classify_heatwave_risk__mutmut_58 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_59'] = x_classify_heatwave_risk__mutmut_59 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_60'] = x_classify_heatwave_risk__mutmut_60 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_61'] = x_classify_heatwave_risk__mutmut_61 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_62'] = x_classify_heatwave_risk__mutmut_62 # type: ignore # mutmut generated
mutants_x_classify_heatwave_risk__mutmut['x_classify_heatwave_risk__mutmut_63'] = x_classify_heatwave_risk__mutmut_63 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_heat_index__mutmut)
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


def x_calculate_heat_index__mutmut_orig(temp_celsius: float, relative_humidity: float) -> float:
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


def x_calculate_heat_index__mutmut_1(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 and relative_humidity > 100:
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


def x_calculate_heat_index__mutmut_2(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity <= 0 or relative_humidity > 100:
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


def x_calculate_heat_index__mutmut_3(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 1 or relative_humidity > 100:
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


def x_calculate_heat_index__mutmut_4(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity >= 100:
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


def x_calculate_heat_index__mutmut_5(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 101:
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


def x_calculate_heat_index__mutmut_6(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError(None)
    
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


def x_calculate_heat_index__mutmut_7(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("XXRelative humidity must be between 0 and 100 percentage points.XX")
    
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


def x_calculate_heat_index__mutmut_8(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("relative humidity must be between 0 and 100 percentage points.")
    
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


def x_calculate_heat_index__mutmut_9(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("RELATIVE HUMIDITY MUST BE BETWEEN 0 AND 100 PERCENTAGE POINTS.")
    
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


def x_calculate_heat_index__mutmut_10(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = None
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


def x_calculate_heat_index__mutmut_11(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9/5) - 32
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


def x_calculate_heat_index__mutmut_12(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9 * 5) + 32
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


def x_calculate_heat_index__mutmut_13(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius / 9/5) + 32
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


def x_calculate_heat_index__mutmut_14(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 10/5) + 32
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


def x_calculate_heat_index__mutmut_15(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9/6) + 32
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


def x_calculate_heat_index__mutmut_16(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9/5) + 33
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


def x_calculate_heat_index__mutmut_17(temp_celsius: float, relative_humidity: float) -> float:
    """
    Calculates simplified Heat Index (°C) given temperature in Celsius and Relative Humidity (%).
    Formula uses NOAA Rothfusz regression approximation adapted for Celsius.
    """
    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("Relative humidity must be between 0 and 100 percentage points.")
    
    # Convert Celsius to Fahrenheit for standard NOAA equation
    T = (temp_celsius * 9/5) + 32
    RH = None

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


def x_calculate_heat_index__mutmut_18(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = None
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_19(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 / (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_20(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 1.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_21(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) - (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_22(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 - ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_23(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T - 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_24(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 62.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_25(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) / 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_26(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T + 68.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_27(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 69.0) * 1.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_28(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 2.2) + (RH * 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_29(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH / 0.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_30(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 1.094))
    
    if hi_f >= 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_31(temp_celsius: float, relative_humidity: float) -> float:
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
    
    if hi_f > 80:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_32(temp_celsius: float, relative_humidity: float) -> float:
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
    
    if hi_f >= 81:
        # Full Rothfusz equation
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_33(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = None

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_34(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH + 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_35(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH - 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_36(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH - 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_37(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T * RH - 0.00683783 * T * T + 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_38(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T * RH + 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_39(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH + 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_40(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 2.04901523 * T - 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_41(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 - 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_42(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (+42.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_43(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-43.379 + 2.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_44(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 2.04901523 / T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_45(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 3.04901523 * T + 10.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_46(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 2.04901523 * T + 10.14333127 / RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_47(temp_celsius: float, relative_humidity: float) -> float:
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
        hi_f = (-42.379 + 2.04901523 * T + 11.14333127 * RH
                - 0.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_48(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T / RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_49(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 / T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_50(temp_celsius: float, relative_humidity: float) -> float:
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
                - 1.22475541 * T * RH - 0.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_51(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T * RH - 0.00683783 * T / T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_52(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T * RH - 0.00683783 / T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_53(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.22475541 * T * RH - 1.00683783 * T * T
                - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_54(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH / RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_55(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 / RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_56(temp_celsius: float, relative_humidity: float) -> float:
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
                - 1.05481717 * RH * RH + 0.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_57(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH + 0.00122874 * T * T / RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_58(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH + 0.00122874 * T / T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_59(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH + 0.00122874 / T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_60(temp_celsius: float, relative_humidity: float) -> float:
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
                - 0.05481717 * RH * RH + 1.00122874 * T * T * RH
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_61(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH / RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_62(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T / RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_63(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 / T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_64(temp_celsius: float, relative_humidity: float) -> float:
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
                + 1.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_65(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH / RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_66(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH - 0.00000199 * T * T / RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_67(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH - 0.00000199 * T / T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_68(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH - 0.00000199 / T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_69(temp_celsius: float, relative_humidity: float) -> float:
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
                + 0.00085282 * T * RH * RH - 1.00000199 * T * T * RH * RH)

    # Convert back to Celsius
    hi_c = (hi_f - 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_70(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = None
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_71(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f - 32) * 5 * 9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_72(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f - 32) / 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_73(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f + 32) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_74(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f - 33) * 5/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_75(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f - 32) * 6/9
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_76(temp_celsius: float, relative_humidity: float) -> float:
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
    hi_c = (hi_f - 32) * 5/10
    return round(hi_c, 1)


def x_calculate_heat_index__mutmut_77(temp_celsius: float, relative_humidity: float) -> float:
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
    return round(None, 1)


def x_calculate_heat_index__mutmut_78(temp_celsius: float, relative_humidity: float) -> float:
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
    return round(hi_c, None)


def x_calculate_heat_index__mutmut_79(temp_celsius: float, relative_humidity: float) -> float:
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
    return round(1)


def x_calculate_heat_index__mutmut_80(temp_celsius: float, relative_humidity: float) -> float:
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
    return round(hi_c, )


def x_calculate_heat_index__mutmut_81(temp_celsius: float, relative_humidity: float) -> float:
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
    return round(hi_c, 2)

mutants_x_calculate_heat_index__mutmut['_mutmut_orig'] = x_calculate_heat_index__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_1'] = x_calculate_heat_index__mutmut_1 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_2'] = x_calculate_heat_index__mutmut_2 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_3'] = x_calculate_heat_index__mutmut_3 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_4'] = x_calculate_heat_index__mutmut_4 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_5'] = x_calculate_heat_index__mutmut_5 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_6'] = x_calculate_heat_index__mutmut_6 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_7'] = x_calculate_heat_index__mutmut_7 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_8'] = x_calculate_heat_index__mutmut_8 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_9'] = x_calculate_heat_index__mutmut_9 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_10'] = x_calculate_heat_index__mutmut_10 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_11'] = x_calculate_heat_index__mutmut_11 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_12'] = x_calculate_heat_index__mutmut_12 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_13'] = x_calculate_heat_index__mutmut_13 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_14'] = x_calculate_heat_index__mutmut_14 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_15'] = x_calculate_heat_index__mutmut_15 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_16'] = x_calculate_heat_index__mutmut_16 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_17'] = x_calculate_heat_index__mutmut_17 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_18'] = x_calculate_heat_index__mutmut_18 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_19'] = x_calculate_heat_index__mutmut_19 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_20'] = x_calculate_heat_index__mutmut_20 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_21'] = x_calculate_heat_index__mutmut_21 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_22'] = x_calculate_heat_index__mutmut_22 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_23'] = x_calculate_heat_index__mutmut_23 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_24'] = x_calculate_heat_index__mutmut_24 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_25'] = x_calculate_heat_index__mutmut_25 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_26'] = x_calculate_heat_index__mutmut_26 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_27'] = x_calculate_heat_index__mutmut_27 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_28'] = x_calculate_heat_index__mutmut_28 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_29'] = x_calculate_heat_index__mutmut_29 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_30'] = x_calculate_heat_index__mutmut_30 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_31'] = x_calculate_heat_index__mutmut_31 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_32'] = x_calculate_heat_index__mutmut_32 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_33'] = x_calculate_heat_index__mutmut_33 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_34'] = x_calculate_heat_index__mutmut_34 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_35'] = x_calculate_heat_index__mutmut_35 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_36'] = x_calculate_heat_index__mutmut_36 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_37'] = x_calculate_heat_index__mutmut_37 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_38'] = x_calculate_heat_index__mutmut_38 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_39'] = x_calculate_heat_index__mutmut_39 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_40'] = x_calculate_heat_index__mutmut_40 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_41'] = x_calculate_heat_index__mutmut_41 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_42'] = x_calculate_heat_index__mutmut_42 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_43'] = x_calculate_heat_index__mutmut_43 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_44'] = x_calculate_heat_index__mutmut_44 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_45'] = x_calculate_heat_index__mutmut_45 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_46'] = x_calculate_heat_index__mutmut_46 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_47'] = x_calculate_heat_index__mutmut_47 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_48'] = x_calculate_heat_index__mutmut_48 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_49'] = x_calculate_heat_index__mutmut_49 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_50'] = x_calculate_heat_index__mutmut_50 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_51'] = x_calculate_heat_index__mutmut_51 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_52'] = x_calculate_heat_index__mutmut_52 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_53'] = x_calculate_heat_index__mutmut_53 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_54'] = x_calculate_heat_index__mutmut_54 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_55'] = x_calculate_heat_index__mutmut_55 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_56'] = x_calculate_heat_index__mutmut_56 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_57'] = x_calculate_heat_index__mutmut_57 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_58'] = x_calculate_heat_index__mutmut_58 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_59'] = x_calculate_heat_index__mutmut_59 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_60'] = x_calculate_heat_index__mutmut_60 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_61'] = x_calculate_heat_index__mutmut_61 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_62'] = x_calculate_heat_index__mutmut_62 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_63'] = x_calculate_heat_index__mutmut_63 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_64'] = x_calculate_heat_index__mutmut_64 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_65'] = x_calculate_heat_index__mutmut_65 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_66'] = x_calculate_heat_index__mutmut_66 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_67'] = x_calculate_heat_index__mutmut_67 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_68'] = x_calculate_heat_index__mutmut_68 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_69'] = x_calculate_heat_index__mutmut_69 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_70'] = x_calculate_heat_index__mutmut_70 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_71'] = x_calculate_heat_index__mutmut_71 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_72'] = x_calculate_heat_index__mutmut_72 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_73'] = x_calculate_heat_index__mutmut_73 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_74'] = x_calculate_heat_index__mutmut_74 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_75'] = x_calculate_heat_index__mutmut_75 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_76'] = x_calculate_heat_index__mutmut_76 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_77'] = x_calculate_heat_index__mutmut_77 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_78'] = x_calculate_heat_index__mutmut_78 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_79'] = x_calculate_heat_index__mutmut_79 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_80'] = x_calculate_heat_index__mutmut_80 # type: ignore # mutmut generated
mutants_x_calculate_heat_index__mutmut['x_calculate_heat_index__mutmut_81'] = x_calculate_heat_index__mutmut_81 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_stakeholder_advisory__mutmut)
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


def x_generate_stakeholder_advisory__mutmut_orig(region: str, risk_level: str, category: str) -> str:
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


def x_generate_stakeholder_advisory__mutmut_1(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = None
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


def x_generate_stakeholder_advisory__mutmut_2(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.upper().strip()
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


def x_generate_stakeholder_advisory__mutmut_3(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region and not risk_level:
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


def x_generate_stakeholder_advisory__mutmut_4(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if region or not risk_level:
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


def x_generate_stakeholder_advisory__mutmut_5(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or risk_level:
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


def x_generate_stakeholder_advisory__mutmut_6(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError(None)

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


def x_generate_stakeholder_advisory__mutmut_7(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("XXRegion and risk level cannot be empty strings.XX")

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


def x_generate_stakeholder_advisory__mutmut_8(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("region and risk level cannot be empty strings.")

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


def x_generate_stakeholder_advisory__mutmut_9(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("REGION AND RISK LEVEL CANNOT BE EMPTY STRINGS.")

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


def x_generate_stakeholder_advisory__mutmut_10(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category != "agriculture":
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


def x_generate_stakeholder_advisory__mutmut_11(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "XXagricultureXX":
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


def x_generate_stakeholder_advisory__mutmut_12(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "AGRICULTURE":
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


def x_generate_stakeholder_advisory__mutmut_13(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level not in ["Extreme Alert", "Severe Heat"]:
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


def x_generate_stakeholder_advisory__mutmut_14(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["XXExtreme AlertXX", "Severe Heat"]:
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


def x_generate_stakeholder_advisory__mutmut_15(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["extreme alert", "Severe Heat"]:
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


def x_generate_stakeholder_advisory__mutmut_16(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["EXTREME ALERT", "Severe Heat"]:
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


def x_generate_stakeholder_advisory__mutmut_17(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["Extreme Alert", "XXSevere HeatXX"]:
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


def x_generate_stakeholder_advisory__mutmut_18(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["Extreme Alert", "severe heat"]:
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


def x_generate_stakeholder_advisory__mutmut_19(region: str, risk_level: str, category: str) -> str:
    """
    Generates tailored advisory messages for different stakeholder categories.
    Supported categories: 'agriculture', 'urban_health', 'municipal', 'general'
    """
    category = category.lower().strip()
    if not region or not risk_level:
        raise ValueError("Region and risk level cannot be empty strings.")

    if category == "agriculture":
        if risk_level in ["Extreme Alert", "SEVERE HEAT"]:
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


def x_generate_stakeholder_advisory__mutmut_20(region: str, risk_level: str, category: str) -> str:
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
    elif category != "urban_health":
        if risk_level in ["Extreme Alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_21(region: str, risk_level: str, category: str) -> str:
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
    elif category == "XXurban_healthXX":
        if risk_level in ["Extreme Alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_22(region: str, risk_level: str, category: str) -> str:
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
    elif category == "URBAN_HEALTH":
        if risk_level in ["Extreme Alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_23(region: str, risk_level: str, category: str) -> str:
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
        if risk_level not in ["Extreme Alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_24(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["XXExtreme AlertXX", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_25(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["extreme alert", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_26(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["EXTREME ALERT", "Severe Heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_27(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["Extreme Alert", "XXSevere HeatXX"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_28(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["Extreme Alert", "severe heat"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_29(region: str, risk_level: str, category: str) -> str:
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
        if risk_level in ["Extreme Alert", "SEVERE HEAT"]:
            return f"WARNING [{region}]: Open emergency cooling centers and deploy heat-stroke ambulances."
        return f"INFO [{region}]: Issue hydration public health announcements."
    elif category == "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_30(region: str, risk_level: str, category: str) -> str:
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
    elif category != "municipal":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_31(region: str, risk_level: str, category: str) -> str:
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
    elif category == "XXmunicipalXX":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."


def x_generate_stakeholder_advisory__mutmut_32(region: str, risk_level: str, category: str) -> str:
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
    elif category == "MUNICIPAL":
        return f"INFRASTRUCTURE [{region}]: Limit non-essential power usage to prevent grid overload during peak heat."
    else:
        return f"GENERAL [{region}]: Stay hydrated and avoid direct outdoor sunlight during peak daytime hours."

mutants_x_generate_stakeholder_advisory__mutmut['_mutmut_orig'] = x_generate_stakeholder_advisory__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_1'] = x_generate_stakeholder_advisory__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_2'] = x_generate_stakeholder_advisory__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_3'] = x_generate_stakeholder_advisory__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_4'] = x_generate_stakeholder_advisory__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_5'] = x_generate_stakeholder_advisory__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_6'] = x_generate_stakeholder_advisory__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_7'] = x_generate_stakeholder_advisory__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_8'] = x_generate_stakeholder_advisory__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_9'] = x_generate_stakeholder_advisory__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_10'] = x_generate_stakeholder_advisory__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_11'] = x_generate_stakeholder_advisory__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_12'] = x_generate_stakeholder_advisory__mutmut_12 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_13'] = x_generate_stakeholder_advisory__mutmut_13 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_14'] = x_generate_stakeholder_advisory__mutmut_14 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_15'] = x_generate_stakeholder_advisory__mutmut_15 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_16'] = x_generate_stakeholder_advisory__mutmut_16 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_17'] = x_generate_stakeholder_advisory__mutmut_17 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_18'] = x_generate_stakeholder_advisory__mutmut_18 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_19'] = x_generate_stakeholder_advisory__mutmut_19 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_20'] = x_generate_stakeholder_advisory__mutmut_20 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_21'] = x_generate_stakeholder_advisory__mutmut_21 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_22'] = x_generate_stakeholder_advisory__mutmut_22 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_23'] = x_generate_stakeholder_advisory__mutmut_23 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_24'] = x_generate_stakeholder_advisory__mutmut_24 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_25'] = x_generate_stakeholder_advisory__mutmut_25 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_26'] = x_generate_stakeholder_advisory__mutmut_26 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_27'] = x_generate_stakeholder_advisory__mutmut_27 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_28'] = x_generate_stakeholder_advisory__mutmut_28 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_29'] = x_generate_stakeholder_advisory__mutmut_29 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_30'] = x_generate_stakeholder_advisory__mutmut_30 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_31'] = x_generate_stakeholder_advisory__mutmut_31 # type: ignore # mutmut generated
mutants_x_generate_stakeholder_advisory__mutmut['x_generate_stakeholder_advisory__mutmut_32'] = x_generate_stakeholder_advisory__mutmut_32 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_filter_telemetry_data__mutmut)
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


def x_filter_telemetry_data__mutmut_orig(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
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


def x_filter_telemetry_data__mutmut_1(sensor_records: List[Dict[str, Any]], min_temp: float = 1.0) -> List[Dict[str, Any]]:
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


def x_filter_telemetry_data__mutmut_2(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = None
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_3(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record or "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_4(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "XXstation_idXX" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_5(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "STATION_ID" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_6(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" not in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_7(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "XXtemperatureXX" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_8(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "TEMPERATURE" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_9(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" not in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_10(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = None
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_11(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["XXtemperatureXX"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_12(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["TEMPERATURE"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_13(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) or temp >= min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_14(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp > min_temp:
                valid_records.append(record)
    return valid_records


def x_filter_telemetry_data__mutmut_15(sensor_records: List[Dict[str, Any]], min_temp: float = 0.0) -> List[Dict[str, Any]]:
    """
    Filters sensor telemetry records with valid data and temperature above min_temp.
    """
    valid_records = []
    for record in sensor_records:
        if "station_id" in record and "temperature" in record:
            temp = record["temperature"]
            if isinstance(temp, (int, float)) and temp >= min_temp:
                valid_records.append(None)
    return valid_records

mutants_x_filter_telemetry_data__mutmut['_mutmut_orig'] = x_filter_telemetry_data__mutmut_orig # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_1'] = x_filter_telemetry_data__mutmut_1 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_2'] = x_filter_telemetry_data__mutmut_2 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_3'] = x_filter_telemetry_data__mutmut_3 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_4'] = x_filter_telemetry_data__mutmut_4 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_5'] = x_filter_telemetry_data__mutmut_5 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_6'] = x_filter_telemetry_data__mutmut_6 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_7'] = x_filter_telemetry_data__mutmut_7 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_8'] = x_filter_telemetry_data__mutmut_8 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_9'] = x_filter_telemetry_data__mutmut_9 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_10'] = x_filter_telemetry_data__mutmut_10 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_11'] = x_filter_telemetry_data__mutmut_11 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_12'] = x_filter_telemetry_data__mutmut_12 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_13'] = x_filter_telemetry_data__mutmut_13 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_14'] = x_filter_telemetry_data__mutmut_14 # type: ignore # mutmut generated
mutants_x_filter_telemetry_data__mutmut['x_filter_telemetry_data__mutmut_15'] = x_filter_telemetry_data__mutmut_15 # type: ignore # mutmut generated
