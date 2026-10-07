from fastapi import FastAPI
from src.routes.productRoute import productRoutes

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}

app.include_router(productRoutes, prefix = '/products' )

