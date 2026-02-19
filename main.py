from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Automotive Management API")

# Vehicle Model
class Vehicle(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: float


# Temporary storage
vehicles_db: List[Vehicle] = []


@app.get("/")
def home():
    return {"message": "Welcome to Automotive Management System - Version 2 🚀"}



# Add Vehicle
@app.post("/vehicles")
def add_vehicle(vehicle: Vehicle):
    vehicles_db.append(vehicle)
    return {"message": "Vehicle added successfully"}


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
