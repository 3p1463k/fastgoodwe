from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")


@router.get("/help/")
async def help(request: Request):

    context = {"request": request}
    return templates.TemplateResponse("general_pages/help.html", context)
