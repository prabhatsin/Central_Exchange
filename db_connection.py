from sqlalchemy import create_engine
import sqlalchemy
# print(sqlalchemy.__version__)
import os
from dotenv  import load_dotenv

url=os.load_dotenv("link")


engine=create_engine(url,echo=True)


