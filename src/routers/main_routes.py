from config.app import app

@app.get("/")
async def root():
    return {"message": "Hello World"}