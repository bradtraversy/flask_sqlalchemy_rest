import sqlalchemy
import psycopg2
import os
import pandas as pd
from fastapi import FastAPI
import uvicorn



# Init app
app = FastAPI()
# Database
db_uri = 'postgresql://gitpod@localhost/postgres'
# Init db
engine = sqlalchemy.create_engine(db_uri)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get All Products
@app.post('/product')
def get_products():
  df=pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
  connection = db.raw_connection()
  df.to_sql('test',connection)
  print("-------------------DUDE")
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  print('hello')
  return jsonify(result)

@app.route('/', methods=['GET'])
def say_hello():
  return "<h1>hello there mate</h1>"



# Run Server
if __name__ == "__main__":
  uvicorn.run(app)

