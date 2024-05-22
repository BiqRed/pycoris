from uuid import UUID

from typing import Dict


class BaseORM:
    """Base adapter for interacting with the database through the ORM system."""

    async def get_admin_by_uuid(self, uuid: UUID) -> Dict[str, str]:
        """Get an admin by UUID."""
        raise NotImplementedError


async def init_db(orm: BaseORM) -> None:
    """Initialize the database."""
    raise NotImplementedError
