"""
This type stub file was generated by pyright.
"""

from CxAdmin.api.http.httpClientModel import HTTPClientModel
from typing import Any

class HTTPClient(HTTPClientModel):
    __basePath: str
    __token: str
    __headers: dict[str, Any]
    def __init__(self, basePath: str, token: str) -> None:
        ...
    
    def get(self, path: str) -> str:
        ...
    
    def post(self, path: str, data: Any) -> dict[str, Any]:
        ...
    
    @staticmethod
    def getToken(basePath: str, apiKey: str, apiSecret: str, tenantID: str) -> str:
        ...
    


