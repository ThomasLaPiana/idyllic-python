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
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' | \
		sort

# =============================================================================
# Setup & Dependencies
# =============================================================================

.PHONY: install
install: ## Install dependencies using uv
	@echo "$(BLUE)Installing dependencies...$(RESET)"
	uv sync

.PHONY: deps-update
deps-update: ## Update all dependencies
	@echo "$(BLUE)Updating dependencies...$(RESET)"
	uv lock --upgrade

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

# =============================================================================
# Testing
# =============================================================================

.PHONY: test-verbose
test: ## Run tests with verbose output
	uv run pytest -v

.PHONY: test-coverage
test-coverage: ## Run tests with coverage report
	uv run pytest --cov=idyllic_python --cov-report=term-missing

.PHONY: test-watch
test-watch: ## Run tests in watch mode
	uv run pytest-watch

# =============================================================================
# Code Quality
# =============================================================================

.PHONY: black
black: ## Format code with black
	@echo "$(BLUE)Formatting code with black...$(RESET)"
	uv run black src/ tests/

.PHONY: isort
isort: ## Sort imports with isort
	@echo "$(BLUE)Sorting imports with isort...$(RESET)"
	uv run isort src/ tests/

.PHONY: ruff
ruff: ## Lint code with ruff
	@echo "$(BLUE)Linting code with ruff...$(RESET)"
	uv run ruff check src/ tests/

.PHONY: ruff-fix
ruff-fix: ## Lint and fix code with ruff
	@echo "$(BLUE)Linting and fixing code with ruff...$(RESET)"
	uv run ruff check --fix src/ tests/

.PHONY: mypy
mypy: ## Run type checking with mypy
	@echo "$(BLUE)Running type checks with mypy...$(RESET)"
	uv run mypy src/

.PHONY: pylint
pylint: ## Run code analysis with pylint
	@echo "$(BLUE)Running code analysis with pylint...$(RESET)"
	uv run pylint src/ tests/

.PHONY: radon-cc
radon-cc: ## Analyze cyclomatic complexity with radon
	@echo "$(BLUE)Analyzing cyclomatic complexity...$(RESET)"
	uv run radon cc src/ -s

.PHONY: radon-mi
radon-mi: ## Analyze maintainability index with radon
	@echo "$(BLUE)Analyzing maintainability index...$(RESET)"
	uv run radon mi src/ -s

.PHONY: radon
radon: radon-cc radon-mi ## Run all radon complexity analysis
	@echo "$(GREEN)Complexity analysis completed!$(RESET)"

.PHONY: pip-audit
pip-audit: ## Run security checks with pip-audit
	@echo "$(BLUE)Running security checks with pip-audit...$(RESET)"
	uv run pip-audit

.PHONY: check-all
check-all: black isort ruff-fix ruff pylint mypy radon pip-audit ## Run all quality checks
	@echo "$(GREEN)Standard quality checks completed!$(RESET)"

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
