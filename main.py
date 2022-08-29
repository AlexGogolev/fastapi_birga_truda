from fastapi import FastAPI
import uvicorn
from db.base import database


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# приложение должно подключаться к БД на самом старте
@app.on_event("startapp")  # это выполняется во время старта приложения
async def startapp():
    await database.connect()
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
    
    