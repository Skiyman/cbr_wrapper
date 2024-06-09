'''
https://www.cbr.ru/FO_ZoomWS/FinOrg.asmx - Поиск по инн и огрн
https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx - Ежедневная информация
https://www.cbr.ru/secinfo/secinfo.asmx - Информация по рынку ценных бумаг
https://www.cbr.ru/CreditInfoWebServ/CreditOrgInfo.asmx - Справочник по кредитным организациям
'''

"""
Получение всей оперативной (ежедневной) информации
"""
all_data_info = {
    "url": "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=AllDataInfoXML",
    "body": """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <AllDataInfoXML xmlns="http://web.cbr.ru/" />
        </soap:Body>
        </soap:Envelope>""",
    "args": [],
    "page_type": "all_data_info"
}

"""
Получение курсов валют на определенную дату (ежедневные курсы валют)
Args: 
    On_date - Дата запроса для курсов, формат — System.DateTime 
Таблица содержит поля:
    Vname — Название валюты
    Vnom — Номинал
    Vcurs — Курс
    Vcode — ISO Цифровой код валюты
    VchCode — ISO Символьный код валюты
    VunitRate — Курс за 1 единицу валюты new

"""
get_curse_on_date = {
    "url": "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursOnDateXML",
    "body": """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetCursOnDateXML xmlns="http://web.cbr.ru/">
            <On_date></On_date>
            </GetCursOnDateXML>
        </soap:Body>
        </soap:Envelope>""",
    "args": ["On_date"],
    "page_type": "get_curse_on_date"
}


"""
Последняя дата публикации курсов валют как DateTime (ежедневные валюты)
"""
get_latest_date_time = {
    "url": "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetLatestDateTime",
    "body": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetLatestDateTime xmlns="http://web.cbr.ru/" />
  </soap:Body>
</soap:Envelope>""",
    "args": [],
    "page_type": "get_latest_date_time"
}

"""
Справочник по кодам валют, содержит полный перечень валют котируемых Банком России.
Аргументы:
Seld — формат -boolean 
    False — перечень ежедневных валют
    True — перечень ежемесячных валют
"""

enum_valutes = {
    "url": "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=EnumValutesXML",
    "body": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <EnumValutesXML xmlns="http://web.cbr.ru/">
      <Seld></Seld>
    </EnumValutesXML>
  </soap:Body>
</soap:Envelope>""",
    "args": ["Seld"],
    "page_type": "enum_valutes"
}

get_curs_dynamic = {
    "url": "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursDynamicXML",
    "body": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetCursDynamicXML xmlns="http://web.cbr.ru/">
      <FromDate></FromDate>
      <ToDate></ToDate>
      <ValutaCode></ValutaCode>
    </GetCursDynamicXML>
  </soap:Body>
</soap:Envelope>""",
    "args": ["FromDate", "ToDate", "ValutaCode"],
    "page_type": "get_curs_dynamic"
}
