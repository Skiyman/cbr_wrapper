from scripts.cb_request import CbRequest
from templates.xml_parser_factory import XmlParserFactory


async def request_and_parse(template, args_data) -> list:
    request = CbRequest(xml_template=template, args_data=args_data)
    response = await request.make_request()

    parser = XmlParserFactory.get_parser(template["page_type"])()
    parse_data = parser.parse(response)
    return parse_data
