from bs4 import BeautifulSoup

from templates.iparser import IParser


class GetCursDynamicParser(IParser):
    def parse(self, xml_page: str):
        page = BeautifulSoup(xml_page, "xml")
        response = []
        currencies = page.find_all("ValuteCursDynamic")

        for currency in currencies:
            currency_date = currency.find("CursDate").text
            currency_rate = currency.find("Vcurs").text
            response.append({
                "currency_date": currency_date,
                "currency_rate": currency_rate
            })

        return response
