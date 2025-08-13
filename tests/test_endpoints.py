"""Tests for all API endpoints."""

from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from litestar.testing import TestClient


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check_returns_healthy_status(self, client: TestClient):
        """Test that health check returns healthy status."""
        response = client.get("/health")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
        assert data["message"] == "Service is running"

    def test_health_check_response_structure(self, client: TestClient):
        """Test that health check response has correct structure."""
        response = client.get("/health")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert "status" in data
        assert "message" in data
        assert len(data) == 2  # Only these two fields


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_welcome_message(self, client: TestClient):
        """Test that root endpoint returns welcome message."""
        response = client.get("/")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert data["message"] == "Welcome to Idyllic Python API!"

    def test_root_response_structure(self, client: TestClient):
        """Test that root response has correct structure."""
        response = client.get("/")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert len(data) == 1


class TestHelloEndpoint:
    """Tests for the personalized greeting endpoint."""

    def test_hello_with_name_returns_personalized_greeting(self, client: TestClient):
        """Test that hello endpoint returns personalized greeting."""
        name = "Alice"
        response = client.get(f"/hello/{name}")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert data["message"] == f"Hello, {name}!"

    def test_hello_with_different_names(self, client: TestClient):
        """Test hello endpoint with different names."""
        names = ["Bob", "Charlie", "Diana"]

        for name in names:
            response = client.get(f"/hello/{name}")
            assert response.status_code == HTTP_200_OK
            data = response.json()
            assert data["message"] == f"Hello, {name}!"

    def test_hello_with_special_characters_in_name(self, client: TestClient):
        """Test hello endpoint with special characters in name."""
        name = "José"
        response = client.get(f"/hello/{name}")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert data["message"] == f"Hello, {name}!"


class TestUserEndpoints:
    """Tests for user-related endpoints."""

    def test_get_users_empty_initially(self, client: TestClient):
        """Test that users list is empty initially."""
        response = client.get("/users")

        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert "users" in data
        assert data["users"] == []

    def test_create_user_success(self, client: TestClient, sample_user_data):
        """Test successful user creation."""
        response = client.post("/users", json=sample_user_data)

        assert response.status_code == HTTP_201_CREATED
        data = response.json()
        assert data["name"] == sample_user_data["name"]
        assert data["email"] == sample_user_data["email"]
        assert "id" in data
        assert isinstance(data["id"], int)

    def test_create_user_missing_fields(self, client: TestClient):
        """Test user creation with missing fields."""
        incomplete_data = {"name": "John Doe"}  # Missing email
        response = client.post("/users", json=incomplete_data)

        assert response.status_code == 400  # Litestar returns 400 for validation errors

    def test_get_user_by_id_success(self, client: TestClient, sample_user_data):
        """Test getting a user by ID after creation."""
        # First create a user
        create_response = client.post("/users", json=sample_user_data)
        assert create_response.status_code == HTTP_201_CREATED
        created_user = create_response.json()
        user_id = created_user["id"]

        # Then get the user by ID
        get_response = client.get(f"/users/{user_id}")
        assert get_response.status_code == HTTP_200_OK

        retrieved_user = get_response.json()
        assert retrieved_user["id"] == user_id
        assert retrieved_user["name"] == sample_user_data["name"]
        assert retrieved_user["email"] == sample_user_data["email"]

    def test_get_user_by_id_not_found(self, client: TestClient):
        """Test getting a non-existent user by ID."""
        non_existent_id = 999
        response = client.get(f"/users/{non_existent_id}")

        assert response.status_code == HTTP_404_NOT_FOUND

    def test_get_users_after_creation(self, client: TestClient, sample_user_data):
        """Test that created users appear in the users list."""
        # Initially empty
        response = client.get("/users")
        assert len(response.json()["users"]) == 0

        # Create a user
        client.post("/users", json=sample_user_data)

        # Check users list
        response = client.get("/users")
        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert len(data["users"]) == 1
        assert data["users"][0]["name"] == sample_user_data["name"]

    def test_create_multiple_users(self, client: TestClient):
        """Test creating multiple users and verify they get unique IDs."""
        users_data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
            {"name": "Charlie", "email": "charlie@example.com"},
        ]

        created_users = []
        for user_data in users_data:
            response = client.post("/users", json=user_data)
            assert response.status_code == HTTP_201_CREATED
            created_users.append(response.json())

        # Verify unique IDs
        user_ids = [user["id"] for user in created_users]
        assert len(set(user_ids)) == len(user_ids)  # All IDs are unique

        # Verify all users are in the list
        response = client.get("/users")
        assert response.status_code == HTTP_200_OK
        all_users = response.json()["users"]
        assert len(all_users) == 3
