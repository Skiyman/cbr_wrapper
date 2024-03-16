from bs4 import BeautifulSoup

from models.xml_models import CurseOnDateModel

"""
Parse data from xml request and convert in json response
"""


class XmlParser:
    def __init__(self, xml_page: str, page_type: str):
        self.page = BeautifulSoup(xml_page, "xml")
        self.page_type = page_type

    def parse(self) -> list | CurseOnDateModel:
        response = {}
        if self.page_type == "get_curse_on_date":
            response = self.curse_on_date_parse()
        elif self.page_type == "enum_valutes":
            response = self.enum_valutes_parse()
        elif self.page_type == "get_curs_dynamic":
            response = self.curs_dynamic_parse()

        return response

    def curs_dynamic_parse(self) -> list:
        response = []
        currencies = self.page.find_all("ValuteCursDynamic")

        for currency in currencies:
            currency_date = currency.find("CursDate").text
            currency_rate = currency.find("Vcurs").text
            response.append({
                "currency_date": currency_date,
                "currency_rate": currency_rate
            })

        return response

    def enum_valutes_parse(self) -> list:
        response = []
        currencies = self.page.find_all("EnumValutes")

        for currency in currencies:
            currency_code = currency.find("Vcode").text.replace(" ", "")
            currency_name = currency.find("Vname").text.strip().replace("  ", "")
            try:
                currency_str_code = currency.find("VcharCode").text
            except AttributeError:
                continue

            response.append({
                "currency_str_code": currency_str_code,
                "currency_code": currency_code,
                "currency_name": currency_name
            })

        return response

    def curse_on_date_parse(self) -> list:
        response = []
        currencies = self.page.find_all("ValuteCursOnDate")

        for currency in currencies:
            currency_name = currency.find("Vname").text.strip().replace("  ", "")
            currency_denomination = int(currency.find("Vnom").text)
            currency_rate = float(currency.find("Vcurs").text)
            currency_iso_code = int(currency.find("Vcode").text)
            currency_str_code = currency.find("VchCode").text
            currency_unit_rate = float(currency.find("VunitRate").text)

            response.append({
                "currency_str_code": currency_str_code,
                "currency_name": currency_name,
                "currency_denomination": currency_denomination,
                "currency_rate": currency_rate,
                "currency_iso_code": currency_iso_code,
                "currency_unit_rate": currency_unit_rate,
            })

        return response

