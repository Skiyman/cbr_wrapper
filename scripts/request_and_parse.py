from scripts.cb_request import CbRequest
from scripts.xml_parser import XmlParser


async def request_and_parse(template, args_data) -> list:
    request = CbRequest(xml_template=template, args_data=args_data)
    response = await request.make_request()

    parser = XmlParser(response, template["page_type"])
    parse_data = parser.parse()
    return parse_data
