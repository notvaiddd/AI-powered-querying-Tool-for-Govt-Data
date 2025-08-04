from sqlalchemy import create_engine 
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB = 'survey_db'

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)
