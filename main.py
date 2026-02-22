from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

# FastAPI app
app = FastAPI(title="Automotive Management API")

# Templates folder for front-end
templates = Jinja2Templates(directory="templates")

# Vehicle Model
class Vehicle(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: float

# Temporary in-memory storage
vehicles_db: List[Vehicle] = []

# -----------------------------
# Front-end Route
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

# -----------------------------
# Health Check (for Kubernetes)
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------
# API Endpoints
# -----------------------------

# Add Vehicle
@app.post("/vehicles")
def add_vehicle(vehicle: Vehicle):
    vehicles_db.append(vehicle)
    return vehicle

# View All Vehicles
@app.get("/vehicles")
def get_vehicles():
    return vehicles_db

# Get Single Vehicle
@app.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    for v in vehicles_db:
        if v.id == vehicle_id:
            return v
    return {"error": "Vehicle not found"}

# Delete Vehicle
@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    global vehicles_db
    vehicles_db = [v for v in vehicles_db if v.id != vehicle_id]
    return {"message": "Vehicle deleted"}
