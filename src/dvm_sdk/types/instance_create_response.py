# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instance import Instance

__all__ = ["InstanceCreateResponse"]


class InstanceCreateResponse(Instance):
    id: str  # type: ignore
    """Instance ID"""

    cpu: float  # type: ignore
    """CPU count (API units, minimum 1)"""

    created_at: str  # type: ignore
    """Creation timestamp"""

    memory: float  # type: ignore
    """Memory size in MiB"""

    name: str  # type: ignore
    """Instance name"""

    status: str  # type: ignore
    """Instance status"""

    storage: float
    """Storage size in GB"""
