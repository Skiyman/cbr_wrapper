from bs4 import BeautifulSoup

"""
Parse data from xml request and convert in json response
"""


class XmlParser:
    def __init__(self, xml_page: str, page_type: str):
        self.page = BeautifulSoup(xml_page, "xml")
        self.page_type = page_type

    def parse(self) -> dict:
        response = {}
        if self.page_type == "get_curse_on_date":
            response = self.curse_on_date_parse()
        elif self.page_type == "enum_valutes":
            response = self.enum_valutes_parse()
        elif self.page_type == "get_curs_dynamic":
            response = self.get_curs_dynamic()

        return response

    def get_curs_dynamic(self) -> dict:
        response = {}
        currencies = self.page.find_all("ValuteCursDynamic")

        for currency in currencies:
            currency_date = currency.find("CursDate").text
            currency_rate = currency.find("Vcurs").text
            response[currency_date] = {"currency_rate": currency_rate}

        return response

    def enum_valutes_parse(self) -> dict:
        response = {}
        currencies = self.page.find_all("EnumValutes")

        for currency in currencies:
            currency_code = currency.find("Vcode").text.replace(" ", "")
            currency_name = currency.find("Vname").text.strip().replace("  ", "")
            try:
                currency_str_code = currency.find("VcharCode").text
            except AttributeError:
                continue

            response[currency_str_code] = {
                "currency_code": currency_code,
                "currency_name": currency_name
            }

        return response

    def curse_on_date_parse(self) -> dict:
        response = {}
        currencies = self.page.find_all("ValuteCursOnDate")

        for currency in currencies:
            currency_name = currency.find("Vname").text.strip().replace("  ", "")
            currency_denomination = currency.find("Vnom").text
            currency_rate = currency.find("Vcurs").text
            currency_iso_code = currency.find("Vcode").text
            currency_str_code = currency.find("VchCode").text
            currency_unit_rate = currency.find("VunitRate").text

            response[currency_str_code] = {
                "currency_name": currency_name,
                "currency_denomination": currency_denomination,
                "currency_rate": currency_rate,
                "currency_iso_code": currency_iso_code,
                "currency_unit_rate": currency_unit_rate,
            }

        return response
