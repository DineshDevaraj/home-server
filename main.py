
from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
router = APIRouter()

templates = Jinja2Templates(directory="templates")
app.mount("/learn/homeserver/static", StaticFiles(directory="static"), name="static")


@router.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(router, prefix="/learn/homeserver")
