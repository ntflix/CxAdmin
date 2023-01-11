"""
This type stub file was generated by pyright.
"""

from CxAdmin.api.cxLists import CxLists
from CxAdmin.api.cxQueues import CxQueues
from CxAdmin.api.cxStatistics import CxStatistics
from CxAdmin.api.cxEnvironment import CxEnvironment
from CxAdmin.api.cxFlows import CxFlows
from CxAdmin.api.cxUsers import CxUsers
from CxAdmin.api.http.httpClientModel import HTTPClientModel

class Cx:
    __BASE_URL: str
    __API_KEY: str
    __API_SECRET: str
    __TENANT_ID: str
    __TENANT_URL: str
    __httpClient: HTTPClientModel
    lists: CxLists
    queues: CxQueues
    statistics: CxStatistics
    environment: CxEnvironment
    flows: CxFlows
    users: CxUsers

    def __init__(
        self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str
    ) -> None: ...
    @staticmethod
    def fromConfigFile(configFilePath: str) -> Cx: ...
