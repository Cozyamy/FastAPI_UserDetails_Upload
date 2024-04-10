from database import create_database
from sqlmodel import Session

async def get_session():
    """
        Asynchronous function to retrieve a session from the database.
    """
    engine = create_database()
    session = Session(engine)
    return session