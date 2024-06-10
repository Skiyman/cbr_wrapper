import asyncio
from datetime import datetime

import templates.xml_templates
from scripts.get_major_currencies import GetMajorCurrenciesRequest
from scripts.request_and_parse import request_and_parse


def main():
    asyncio.run(GetMajorCurrenciesRequest("USD").run())


if __name__ == '__main__':
    main()
