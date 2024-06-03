from bs4 import BeautifulSoup

from templates.iparser import IParser


class AllDataInfoParser(IParser):
    def __init__(self, xml_page: str, page_type: str):
        self.page = BeautifulSoup(xml_page, "xml")
        self.page_type = page_type

    def parse(self):
        raise NotImplementedError
