from fastapi import FastAPI
from middleware import log_request
from routes import users
from database import create_database

app = FastAPI()

@app.middleware("http")
async def middleware(request, call_next):
    """
    Middleware function to log HTTP requests.

    Parameters:
        request: Incoming HTTP request.
        call_next: The function to call to continue processing the request.

    Returns:
        HTTP response to the request.
    """
    response = await log_request(request, call_next)
    return response

app.include_router(users)

@app.on_event("startup")
async def startup_event() -> None:
    """
    This event is called when the application starts.

    It creates the SQL database if it doesn't exist.
    """
    create_database()
