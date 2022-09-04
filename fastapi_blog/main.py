from fastapi import FastAPI

from routes import routes


app = FastAPI(title='Blog', version='v1')

app.include_router(routes, prefix='/api/v1/')
