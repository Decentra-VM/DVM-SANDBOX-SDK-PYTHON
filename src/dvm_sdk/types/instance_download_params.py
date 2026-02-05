# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceDownloadParams"]


class InstanceDownloadParams(TypedDict, total=False):
    path: Required[str]
    """File path in instance (e.g., /data/myfile.txt)"""
