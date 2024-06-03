from typing import Type

from templates.enum_valutes.parser import EnumValutesParser
from templates.get_curs_dynamic.parser import GetCursDynamicParser
from templates.get_curse_on_date.parser import GetCurseOnDateParser
from templates.iparser import IParser

"""
Parse data from xml request and convert in json response
"""


class XmlParserFactory:
    @staticmethod
    def get_parser(class_name: str) -> Type[IParser]:
        classes = {
            "get_curse_on_date": GetCurseOnDateParser,
            "enum_valutes": EnumValutesParser,
            "get_curs_dynamic": GetCursDynamicParser,
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_

        raise ValueError



