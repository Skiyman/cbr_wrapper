from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def parse(self, xml_page: str):
        raise NotImplementedError
