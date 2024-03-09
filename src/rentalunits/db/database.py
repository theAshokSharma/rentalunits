from sqlmodel import SQLModel, create_engine, Session


# UIsing SQLite here but can easily use PostgreSQL by changing the url
sqlite_file_name = "data/rentalunits.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

# The engine is the interface to our database so we can execute SQL commands
engine = create_engine(sqlite_url, connect_args=connect_args)


# using the engine we create the tables we need if they aren't already done
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
