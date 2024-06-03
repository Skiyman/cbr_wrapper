from bs4 import BeautifulSoup

from templates.iparser import IParser


class EnumValutesParser(IParser):
    def parse(self, xml_page: str):
        page = BeautifulSoup(xml_page, "xml")
        response = []
        currencies = page.find_all("EnumValutes")

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
