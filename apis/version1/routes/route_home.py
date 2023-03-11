import goodwe
from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import FastAPI
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from goodwe.exceptions import InverterError
from stampa.stampa import Stamp

from apis.version1.functions.picklator import pickle_ip


router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")
# discover_inverter = deta.Base("discover_inverter")


async def search_network_for_inverter():
    """Search network for inverter"""

    try:

        search_for_inverter = await goodwe.search_inverters()

        """Decode bytes input"""
        data = search_for_inverter.decode("utf-8").split(",")

        """If inverter found return data"""
        if data:

            dict_w_data = {
                "ip": data[0],
                "inverter": data[1],
                "wifi": data[2],
                "stamp": f"{Stamp('sec')}",
            }

            pickle_ip(dict_w_data["ip"])
            return dict_w_data

    except (InverterError):
        """Sleep for 60s if if any inverter errors"""

        return 0


@router.get("/")
async def home(request: Request):
    """Serve page and run inverter start_up"""

    data = await search_network_for_inverter()

    if data:

        context = {"request": request, "data": data}
        return templates.TemplateResponse("general_pages/discovery.html", context)

    context = {"request": request}
    return templates.TemplateResponse("general_pages/NOK.html", context)

    # context = {request: Request, "data":data}
    # return templates.TemplateResponse("general_pages/homepage.html", context)
