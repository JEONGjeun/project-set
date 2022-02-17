import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

file = request.files.get('fileInput') #파일은 화면 input창에서 받아온 것.

df = files = pd.read_excel(file)

engine = create_engine("postgresql://user:password@localhost:5432/postgres")
df.to_sql(name = 'airvisipinfo',
          con = engine,
          schema = 'public',
          if_exists = 'append',
          index = False
          )