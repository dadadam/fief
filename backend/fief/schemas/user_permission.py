from typing import Optional

from pydantic import UUID4, BaseModel

from fief.schemas.generics import CreatedUpdatedAt, UUIDSchema
from fief.schemas.permission import PermissionEmbedded
from fief.schemas.role import RoleEmbedded


class UserPermissionCreate(BaseModel):
    id: UUID4


class BaseUserPermission(UUIDSchema, CreatedUpdatedAt):
    user_id: UUID4
    permission_id: UUID4
    from_role_id: Optional[UUID4]


class UserPermission(BaseUserPermission):
    permission: PermissionEmbedded
    from_role: Optional[RoleEmbedded]
