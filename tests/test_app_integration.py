"""Integration tests for the application."""

from litestar.testing import TestClient


class TestAppIntegration:
    """Integration tests for the entire application."""

    def test_app_creation(self, app):
        """Test that the app can be created successfully."""
        assert app is not None
        assert hasattr(app, "routes")

    def test_client_creation(self, client: TestClient):
        """Test that the test client can be created successfully."""
        assert client is not None

    def test_full_user_workflow(self, client: TestClient):
        """Test a complete user workflow: create, retrieve, list."""
        # Step 1: Verify no users initially
        response = client.get("/users")
        assert response.status_code == 200
        assert len(response.json()["users"]) == 0

        # Step 2: Create a user
        user_data = {"name": "Integration Test User", "email": "integration@test.com"}
        create_response = client.post("/users", json=user_data)
        assert create_response.status_code == 201
        created_user = create_response.json()
        user_id = created_user["id"]

        # Step 3: Retrieve the user by ID
        get_response = client.get(f"/users/{user_id}")
        assert get_response.status_code == 200
        retrieved_user = get_response.json()
        assert retrieved_user["name"] == user_data["name"]
        assert retrieved_user["email"] == user_data["email"]

        # Step 4: Verify user appears in users list
        list_response = client.get("/users")
        assert list_response.status_code == 200
        users_list = list_response.json()["users"]
        assert len(users_list) == 1
        assert users_list[0]["id"] == user_id

    def test_multiple_endpoints_in_sequence(self, client: TestClient):
        """Test calling multiple endpoints in sequence."""
        # Health check
        health_response = client.get("/health")
        assert health_response.status_code == 200

        # Root endpoint
        root_response = client.get("/")
        assert root_response.status_code == 200

        # Hello endpoint
        hello_response = client.get("/hello/TestUser")
        assert hello_response.status_code == 200

        # Users endpoint
        users_response = client.get("/users")
        assert users_response.status_code == 200

    def test_error_handling_integration(self, client: TestClient):
        """Test error handling across different scenarios."""
        # Test 404 for non-existent user
        response = client.get("/users/999")
        assert response.status_code == 404

        # Test validation error for incomplete user data
        response = client.post("/users", json={"name": "Only Name"})
        assert response.status_code == 400

        # Test 404 for non-existent endpoint
        response = client.get("/non-existent-endpoint")
        assert response.status_code == 404


class TestAppConfiguration:
    """Tests for application configuration."""

    def test_debug_mode_enabled(self, app):
        """Test that debug mode is enabled in the test app."""
        assert app.debug is True

    def test_route_handlers_registered(self, app):
        """Test that all expected route handlers are registered."""
        # Get all registered routes from the app's routes
        routes = []
        for route in app.routes:
            if hasattr(route, "path"):
                routes.append(route.path)

        # Expected routes (simplified patterns)
        expected_routes = ["/health", "/", "/users"]

        # Check that basic routes are present
        for expected_route in expected_routes:
            route_found = any(expected_route in str(route) for route in routes)
            assert (
                route_found
            ), f"Route {expected_route} not found in registered routes: {routes}"
