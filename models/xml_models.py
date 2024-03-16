from pydantic import BaseModel

from typing import Dict


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



class CurseDynamicModel(BaseModel):
    currency_date: str
    currency_rate: str
