# Idyllic Python

This is an example repository showing an "idyllic" setup for a basic Python web server application using [Litestar](https://litestar.dev/), a modern, fast, and flexible ASGI web framework.

## Features

- **Modern Python Web Framework**: Built with Litestar, a high-performance ASGI framework
- **Type Safety**: Full type hints and Pydantic models for request/response validation
- **Comprehensive Testing**: Complete test suite using Litestar's TestClient
- **Development Tools**: Pre-configured with Black, isort, mypy, and Ruff for code quality
- **Package Management**: Uses `uv` for fast and reliable dependency management
- **Clean Architecture**: Well-organized project structure following Python best practices

## API Endpoints

The application provides the following REST API endpoints:

- `GET /health` - Health check endpoint
- `GET /` - Welcome message
- `GET /hello/{name}` - Personalized greeting
- `GET /users` - List all users
- `GET /users/{user_id}` - Get a specific user by ID
- `POST /users` - Create a new user

## Project Structure

```
idyllic-python/
├── src/
│   └── idyllic_python/
│       ├── __init__.py
│       └── main.py          # Main application and route handlers
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test fixtures and configuration
│   ├── test_endpoints.py    # Endpoint tests
│   └── test_app_integration.py  # Integration tests
├── pyproject.toml           # Project configuration and dependencies
└── README.md
```

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd idyllic-python
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

   This will create a virtual environment and install all dependencies.

## Running the Application

### Using Make (Recommended)

```bash
# See all available commands
make help

# Run the development server
make run

# Run the production server
make run-prod
```

### Using uv directly

```bash
# Run the development server with uvicorn
uv run uvicorn idyllic_python.main:app --reload --host 127.0.0.1 --port 8000

# Or run the main module directly
uv run python -m idyllic_python.main
```

### Using uvicorn directly

```bash
# Activate the virtual environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run with uvicorn
uvicorn idyllic_python.main:app --reload --host 127.0.0.1 --port 8000
```

The application will be available at `http://127.0.0.1:8000`.

### Using Docker

```bash
# Build and run with Docker
make docker-build
make docker-run

# For production (multi-stage build)
make docker-build-prod
make docker-run-prod
```

## API Usage Examples

### Health Check
```bash
curl http://127.0.0.1:8000/health
```
Response:
```json
{
  "status": "healthy",
  "message": "Service is running"
}
```

### Create a User
```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```
Response:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Get All Users
```bash
curl http://127.0.0.1:8000/users
```
Response:
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
  ]
}
```

### Get User by ID
```bash
curl http://127.0.0.1:8000/users/1
```

### Personalized Greeting
```bash
curl http://127.0.0.1:8000/hello/Alice
```
Response:
```json
{
  "message": "Hello, Alice!"
}
```

## Testing

The project includes comprehensive tests using pytest and Litestar's TestClient.

### Run all tests:
```bash
uv run pytest
```

### Run tests with verbose output:
```bash
uv run pytest -v
```

### Run tests with coverage:
```bash
uv run pytest --cov=idyllic_python
```

### Test Structure

- **`tests/conftest.py`**: Shared fixtures and test configuration
- **`tests/test_endpoints.py`**: Individual endpoint tests organized by functionality
- **`tests/test_app_integration.py`**: Integration tests and application-level tests

The tests cover:
- All API endpoints
- Request/response validation
- Error handling
- Edge cases
- Integration scenarios

## Development

### Make Commands

The project includes a comprehensive Makefile for common development tasks:

```bash
# See all available commands
make help

# Install dependencies
make install

# Run all code quality checks
make check

# Format code
make format

# Run linting
make lint

# Run type checking
make typecheck

# Run tests
make test

# Run tests with coverage
make test-coverage

# Clean up cache files
make clean

# Docker commands
make docker-build
make docker-run
```

### Code Quality Tools

You can also run the tools directly:

```bash
# Format code with Black
uv run black src/ tests/

# Sort imports with isort
uv run isort src/ tests/

# Lint with Ruff
uv run ruff check src/ tests/

# Type checking with mypy
uv run mypy src/
```

### Adding Dependencies

Use `uv` to manage dependencies:

```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name
```

## Architecture Notes

### Framework Choice: Litestar

Litestar was chosen for this example because it provides:

- **High Performance**: Built on Starlette and Pydantic for speed
- **Modern Python**: Full support for type hints and async/await
- **Developer Experience**: Excellent error messages and debugging tools
- **Flexibility**: Supports both REST APIs and full web applications
- **Testing**: Built-in TestClient for easy testing

### Data Models

The application uses Pydantic models for request/response validation:

- `UserCreateRequest`: Validates user creation requests
- `UserResponse`: Standardizes user response format
- `HealthResponse`: Provides structured health check responses

### In-Memory Storage

For simplicity, this example uses in-memory storage. In a production application, you would typically use:

- A database (PostgreSQL, MySQL, etc.)
- An ORM (SQLAlchemy, Tortoise ORM, etc.)
- Proper data persistence and migrations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
