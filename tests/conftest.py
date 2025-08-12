"""Shared test fixtures and configuration."""

import pytest
from litestar.testing import TestClient

from idyllic_python.main import create_app


@pytest.fixture
def app():
    """Create a fresh app instance for testing."""
    # Clear the in-memory database before each test
    from idyllic_python.main import users_db

    users_db.clear()
    # Reset the user ID counter
    import idyllic_python.main

    idyllic_python.main.next_user_id = 1
    return create_app()


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    with TestClient(app=app) as test_client:
        yield test_client


@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return {"name": "John Doe", "email": "john.doe@example.com"}
