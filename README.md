# Idyllic Python

[![CI/CD Pipeline](https://github.com/yourusername/idyllic-python/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/idyllic-python/actions/workflows/ci.yml)
[![Release Pipeline](https://github.com/yourusername/idyllic-python/actions/workflows/release.yml/badge.svg)](https://github.com/yourusername/idyllic-python/actions/workflows/release.yml)
[![Maintenance](https://github.com/yourusername/idyllic-python/actions/workflows/maintenance.yml/badge.svg)](https://github.com/yourusername/idyllic-python/actions/workflows/maintenance.yml)

A comprehensive template for modern Python web applications, demonstrating industry best practices, comprehensive tooling, and automated workflows. Built with [Litestar](https://litestar.dev/) and designed as a production-ready foundation for new projects.

## Overview

This repository serves as a reference implementation and template that incorporates:

- **Modern Architecture**: Clean dependency injection, type safety, and SOLID principles
- **Comprehensive Tooling**: Essential development tools with proper configuration
- **Production-Ready CI/CD**: Automated quality gates, testing, and deployment
- **Quality Excellence**: Consistent high-quality code standards
- **Security Focus**: Automated vulnerability scanning and dependency management
- **Complete Documentation**: Clear and maintainable project documentation

**Use Cases**: Starting new projects, upgrading existing codebases, or learning modern Python development practices.

## Key Features

### Modern Architecture & Design

- **Dependency Injection**: Clean, testable architecture using Litestar's DI system
- **Type Safety**: Full type annotations with mypy validation (100% coverage)
- **SOLID Principles**: Proper separation of concerns and clean code practices
- **Modern Python**: Leverages Python 3.11+ features and best practices

### Comprehensive Development Tooling

- **Package Management**: [uv](https://github.com/astral-sh/uv) for fast dependency management
- **Code Formatting**: [Black](https://black.readthedocs.io/) + [isort](https://pycqa.github.io/isort/) for consistent style
- **Linting**: [Ruff](https://docs.astral.sh/ruff/) for comprehensive linting
- **Type Checking**: [mypy](https://mypy.readthedocs.io/) for static type analysis
- **Code Quality**: [Pylint](https://pylint.pycqa.org/) for detailed code analysis
- **Complexity Analysis**: [Radon](https://radon.readthedocs.io/) for maintainability metrics
- **Security**: [pip-audit](https://pypi.org/project/pip-audit/) for vulnerability scanning

### Production-Ready CI/CD

- **Matrix Parallelization**: All quality tools run simultaneously for fast feedback
- **Multi-Version Testing**: Automated testing across Python 3.11, 3.12, and 3.13
- **Docker Integration**: Containerized deployment with multi-platform support
- **Automated Releases**: Tag-triggered releases with changelog generation
- **Dependency Updates**: Weekly automated dependency updates with quality validation

### Quality Standards

- **High Code Quality**: 10.0/10 Pylint score, 100% type coverage
- **Comprehensive Testing**: Unit tests, integration tests, and coverage reporting
- **Security Focus**: Automated vulnerability scanning and dependency auditing
- **Complete Documentation**: Clear documentation with examples

### Developer Experience

- **Make Integration**: Simple commands for all development tasks
- **Local Testing**: Full CI/CD pipeline simulation locally
- **IDE Support**: Proper configuration for VS Code, PyCharm, and other IDEs
- **Hot Reloading**: Development server with automatic reload

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

```text
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
├── .github/
│   └── workflows/           # GitHub Actions CI/CD workflows
├── pyproject.toml           # Project configuration and dependencies
├── Dockerfile               # Container configuration
├── Makefile                 # Development commands
└── README.md                # Project documentation
```

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

## Quick Start

### Using as a Template

1. **Use this template:**

   ```bash
   # Click "Use this template" on GitHub, or clone directly:
   git clone https://github.com/yourusername/idyllic-python.git my-new-project
   cd my-new-project
   ```

2. **Customize for your project:**

   ```bash
   # Update project name in pyproject.toml
   # Update package name in src/
   # Update README.md with your project details
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

4. **Verify everything works:**

   ```bash
   make check-all  # Run all quality checks
   make test       # Run tests
   make run        # Start development server
   ```

5. **Start developing:**
   - Visit `http://127.0.0.1:8000` to see your app
   - Modify `src/idyllic_python/main.py` to add your features
   - Use `make help` to see all available commands

## Template Customization Guide

### Essential Files to Update

When using this as a template, update these key files:

**Project Configuration:**

- `pyproject.toml` - Update name, description, authors, and URLs
- `Dockerfile` - Modify if you need different base image or dependencies
- `.github/workflows/*.yml` - Update repository URLs in badges and deployment targets

**Source Code:**

- `src/idyllic_python/` - Rename package directory to match your project
- `src/idyllic_python/main.py` - Replace example endpoints with your application logic
- `tests/` - Update test files to match your new package structure

**Documentation:**

- `README.md` - Replace with your project's documentation
- `LICENSE` - Update with your preferred license
- `.github/SETUP.md` - Customize CI/CD setup instructions

### Best Practices Included

This template demonstrates:

**Architecture Patterns:**

- Dependency injection for testable, maintainable code
- Clean separation between business logic and framework code
- Type-safe interfaces and data models
- Proper error handling and HTTP status codes

**Development Workflow:**

- Pre-commit hooks for code quality (via make targets)
- Comprehensive testing strategy with fixtures and mocks
- Local development environment that mirrors production
- Documentation-driven development

**Production Readiness:**

- Multi-stage Docker builds for optimized images
- Health checks and monitoring endpoints
- Proper logging and error handling
- Security best practices and vulnerability scanning

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

## Development Guide

This section demonstrates the development workflow and tooling configuration.

### Individual Quality Tools

Each tool can be run independently for focused development:

```bash
# Code Formatting
make black          # Format code with Black
make isort          # Sort imports with isort
make format         # Run both Black and isort

# Linting & Analysis
make ruff           # Fast linting with Ruff
make ruff-fix       # Auto-fix issues with Ruff
make lint           # Run linting (alias for ruff)
make lint-fix       # Auto-fix linting issues

# Type Checking
make mypy           # Static type analysis

# Code Quality Analysis
make pylint         # Comprehensive code analysis
make radon-cc       # Cyclomatic complexity analysis
make radon-mi       # Maintainability index analysis
make radon          # All complexity analysis

# Security
make pip-audit      # Security vulnerability scanning
```

### Comprehensive Workflows

For complete quality assurance:

```bash
# Run ALL quality checks (recommended before commits)
make check-all      # Exhaustive quality validation

# Testing
make test           # Run test suite
make test-coverage  # Run tests with coverage report
make test-watch     # Run tests in watch mode

# Development
make run            # Start development server
make run-prod       # Start production server

# Docker
make docker-build   # Build container image
make docker-run     # Run containerized application
```

### Development Approach

This Makefile demonstrates industry best practices:

- **Granular Control**: Run individual tools for focused debugging
- **Composite Commands**: Combine related tools for efficient workflows
- **Consistent Interface**: Same command structure across all tools
- **Fast Feedback**: Parallel execution where possible
- **CI/CD Ready**: Commands mirror exactly what runs in automation

### Code Quality Tools

The project includes comprehensive code quality tools:

- **Black** - Code formatting
- **isort** - Import sorting
- **Ruff** - Fast Python linter with many rules
- **mypy** - Static type checking
- **Pylint** - Comprehensive code analysis
- **Radon** - Code complexity analysis

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

# Code analysis with Pylint
uv run pylint src/ tests/

# Complexity analysis with Radon
uv run radon cc src/ -s  # Cyclomatic complexity
uv run radon mi src/ -s  # Maintainability index
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

## CI/CD Pipeline

The project includes comprehensive CI/CD workflows using GitHub Actions:

### Continuous Integration (`ci.yml`)

- Matrix-based parallelization of all quality tools
- Multi-version Python testing (3.11, 3.12, 3.13)
- Docker build verification
- Security auditing
- Automated package building

**Quality Tools (Parallelized):**

- `black` - Code formatting
- `isort` - Import sorting
- `ruff` - Fast linting
- `mypy` - Type checking
- `pylint` - Code analysis
- `radon-cc` - Complexity analysis
- `radon-mi` - Maintainability index
- `pip-audit` - Security audit

### Release Pipeline (`release.yml`)

- Automated releases on version tags
- Multi-platform Docker images (AMD64, ARM64)
- PyPI package publishing
- GitHub release creation with changelog
- Comprehensive quality gate

### Maintenance (`maintenance.yml`)

- Weekly dependency updates
- Automated security audits
- Quality report generation
- Docker image maintenance

### Workflow Triggers

```yaml
# CI runs on:
- push to main/develop
- pull requests
- manual dispatch

# Release runs on:
- version tags (v*)
- manual dispatch

# Maintenance runs:
- weekly (Sundays 2 AM UTC)
- manual dispatch
```

## What Makes This Template Valuable?

### Measurable Quality

- **Perfect Pylint Score**: 10.0/10 demonstrating code excellence
- **100% Type Coverage**: Full mypy validation with no type errors
- **Comprehensive Testing**: 21 tests covering all functionality
- **Zero Security Vulnerabilities**: Clean pip-audit results
- **Low Complexity**: All functions rated 'A' for maintainability

### Modern Development Practices

- **Dependency Injection**: Clean, testable architecture
- **Type Safety**: Full type annotations throughout
- **Automated Quality Gates**: No manual quality checks needed
- **Container-First**: Docker-ready from day one
- **Security-First**: Automated vulnerability scanning

### Production-Ready Features

- **Multi-Platform Support**: ARM64 and AMD64 Docker images
- **Health Checks**: Built-in monitoring endpoints
- **Proper Error Handling**: Structured error responses
- **Logging Ready**: Structured logging configuration
- **Scalable Architecture**: Clean separation of concerns

### Learning Resource

This repository serves as a comprehensive example of:

- Modern Python project structure
- Industry-standard tooling configuration
- CI/CD best practices
- Testing strategies
- Documentation standards

### Template Benefits

- **Immediate Productivity**: Start coding features, not infrastructure
- **Quality Assurance**: Built-in quality gates prevent technical debt
- **Team Onboarding**: Clear patterns and documentation
- **Maintenance**: Automated dependency updates and security scanning
- **Scalability**: Architecture that grows with your project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
