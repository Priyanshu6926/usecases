"""
Unit & Integration Test Suite for Advisory & Early Warning Microservice
Validates FastAPI endpoints, Pydantic request models, response contracts,
error boundary conditions, and multilingual translations.
"""

import pytest
from fastapi.testclient import TestClient
from microservices.advisory_service import app

client = TestClient(app)


def test_root_endpoint():
    """Verify service identification and architecture metadata."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "HeatAware AI Advisory & Early Warning Microservice"
    assert data["status"] == "online"
    assert "endpoints" in data


def test_health_check_probe():
    """Verify liveness probe returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["port"] == 8001


def test_advisory_generate_extreme_heat_success():
    """Test advisory generation under extreme heat conditions (Level 4)."""
    payload = {
        "region": "Northwest India",
        "temperature": 44.5,
        "relative_humidity": 65.0,
        "stakeholder_type": "agriculture",
        "baseline_temp": 36.5,
        "language": "en"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["region"] == "Northwest India"
    assert data["stakeholder_type"] == "agriculture"
    assert data["metrics"]["risk_level"] == 4
    assert data["metrics"]["risk_status"] == "Extreme Alert"
    assert data["metrics"]["heat_index_celsius"] > 44.5
    assert len(data["action_items"]) > 0
    assert "Extreme Heat Alert" in data["advisory_headline"]


def test_advisory_generate_urban_health():
    """Test advisory generation for urban public health personnel."""
    payload = {
        "region": "Gangetic Plain",
        "temperature": 41.0,
        "relative_humidity": 50.0,
        "stakeholder_type": "urban_health",
        "baseline_temp": 38.0,
        "language": "en"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["metrics"]["risk_level"] == 3
    assert data["metrics"]["risk_status"] == "Severe Heat"


def test_advisory_multilingual_hindi():
    """Verify localized Hindi output generation."""
    payload = {
        "region": "Central India",
        "temperature": 45.0,
        "relative_humidity": 40.0,
        "stakeholder_type": "general",
        "baseline_temp": 37.0,
        "language": "hi"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["language"] == "hi"
    assert "अत्यधिक उष्णता चेतावनी" in data["advisory_headline"]


def test_advisory_multilingual_marathi():
    """Verify localized Marathi output generation."""
    payload = {
        "region": "Coastal Maharashtra",
        "temperature": 39.5,
        "relative_humidity": 75.0,
        "stakeholder_type": "municipal",
        "baseline_temp": 35.0,
        "language": "mr"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["language"] == "mr"
    assert "तीव्र उष्णतेची लाट" in data["advisory_headline"] or "अतिदक्षतेचा इशारा" in data["advisory_headline"]


def test_advisory_validation_error_humidity_out_of_bounds():
    """Pydantic must reject relative humidity values above 100%."""
    payload = {
        "region": "Northwest India",
        "temperature": 40.0,
        "relative_humidity": 125.0,  # Invalid
        "stakeholder_type": "general"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 422


def test_advisory_validation_error_temperature_out_of_bounds():
    """Pydantic must reject non-physical temperature values."""
    payload = {
        "region": "Northwest India",
        "temperature": 85.0,  # Above maximum 60.0 C
        "relative_humidity": 50.0,
        "stakeholder_type": "general"
    }
    response = client.post("/api/v1/advisory/generate", json=payload)
    assert response.status_code == 422


def test_architecture_specs_endpoint():
    """Verify architecture comparison specs endpoint returns all three paradigms."""
    response = client.get("/api/v1/advisory/specs")
    assert response.status_code == 200
    data = response.json()
    assert "monolithic" in data["architectures"]
    assert "three_tier" in data["architectures"]
    assert "microservices" in data["architectures"]
    assert data["architectures"]["microservices"]["coupling"] == "Loose (Zero direct code dependency with client)."
