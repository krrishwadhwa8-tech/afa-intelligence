from fastapi import FastAPI
from api.analyze import router
from api.market_pulse import (
    router as market_router
)
from api.dashboard import (
    router as dashboard_router
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AFA Intelligence API",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(market_router)
app.include_router(
    dashboard_router
)
@app.get("/")
def root():
    return {
        "name": "AFA Intelligence API",
        "status": "online",
        "version": "1.0"
    }