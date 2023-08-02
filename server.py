from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import Race
import data
from random import choice

app = FastAPI()

@app.post("/npc")
async def name(json_info: Race):
    # breakpoint()
    if json_info.race is None:
        json_info.race = choice(data.races_list)
    if json_info.gender is None:
        json_info.gender = choice(("male", "female"))
    obj = data.races.get(json_info.race)(json_info.gender)
    return JSONResponse(obj.to_json())
