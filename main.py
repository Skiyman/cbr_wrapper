import requests
import datetime
import xml_templates as templates
from cb_request import CbRequest
from xml_parser import XmlParser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session():
    session = requests.Session()

    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


if __name__ == "__main__":
    # session = create_session()
    # from_date = datetime.datetime.fromisoformat("2019-12-04").isoformat()
    # to_date = datetime.datetime.today().isoformat()
    # print(to_date)
    # args_data = [from_date, to_date, "R01090B"]
    # request = CbRequest(xml_template=templates.get_curs_dynamic, args_data=args_data, session=session)

    with open("text.xml", "r") as file:
        page = file.read()
    parser = XmlParser(page, templates.get_curs_dynamic["page_type"])
    print(parser.parse())

