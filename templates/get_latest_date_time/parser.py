from datetime import datetime

from bs4 import BeautifulSoup

from templates.iparser import IParser


class GetLatestDateTimeParser(IParser):
    def parse(self, xml_page: str):
        page = BeautifulSoup(xml_page, "xml")
        response = []

        latest_date = page.find_all("GetLatestDateTimeResult")[0].text
        response.append(datetime.fromisoformat(latest_date))

        return response
