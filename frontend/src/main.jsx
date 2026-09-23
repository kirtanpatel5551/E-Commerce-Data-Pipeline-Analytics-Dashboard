import React,{useEffect,useState} from "react";import{createRoot}from"react-dom/client";import"./styles.css";
const API="http://127.0.0.1:8000";
function App(){const[s,setS]=useState(null),[p,setP]=useState([]),[m,setM]=useState([]),[o,setO]=useState([]);
useEffect(()=>{Promise.all([fetch(API+"/analytics/summary").then(r=>r.json()),fetch(API+"/analytics/top-products").then(r=>r.json()),fetch(API+"/analytics/monthly-sales").then(r=>r.json()),fetch(API+"/orders").then(r=>r.json())]).then(([a,b,c,d])=>{setS(a);setP(b);setM(c);setO(d)})},[]);
if(!s)return <main><h1>Loading analytics...</h1></main>;
return <main><header><small>DATA ENGINEERING PORTFOLIO</small><h1>E-Commerce Analytics Dashboard</h1><p>Python ETL → SQL database → FastAPI → React</p></header>
<section className="cards">{[["Revenue","$"+s.revenue.toLocaleString()],["Orders",s.orders],["Customers",s.customers],["Products",s.products]].map(x=><div className="card"><span>{x[0]}</span><strong>{x[1]}</strong></div>)}</section>
<section className="grid"><article><h2>Monthly Revenue</h2>{m.map(x=><p><b>{x.month}</b> — ${x.revenue.toLocaleString()}</p>)}</article><article><h2>Top Products</h2>{p.map(x=><p><b>{x.product}</b> — {x.units} units — ${x.revenue.toLocaleString()}</p>)}</article></section>
<article><h2>Recent Orders</h2><table><tbody>{o.map(x=><tr><td>{x.date}</td><td>{x.customer}</td><td>{x.product}</td><td>{x.quantity}</td><td>${x.revenue}</td></tr>)}</tbody></table></article></main>}createRoot(document.getElementById("root")).render(<App/>);
