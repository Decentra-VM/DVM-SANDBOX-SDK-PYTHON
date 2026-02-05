# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Instance"]


class Instance(BaseModel):
    id: str
    """Instance ID"""

    cpu: float
    """CPU count"""

    created_at: str
    """Creation timestamp"""

    disk_size: float
    """Disk size in GB"""

    memory: float
    """Memory size in MB"""

    name: str
    """Instance name"""

    status: str
    """Instance status"""
