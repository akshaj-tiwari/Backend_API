from fastapi import FastAPI
from app.routes.book_routes import router
app = FastAPI()

app.include_router(router)