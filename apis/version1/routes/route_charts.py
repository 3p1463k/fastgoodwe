from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")


@router.get("/charts/")
async def charts(request: Request):

    context = {"request": request}
    return templates.TemplateResponse("general_pages/charts.html", context)
