"""Main application module for the Idyllic Python Litestar app."""

from typing import Any, Dict

from litestar import Litestar, get, post
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
users_db: Dict[int, Dict[str, Any]] = {}
next_user_id = 1


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
async def get_users() -> Dict[str, Any]:
    """Get all users."""
    return {"users": list(users_db.values())}


@get("/users/{user_id:int}")
async def get_user(user_id: int) -> UserResponse:
    """Get a specific user by ID."""
    if user_id not in users_db:
        from litestar.exceptions import NotFoundException

        raise NotFoundException(detail=f"User with ID {user_id} not found")

    user_data = users_db[user_id]
    return UserResponse(**user_data)


@post("/users", status_code=HTTP_201_CREATED)
async def create_user(data: UserCreateRequest) -> UserResponse:
    """Create a new user."""
    global next_user_id

    user_data: Dict[str, Any] = {
        "id": next_user_id,
        "name": data.name,
        "email": data.email,
    }

    users_db[next_user_id] = user_data
    next_user_id += 1

    return UserResponse(
        id=next_user_id - 1,
        name=data.name,
        email=data.email,
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
        debug=True,
    )


# Create the app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
