# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .instance import Instance
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["InstanceListResponse"]


class InstanceListResponse(BaseModel):
    data: List[Instance]
    """Array of instances"""

    pagination: Pagination
    """Pagination metadata"""
