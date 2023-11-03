from fastapi import FastAPI

from app.routers import units, productions, plots, cultures, spreads

app = FastAPI(title="Demeter", version="0.1.0")

app.include_router(units.router)
app.include_router(productions.router)
app.include_router(plots.router)
app.include_router(spreads.router)
app.include_router(cultures.router)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
