from sqlmodel import SQLModel, create_engine

def create_database():
    """
    Creates a SQLite database in the current directory and returns
    an engine that can be used to connect to it.

    The database file is named "database.db".

    The echo parameter is set to True to enable logging of SQL
    statements.
    """
    sqlite_file_name = "database.sqlite"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
    return engine