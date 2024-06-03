from bs4 import BeautifulSoup

from templates.iparser import IParser


class GetCurseOnDateParser(IParser):
    def parse(self, xml_page: str):
        page = BeautifulSoup(xml_page, "xml")
        response = []
        currencies = page.find_all("ValuteCursOnDate")

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
