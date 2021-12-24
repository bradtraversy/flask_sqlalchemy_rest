import sqlalchemy
import psycopg2
import os
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Init app
app = FastAPI()

# set up security settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Database
db_uri = 'postgresql://gitpod@localhost/postgres'
# Init db
engine = sqlalchemy.create_engine(db_uri)


# Get All Products
@app.post('/product')
def get_products():
    df = pd.DataFrame({'name': ['User 1', 'User 2', 'User 3']})
    # df.to_sql('test',engine)
    print("-------------------DUDE")
    #all_products = Product.query.all()
    #result = products_schema.dump(all_products)
    print('hello')
    return {'name': ['User 1', 'User 2', 'User 3']}
