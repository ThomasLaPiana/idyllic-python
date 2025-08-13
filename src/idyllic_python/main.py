"""Main application module for the Idyllic Python Litestar app."""

from typing import Any, Dict

from litestar import Litestar, get, post
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    message: str


class UserCreateRequest(BaseModel):
    """User creation request model."""

    name: str
    email: str


class UserResponse(BaseModel):
    """User response model."""

    id: int
    name: str
    email: str


# In-memory storage for demo purposes
class UserStorage:
    """Simple in-memory user storage."""

    def __init__(self) -> None:
        self.users_db: Dict[int, Dict[str, Any]] = {}
        self.next_user_id = 1

    def get_all_users(self) -> list[Dict[str, Any]]:
        """Get all users."""
        return list(self.users_db.values())

    def get_user(self, user_id: int) -> Dict[str, Any] | None:
        """Get a user by ID."""
        return self.users_db.get(user_id)

    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        """Create a new user."""
        user_data = {
            "id": self.next_user_id,
            "name": name,
            "email": email,
        }
        self.users_db[self.next_user_id] = user_data
        self.next_user_id += 1
        return user_data


class UserStorageProvider:
    """Singleton provider for UserStorage."""

    _instance: UserStorage | None = None

    @classmethod
    def get_instance(cls) -> UserStorage:
        """Get the singleton UserStorage instance."""
        if cls._instance is None:
            cls._instance = UserStorage()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton instance (useful for testing)."""
        cls._instance = None


def get_user_storage() -> UserStorage:
    """Dependency provider for UserStorage."""
    return UserStorageProvider.get_instance()


@get("/health", status_code=HTTP_200_OK)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy", message="Service is running")


@get("/")
async def root() -> Dict[str, str]:
    """Root endpoint with welcome message."""
    return {"message": "Welcome to Idyllic Python API!"}


@get("/hello/{name:str}")
async def hello_name(name: str) -> Dict[str, str]:
    """Personalized greeting endpoint."""
    return {"message": f"Hello, {name}!"}


@get("/users")
async def get_users(user_storage: UserStorage) -> Dict[str, Any]:
    """Get all users."""
    return {"users": user_storage.get_all_users()}


@get("/users/{user_id:int}")
async def get_user(user_id: int, user_storage: UserStorage) -> UserResponse:
    """Get a specific user by ID."""
    user_data = user_storage.get_user(user_id)
    if user_data is None:
        raise NotFoundException(detail=f"User with ID {user_id} not found")

    return UserResponse(**user_data)


@post("/users", status_code=HTTP_201_CREATED)
async def create_user(
    data: UserCreateRequest, user_storage: UserStorage
) -> UserResponse:
    """Create a new user."""
    user_data = user_storage.create_user(data.name, data.email)

    return UserResponse(
        id=user_data["id"],
        name=user_data["name"],
        email=user_data["email"],
    )


def create_app() -> Litestar:
    """Create and configure the Litestar application."""

    return Litestar(
        route_handlers=[
            health_check,
            root,
            hello_name,
            get_users,
            get_user,
            create_user,
        ],
        dependencies={"user_storage": Provide(get_user_storage, sync_to_thread=False)},
        debug=True,
    )


# Create the app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
