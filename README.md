# FastAPI + SQLModel + UV + Docker POC

This guide walks you through creating a simple Proof of Concept (POC) API using modern Python tools.


## Run the Application

### Build and Start Services

```bash
# Build the Docker images
docker-compose build

# Start all services
docker-compose up -d

```

### Verify the Application

The API should now be running at `http://localhost:8000`

Navigate to http://localhost:8000/docs and use the built-in Swagger UI to test all endpoints interactively.

## Test the API

### Using curl

```bash
# Health check
curl http://localhost:8000/

# Create a user
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "full_name": "John Doe"}'

# Get all users
curl http://localhost:8000/users/

# Get specific user
curl http://localhost:8000/users/1

# Update user
curl -X PATCH http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"full_name": "John Smith"}'

# Delete user
curl -X DELETE http://localhost:8000/users/1
```

## Development Workflow

### Running Tests Locally (Optional)

If you want to add tests:

```bash
# Add pytest dependencies
uv add --dev pytest pytest-asyncio httpx
uv run pytest
```

### Hot Reloading

The docker-compose configuration includes volume mounting and `--reload` flag, so code changes will automatically reload the application.

## Useful Commands

```bash
# Stop services
docker-compose down

# Stop and remove volumes (clean database)
docker-compose down -v

# View logs
docker-compose logs -f

# Rebuild after dependency changes
docker-compose up -d --build

# Execute commands in running container
docker-compose exec api bash

# Check database directly
docker-compose exec db psql -U postgres -d appdb
```

## Project Structure Summary

```
fastapi-sqlmodel-poc/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLModel definitions
│   └── database.py      # Database configuration
├── tests/               # Optional: test files
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile           # Container definition
├── docker-compose.yml   # Multi-container setup
├── pyproject.toml       # UV project configuration
├── uv.lock             # Dependency lock file
├── .dockerignore
└── .gitignore
```

## Key Benefits of This Stack

1. **UV**: Fast dependency management and virtual environment handling
2. **FastAPI**: Modern, fast web framework with automatic API documentation
3. **SQLModel**: Type-safe ORM combining SQLAlchemy and Pydantic
4. **Docker**: Consistent development and deployment environment
5. **PostgreSQL**: Robust relational database

## Next Steps

- Add authentication (JWT tokens)
- Implement more complex relationships between models
- Add database migrations with Alembic
- Set up CI/CD pipeline
- Add comprehensive test coverage
- Implement logging and monitoring
- Add environment-specific configurations
