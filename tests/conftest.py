"""Shared test fixtures and configuration."""

import pytest
from litestar.testing import TestClient

from idyllic_python.main import UserStorageProvider, create_app


@pytest.fixture
def app():
    """Create a fresh app instance for testing."""
    # Clear the singleton instance before each test
    UserStorageProvider.reset_instance()
    return create_app()


@pytest.fixture
def client(app):  # pylint: disable=redefined-outer-name
    """Create a test client for the app."""
    with TestClient(app=app) as test_client:
        yield test_client


@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return {"name": "John Doe", "email": "john.doe@example.com"}
