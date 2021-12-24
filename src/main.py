import uvicorn
from config.app import app
from config import firebase
from routers import main_routes, metabase_routes

# Run Server
if __name__ == "__main__":
    uvicorn.run(app)
