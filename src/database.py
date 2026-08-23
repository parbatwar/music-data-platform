from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://music_user:music_password@localhost:5433/music_db"

engine = create_engine(DATABASE_URL)

print("Database engine created")

# Connect SqlAlchemy engine to postgresql database and execute a simple query to test the connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.scalar())
