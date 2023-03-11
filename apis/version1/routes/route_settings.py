import pickle

import goodwe
from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from apis.version1.functions.picklator import pickle_sensors_to_list

router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")
# inverter_data = deta.Base("inverter_data")


@router.get("/settings/")
async def setup_router(
    request: Request,
):
    ip_address = "10.0.0.228"

    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    sensors_dict = {}

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:

            # and sensor.name in sl1:
            # print(f"{sensor.id_}: \t\t {sensor.name} = {runtime_data[sensor.id_]} {sensor.unit}")
            # sensors_dict = {sensor.name : str(runtime_data[sensor.id_]) + " " + sensor.unit}
            sensors_dict[sensor.name] = (
                str(runtime_data[sensor.id_]) + " " + sensor.unit
            )

    sl = sensors_dict

    # print(sl)

    context = {"request": request, "sensors_list": sl}
    return templates.TemplateResponse("general_pages/settings.html", context)


@router.post("/ok/")
async def generate_list(
    request: Request,
):

    form_data = await request.form()
    print(form_data)

    sensors_to_save = [x for x in form_data]
    pickle_sensors_to_list(sensors_to_save)

    # inverter_data.put({"test":x})
    sl = sensors_to_save
    context = {"request": request, "sensors_list": sl}
    return templates.TemplateResponse("general_pages/OK.html", context)
