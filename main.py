﻿from fastapi import FastAPI

app = FastAPI(title="EMA Darvas Trading System", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"api_version": "0.1.0"}
