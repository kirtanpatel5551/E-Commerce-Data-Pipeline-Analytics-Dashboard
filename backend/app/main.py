from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import Base,engine,get_db
from .models import Customer,Product,Order
Base.metadata.create_all(engine)
app=FastAPI(title="E-Commerce Analytics API")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/analytics/summary")
def summary(db:Session=Depends(get_db)):
    r=db.query(func.coalesce(func.sum(Order.revenue),0)).scalar()
    return {"revenue":round(float(r),2),"orders":db.query(Order).count(),"customers":db.query(Customer).count(),"products":db.query(Product).count()}
@app.get("/analytics/monthly-sales")
def monthly(db:Session=Depends(get_db)):
    d={}
    for o in db.query(Order).all():
        k=o.order_date.strftime("%Y-%m"); d[k]=round(d.get(k,0)+o.revenue,2)
    return [{"month":k,"revenue":v} for k,v in sorted(d.items())]
@app.get("/analytics/top-products")
def top(db:Session=Depends(get_db)):
    rows=db.query(Product.name,func.sum(Order.quantity),func.sum(Order.revenue)).join(Order,Product.id==Order.product_id).group_by(Product.id).order_by(func.sum(Order.revenue).desc()).limit(5).all()
    return [{"product":n,"units":int(u),"revenue":round(float(r),2)} for n,u,r in rows]
@app.get("/orders")
def orders(limit:int=10,db:Session=Depends(get_db)):
    rows=db.query(Order,Customer,Product).join(Customer,Order.customer_id==Customer.id).join(Product,Order.product_id==Product.id).order_by(Order.order_date.desc()).limit(min(limit,100)).all()
    return [{"id":o.id,"date":o.order_date,"customer":c.name,"product":p.name,"quantity":o.quantity,"revenue":o.revenue} for o,c,p in rows]
