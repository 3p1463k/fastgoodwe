from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from apis.version1.functions.picklator import unpickl_sensor_list
from apis.version1.functions.query_inverter import get_data


router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")


@router.get("/inverters/")
async def inverter(request: Request):

    """Serve page and query inverter"""

    sensors_dict = await get_data()

    context = {"request": request, "sensors_list": sensors_dict}
    return templates.TemplateResponse("general_pages/homepage1.html", context)
