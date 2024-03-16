from fastapi import APIRouter

from models.xml_models import EnumCurseModel
from scripts.request_and_parse import request_and_parse
from templates import xml_templates

enum_currencies_router = APIRouter(
    prefix="/enum_currencies",
    tags=["EnumCurrencies"]
)


@enum_currencies_router.get("/")
async def get_enum_currencies() -> list[EnumCurseModel]:
    args_data = ["false"]
    response = await request_and_parse(xml_templates.enum_valutes, args_data)
    return response
