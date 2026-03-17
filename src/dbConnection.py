from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from config import configSetting

engine = create_engine(configSetting.DB_PATH)

# Enable SQLite constraints on every connection
@event.listens_for(engine, "connect")
def enable_sqlite_constraints(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")           # enforce foreign keys
    cursor.execute("PRAGMA ignore_check_constraints = OFF")  # enforce CHECK constraints
    cursor.execute("PRAGMA recursive_triggers = ON")     # allow cascading triggers
    cursor.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()