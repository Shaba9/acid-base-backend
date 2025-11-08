from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.calculations import calculate_pH
from typing import List, Dict

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

@app.get("/matching-pairs")
def get_matching_pairs(pH: float = Query(...)) -> Dict[str, List[Dict[str, float]]]:
    pairs = []

    for b in range(10, 41):  # bicarbonate range
        for p in range(20, 81):  # pCO2 range
            calc_ph = calculate_pH(b, p)
            if abs(calc_ph - pH) < 0.01:
                pairs.append({"bicarb": b, "pco2": p})

    return {"pairs": pairs}
