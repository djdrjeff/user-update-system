import pandas as pd
from database import engine
from models import User, Base

Base.metadata.create_all(bind=engine)

df = pd.read_excel("data.xlsx")
df.to_sql("users", engine, if_exists="replace", index=False)

print("Excel data loaded successfully")
