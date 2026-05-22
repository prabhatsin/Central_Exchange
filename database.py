
from sqlalchemy.engine import URL 
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv


# Put this inside the.env file 

#? URL creation 

load_dotenv()
# url=os.getenv("DATABASE_URL")
db_url = URL.create(
    drivername="postgresql",
    username="prabhat",
    password="pushpakviman@123",  # Write your raw password here naturally! No %40 needed.
    host="localhost",
    port=5432,
    database="cex_db"
)

#? engine creation

engine=create_engine(db_url,echo=True)
### whats this echo=True
# ---> Prints every SQL statement SQLAlchemy generates to stdout
# ---> Very useful for debugging — you see exactly what queries run

#? 
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
db=SessionLocal()

#  declarative base class
class Base(DeclarativeBase):
    pass
