from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:Cosmos%40152209@localhost/Donation_db"
)

df = pd.read_csv("donation_data.csv")

df.to_sql(
    "donations",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Donations data loaded successfully")
