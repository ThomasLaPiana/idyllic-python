# Idyllic Python - Makefile
# This Makefile provides common development tasks for the Litestar application

.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

# =============================================================================
# Help
# =============================================================================

.PHONY: help
help: ## Show this help message
	@echo "$(BLUE)Idyllic Python - Available Commands$(RESET)"
	@echo ""
	@echo "$(BLUE)Setup & Dependencies:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^(install|deps)" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(BLUE)Development:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^(run|shell|docs)" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(BLUE)Testing:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^test" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(BLUE)Code Quality:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^(format|lint|typecheck|check|security)" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(BLUE)Docker:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^docker" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(BLUE)Utilities:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E "^(clean|build)" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-18s$(RESET) %s\n", $$1, $$2}'

# =============================================================================
# Setup & Dependencies
# =============================================================================

.PHONY: install
install: ## Install dependencies using uv
	@echo "$(BLUE)Installing dependencies...$(RESET)"
	uv sync

.PHONY: install-dev
install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(RESET)"
	uv sync --group dev

.PHONY: deps-update
deps-update: ## Update all dependencies
	@echo "$(BLUE)Updating dependencies...$(RESET)"
	uv lock --upgrade

.PHONY: deps-tree
deps-tree: ## Show dependency tree
	@echo "$(BLUE)Dependency tree:$(RESET)"
	uv tree

# =============================================================================
# Development
# =============================================================================

.PHONY: run
run: ## Run the development server
	@echo "$(BLUE)Starting development server...$(RESET)"
	uv run uvicorn idyllic_python.main:app --reload --host 127.0.0.1 --port 8000

.PHONY: run-prod
run-prod: ## Run the production server
	@echo "$(BLUE)Starting production server...$(RESET)"
	uv run uvicorn idyllic_python.main:app --host 0.0.0.0 --port 8000

.PHONY: shell
shell: ## Start an interactive Python shell with the app loaded
	@echo "$(BLUE)Starting Python shell...$(RESET)"
	uv run python -c "from idyllic_python.main import app; print('App loaded. Available: app'); import code; code.interact(local=locals())"

.PHONY: docs-serve
docs-serve: ## Serve API documentation (starts server for OpenAPI docs)
	@echo "$(BLUE)Starting server for API documentation...$(RESET)"
	@echo "$(YELLOW)API docs will be available at: http://127.0.0.1:8000/schema$(RESET)"
	@echo "$(YELLOW)Interactive docs at: http://127.0.0.1:8000/schema/swagger$(RESET)"
	uv run uvicorn idyllic_python.main:app --host 127.0.0.1 --port 8000

# =============================================================================
# Testing
# =============================================================================

.PHONY: test
test: ## Run all tests
	@echo "$(BLUE)Running tests...$(RESET)"
	uv run pytest

.PHONY: test-verbose
test-verbose: ## Run tests with verbose output
	@echo "$(BLUE)Running tests with verbose output...$(RESET)"
	uv run pytest -v

.PHONY: test-coverage
test-coverage: ## Run tests with coverage report
	@echo "$(BLUE)Running tests with coverage...$(RESET)"
	uv run pytest --cov=idyllic_python --cov-report=term-missing

.PHONY: test-watch
test-watch: ## Run tests in watch mode
	@echo "$(BLUE)Running tests in watch mode...$(RESET)"
	uv run pytest-watch

# =============================================================================
# Code Quality
# =============================================================================

.PHONY: format
format: ## Format code with black and isort
	@echo "$(BLUE)Formatting code...$(RESET)"
	uv run black src/ tests/
	uv run isort src/ tests/

.PHONY: lint
lint: ## Lint code with ruff
	@echo "$(BLUE)Linting code...$(RESET)"
	uv run ruff check src/ tests/

.PHONY: lint-fix
lint-fix: ## Lint and fix code with ruff
	@echo "$(BLUE)Linting and fixing code...$(RESET)"
	uv run ruff check --fix src/ tests/

.PHONY: typecheck
typecheck: ## Run type checking with mypy
	@echo "$(BLUE)Running type checks...$(RESET)"
	uv run mypy src/

.PHONY: check
check: format lint typecheck test ## Run all code quality checks
	@echo "$(GREEN)All checks completed!$(RESET)"

.PHONY: security
security: ## Run security checks (requires pip-audit)
	@echo "$(BLUE)Running security checks...$(RESET)"
	uv run pip-audit

# =============================================================================
# Docker
# =============================================================================

.PHONY: docker-build
docker-build: ## Build Docker image
	@echo "$(BLUE)Building Docker image...$(RESET)"
	docker build -t idyllic-python .

.PHONY: docker-run
docker-run: ## Run Docker container
	@echo "$(BLUE)Running Docker container...$(RESET)"
	docker run --rm -p 8000:8000 idyllic-python


# =============================================================================
# Utilities
# =============================================================================

.PHONY: clean
clean: ## Clean up cache files and build artifacts
	@echo "$(BLUE)Cleaning up...$(RESET)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf build/ dist/

.PHONY: build
build: ## Build the package
	@echo "$(BLUE)Building package...$(RESET)"
	uv build
