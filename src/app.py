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

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/metabaseconfig/{uid}")
def get_metabase_config(uid):
  if uid != False:
    return 'https://esg-analytics.herokuapp.com/embed/dashboard/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNvdXJjZSI6eyJkYXNoYm9hcmQiOjF9LCJwYXJhbXMiOnt9LCJleHAiOjE2MzkwNzYwODR9.CDowmbH6ExFJZwDsWUsYifpJm5e2g_eHtXA0H5uXI8A#theme=night&bordered=true&titled=true'
  return 'invalid uid'

# Get All Products
@app.post('/product')
def get_products():
  df=pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
  #df.to_sql('test',engine)
  print("-------------------DUDE")
  #all_products = Product.query.all()
  #result = products_schema.dump(all_products)
  print('hello')
  return {'name' : ['User 1', 'User 2', 'User 3']}

@app.route('/', methods=['GET'])
def say_hello():
  return "<h1>hello there mate</h1>"




# Run Server
if __name__ == "__main__":
  uvicorn.run(app)

