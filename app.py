from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.calculations import calculate_pH

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calculate-ph")
def get_ph(bicarbonate: float = Query(...), pco2: float = Query(...)):
    return {"pH": calculate_pH(bicarbonate, pco2)}
