import os, snowflake.connector
from dotenv import load_dotenv

load_dotenv()
conn = snowflake.connector.connect(
    account=os.getenv("SF_ACCOUNT"),
    user=os.getenv("SF_USER"),
    password=os.getenv("SF_PASSWORD"),
)
cur = conn.cursor()
cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_VERSION()")
print("Connected:", cur.fetchone())
conn.close()
