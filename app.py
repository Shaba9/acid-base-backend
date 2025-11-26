from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.calculations import calculate_pH
from typing import List, Dict
import numpy as np

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

@app.get("/matching-combos")
def get_matching_combos(pH: float = Query(...)) -> Dict[str, List[Dict[str, float]]]:
    combos = []
    for b in range(21, 27):  # bicarbonate range
        for vco2 in range(100, 1201, 100):  # CO2 production range
            for va in range(1, 16):  # alveolar ventilation range
                pco2 = (vco2 * 0.863) / va
                calc_ph = calculate_pH(b, pco2)
                if abs(calc_ph - pH) < 0.01:
                    combos.append({
                        "bicarbonate": b,
                        "vco2": vco2,
                        "va": va,
                        "pco2": pco2
                    })
    return {"combos": combos}
