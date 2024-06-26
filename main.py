import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.currency import currency_router
from routers.enum_currencies import enum_currencies_router

app = FastAPI()

origins = [
    "*"
]

app.include_router(currency_router)
app.include_router(enum_currencies_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
