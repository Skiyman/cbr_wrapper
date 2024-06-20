from typing import List

from pydantic import BaseModel


class CurseOnDateModel(BaseModel):
    currency_str_code: str
    currency_name: str
    currency_denomination: int
    currency_rate: float
    currency_iso_code: int
    currency_unit_rate: float


class EnumCurseModel(BaseModel):
    currency_str_code: str
    currency_code: str
    currency_name: str


class ShortCurrencyModel(BaseModel):
    date: str
    course: float
    is_more: int


class MajorCurrencyModel(BaseModel):
    name: str
    course: float
    is_more: int
    previous_days: List[ShortCurrencyModel]


class CurseDynamicModel(BaseModel):
    currency_date: str
    currency_rate: float
