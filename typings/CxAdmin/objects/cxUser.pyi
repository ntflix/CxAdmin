"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional
from datetime import datetime
from CxAdmin.objects.platformStatus import PlatformStatus
from CxAdmin.objects.skill import Skill

class CxUser(dict[str, Any]):
    activeExtension: dict[str, str]
    additionalRoleIds: Optional[str]
    aliasPlatformUserId: Optional[str]
    clientLogLevel: Optional[str]
    created: datetime
    createdBy: str
    defaultTenant: Optional[str]
    email: str
    extensions: list[dict[str, Any]]
    externalId: Optional[str]
    firstName: str
    groups: list[dict[str, str]]
    id: str
    lastName: str
    personalTelephone: Optional[str]
    tenantStatus: PlatformStatus
    roleName: str
    skills: list[Skill]
    state: str
    platformStatus: PlatformStatus
    updated: datetime
    updatedBy: str
    def __init__(self, activeExtension: dict[str, str], additionalRoleIds: Optional[str], aliasPlatformUserId: Optional[str], clientLogLevel: Optional[str], created: datetime, createdBy: str, defaultTenant: Optional[str], email: str, extensions: list[dict[str, Any]], externalId: Optional[str], firstName: str, groups: list[dict[str, str]], id: str, lastName: str, personalTelephone: Optional[str], tenantStatus: PlatformStatus, roleName: str, skills: list[Skill], state: str, platformStatus: PlatformStatus, updated: datetime, updatedBy: str) -> None:
        ...
    
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxUser:
        ...
    


