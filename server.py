from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import Race
from data import races
from random import choice

app = FastAPI()

@app.post("/npc")
async def name(json_info: Race):
    # breakpoint()
    if json_info.race is None:
        json_info.race = choice(races.races_list)
    if json_info.gender is None:
        json_info.gender = choice(("male", "female"))
    obj = races.races.get(json_info.race)(json_info.gender)
    return JSONResponse(obj.to_json())
