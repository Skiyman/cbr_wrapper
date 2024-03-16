import uvicorn

from fastapi import FastAPI

from routers.currency import currency_router
from routers.enum_currencies import enum_currencies_router

app = FastAPI()


@app.get('/')
async def home() -> dict:
    return {
        "msg": "Hello World!!!"
    }


app.include_router(currency_router)
app.include_router(enum_currencies_router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
