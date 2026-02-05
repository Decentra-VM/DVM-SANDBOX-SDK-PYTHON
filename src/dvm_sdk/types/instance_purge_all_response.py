# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["InstancePurgeAllResponse", "Error"]


class Error(BaseModel):
    id: str
    """Instance ID that failed to delete"""

    error: str
    """Error message"""


class InstancePurgeAllResponse(BaseModel):
    deleted_count: float
    """Number of instances deleted"""

    deleted_ids: List[str]
    """Array of deleted instance IDs"""

    message: str
    """Success message"""

    errors: Optional[List[Error]] = None
    """Array of deletion errors, if any"""

    storage_deleted_count: Optional[float] = None
    """Number of storage volumes deleted"""
