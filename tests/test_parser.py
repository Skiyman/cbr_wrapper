from typing import List

from pydantic import TypeAdapter

from models.xml_models import CurseOnDateModel, CurseDynamicModel
from templates.get_curs_dynamic.parser import GetCursDynamicParser
from templates.get_curse_on_date.parser import GetCurseOnDateParser
from tests.ext import today_currency_xml_response, course_dynamic_xml_response


def test_today_currency_xml_parser():
    parser = GetCurseOnDateParser()
    result = parser.parse(today_currency_xml_response)
    adapter = TypeAdapter(List[CurseOnDateModel])

    model = adapter.validate_python(result)

    assert model


def test_course_dynamic_xml_parser():
    parser = GetCursDynamicParser()
    result = parser.parse(course_dynamic_xml_response)
    adapter = TypeAdapter(List[CurseDynamicModel])

    model = adapter.validate_python(result)

    assert model
