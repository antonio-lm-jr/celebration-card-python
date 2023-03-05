import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def create_celebration_payload():
    return {
        "of": "mock-of",
        "to": "mock-to",
        "description": "mock-description",
    }
