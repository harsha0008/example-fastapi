from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# 1. Define your database credentials
DB_USER = "postgres"
DB_PASSWORD = "pabsys-sijFer-7xipju"
DB_HOST = "localhost"        # or your server IP
DB_PORT = "5432"             # default PostgreSQL port
DB_NAME = "myfastapi"

# 2. Construct the database URL (dialect+driver://user:password@host:port/dbname)
DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# 3. Create the SQLAlchemy engine
# The engine manages the connection pool under the hood.
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
# 4. Test the connection and execute a query
#try:
#    with engine.connect() as connection:
#        # Wrap the SQL string in text() for SQLAlchemy 2.0 compatibility
#        result = connection.execute(text("SELECT version();"))
#        for row in result:
#            print("Connected successfully! PostgreSQL version:", row[0])
            
#except Exception as e:
#    print("Error connecting to the database:", e)
