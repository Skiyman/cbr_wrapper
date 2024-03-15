import requests
import datetime
import xml_templates as templates

"""
Make requests to CB api
"""


class CbRequest:
    def __init__(self, xml_template: dict, args_data: list[str], session: requests.session):
        self.request_headers = {"Content-Type": "text/xml; charset=utf-8"}
        self.request_body = xml_template['body']
        self.request_url = xml_template['url']
        self.request_args = xml_template['args']

        self.args_data = args_data

        self.session = session
        if len(self.args_data) != len(self.request_args):
            raise IndexError("Length of arguments and data do not match")
        if self.request_args:
            self.set_args()


    def set_args(self) -> None:
        for i in range(0, len(self.request_args)):
            argument_position = self.request_body.find(self.request_args[i]) + len(self.request_args[i]) + 1
            self.request_body = (self.request_body[:argument_position] + self.args_data[i] +
                                 self.request_body[argument_position:])

    def make_request(self) -> str:
        request = self.session.post(url=self.request_url, headers=self.request_headers, data=self.request_body)
        return request.text
