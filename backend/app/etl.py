from pathlib import Path
import pandas as pd
from .database import Base,engine,SessionLocal
from .models import Customer,Product,Order
DATA=Path(__file__).resolve().parents[1]/"data"
def run_etl():
    c=pd.read_csv(DATA/"customers.csv").drop_duplicates("email").dropna()
    p=pd.read_csv(DATA/"products.csv").drop_duplicates("id").dropna()
    o=pd.read_csv(DATA/"orders.csv").drop_duplicates("id").dropna()
    o["order_date"]=pd.to_datetime(o["order_date"]).dt.date
    o=o[(o.quantity>0)&(o.revenue>=0)]
    Base.metadata.drop_all(engine); Base.metadata.create_all(engine)
    db=SessionLocal()
    try:
        db.add_all([Customer(**x) for x in c.to_dict("records")]); db.add_all([Product(**x) for x in p.to_dict("records")]); db.flush()
        db.add_all([Order(**x) for x in o.to_dict("records")]); db.commit()
        print(f"Loaded {len(c)} customers, {len(p)} products, {len(o)} orders")
    finally: db.close()
if __name__=="__main__": run_etl()
