import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base`
from sqlalchemy.orm import Session`
from sqlalchemy import create_engine`
from sqlalchemy.exc import SQLAlchemyError`
from getpass import getpass`
from sklearn.preprocessing import OneHotEncoder, LabelEncoder



engine = create_engine(
    host="anonymousendpoint.amazonaws.com",
    port='5432',
    database="mydb",
    user="admin",
    password="admin123"
)

engine.connect()
