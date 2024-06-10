from datetime import datetime

from fastapi import APIRouter

from models.xml_models import CurseOnDateModel, CurseDynamicModel, MajorCurrencyModel
from scripts.get_major_currencies import GetMajorCurrenciesRequest
from scripts.request_and_parse import request_and_parse
from templates import xml_templates

currency_router = APIRouter(
    prefix="/currencies",
    tags=["Currencies"]
)


@currency_router.get("")
async def get_today_currency_rate() -> list[CurseOnDateModel]:
    args_data = [datetime.today().isoformat()]
    response = await request_and_parse(xml_templates.get_curse_on_date, args_data)
    return response


@currency_router.get("/major/{currency_str_code}")
async def get_major_currencies(currency_str_code: str) -> MajorCurrencyModel | None:
    get_major_currencies_request = GetMajorCurrenciesRequest(currency_str_code)
    response = await get_major_currencies_request.run()
    return response


@currency_router.get("/rate/{date}")
async def get_date_currency_rate(date: str) -> list[CurseOnDateModel]:
    args_data = [datetime.fromisoformat(date).isoformat()]
    response = await request_and_parse(xml_templates.get_curse_on_date, args_data)
    return response


@currency_router.put("/dynamic/{currency_code}")
async def get_currency_dynamic(currency_code: str, begin_date: str, end_date: str) -> list[CurseDynamicModel]:
    args_data = [begin_date, end_date, currency_code]
    response = await request_and_parse(xml_templates.get_curs_dynamic, args_data)
    return response
