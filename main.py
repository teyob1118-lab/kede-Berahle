from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file = "../data/berahle_district_updated.xlsx"

def load(sheet):
    try:
        df = pd.read_excel(file, sheet_name=sheet)
        return df.fillna("").to_dict(orient="records")
    except:
        return []

@app.get("/")
def home():
    return {"message": "Berahle District API running"}

@app.get("/health")
def health():
    return load("Health_Facilities")

@app.get("/schools")
def schools():
    return load("Schools")

@app.get("/water")
def water():
    return load("Water_Sector")

@app.get("/agriculture")
def agriculture():
    return load("Agriculture")

@app.get("/infrastructure")
def infrastructure():
    return load("Infrastructure")

@app.get("/projects")
def projects():
    return load("Projects")

@app.get("/events")
def events():
    return load("Events")

@app.get("/ideas")
def ideas():
    return load("Ideas")