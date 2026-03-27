import urllib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=NOMBRE_DE_TU_SERVIDOR;" 
    "DATABASE=NOMBRE_DE_TU_BBDD;"   
    "Trusted_Connection=yes;"       
)

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    fast_executemany=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()