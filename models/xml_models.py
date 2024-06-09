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
    is_more: bool


class MajorCurrencyModel(BaseModel):
    name: str
    course: float
    is_more: bool
    previous_days: [ShortCurrencyModel]


class CurseDynamicModel(BaseModel):
    currency_date: str
    currency_rate: str
