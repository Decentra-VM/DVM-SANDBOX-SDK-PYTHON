# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceUploadParams"]


class InstanceUploadParams(TypedDict, total=False):
    path: Required[str]
    """Destination path in instance (e.g., /data/myfile.txt)"""

    file: object
    """File to upload (binary data)"""
