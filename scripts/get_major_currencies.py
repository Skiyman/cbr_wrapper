import asyncio
from datetime import datetime, timedelta

from scripts.request_and_parse import request_and_parse
from templates import xml_templates

DOLLAR_STR_CODE = "USD"
EURO_STR_CODE = "EUR"


class GetMajorCurrenciesRequest:
    def __init__(self, currency_str_code):
        self.current_date = None
        self.code = None
        self.records = []
        self.str_code = currency_str_code

    async def run(self):
        self.current_date = await self.get_latest_record_date()
        await self.get_currencies_codes()
        self.records = await self.get_course_dynamic(self.code)

        response = {
            'name': self.str_code,
            'course': self.records[0]["currency_rate"],
            "is_more": self.compare_course(self.records[0]["currency_rate"], self.records[1]["currency_rate"])
        }

        previous_days = []
        for idx, record in enumerate(self.records[1: -1], start=1):
            previous_days.append({
                "date": record["currency_date"],
                "course": record["currency_rate"],
                "is_more": self.compare_course(record["currency_rate"], self.records[idx + 1]["currency_rate"])
            })

        response["previous_days"] = previous_days
        print(response)

    @staticmethod
    def compare_course(current_course, old_course):
        if current_course > old_course:
            return 1
        elif current_course < old_course:
            return -1
        elif current_course == old_course:
            return 0

    async def get_course_dynamic(self, currency_code, number_records=6):
        records = []
        begin_date = self.current_date - timedelta(days=number_records)

        while len(records) < number_records:
            args_data = [begin_date.isoformat(), self.current_date.isoformat(), currency_code]
            records = await request_and_parse(xml_templates.get_curs_dynamic, args_data)
            begin_date -= timedelta(days=1)

        return records[::-1]

    @staticmethod
    async def get_latest_record_date():
        latest_date = await request_and_parse(xml_templates.get_latest_date_time, [])
        return latest_date[0]

    async def get_currencies_codes(self):
        args_data = ["false"]
        response = await request_and_parse(xml_templates.enum_valutes, args_data)

        self.code = [i for i in response if i['currency_str_code'] == self.str_code][0]["currency_code"]
