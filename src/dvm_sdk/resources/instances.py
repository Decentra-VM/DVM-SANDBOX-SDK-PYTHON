# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    instance_list_params,
    instance_create_params,
    instance_delete_params,
    instance_upload_params,
    instance_execute_params,
    instance_download_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.instance_list_response import InstanceListResponse
from ..types.instance_create_response import InstanceCreateResponse
from ..types.instance_delete_response import InstanceDeleteResponse
from ..types.instance_upload_response import InstanceUploadResponse
from ..types.instance_execute_response import InstanceExecuteResponse
from ..types.instance_purge_all_response import InstancePurgeAllResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/decentravm/dvm-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/decentravm/dvm-sdk-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        env_vars: Dict[str, str] | Omit = omit,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: instance_create_params.Resources | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """
        Args:
          env_vars: Environment variables

          image: Docker image name (e.g., decentravm/dvm-default-instance)

          name: Custom instance name (auto-generated as instance-{user_id}-{timestamp} if not
              provided)

          wait_for_ready: Wait for instance to be ready before returning

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/instances/launch",
            body=maybe_transform(
                {
                    "env_vars": env_vars,
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "wait_for_ready": wait_for_ready,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceCreateResponse,
        )

    def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        Args:
          page: Page number

          page_size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/instances/enumerate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        create_snapshot: bool | Omit = omit,
        keep_storage: bool | Omit = omit,
        snapshot_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Args:
          id: Instance ID

          create_snapshot: Create snapshot before deleting storage

          keep_storage: Keep storage after deletion (default: false - storage deleted)

          snapshot_name: Custom name for the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/instances/{id}/delete",
            body=maybe_transform(
                {
                    "create_snapshot": create_snapshot,
                    "keep_storage": keep_storage,
                    "snapshot_name": snapshot_name,
                },
                instance_delete_params.InstanceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )

    def purge_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstancePurgeAllResponse:
        return self._delete(
            "/v1/instances/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstancePurgeAllResponse,
        )

    def download(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          id: Instance ID

          path: File path in instance (e.g., /data/myfile.txt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/v1/instances/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, instance_download_params.InstanceDownloadParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def execute(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        api_timeout: int | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceExecuteResponse:
        """
        Args:
          id: Instance ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables

          api_timeout: Execution timeout in seconds

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/instances/{id}/execute",
            body=maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                instance_execute_params.InstanceExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceExecuteResponse,
        )

    def upload(
        self,
        id: str,
        *,
        path: str,
        file: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUploadResponse:
        """
        Args:
          id: Instance ID

          path: Destination path in instance (e.g., /data/myfile.txt)

          file: File to upload (binary data)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/instances/{id}/upload",
            body=maybe_transform(
                {
                    "path": path,
                    "file": file,
                },
                instance_upload_params.InstanceUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceUploadResponse,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/decentravm/dvm-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/decentravm/dvm-sdk-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        env_vars: Dict[str, str] | Omit = omit,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: instance_create_params.Resources | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """
        Args:
          env_vars: Environment variables

          image: Docker image name (e.g., decentravm/dvm-default-instance)

          name: Custom instance name (auto-generated as instance-{user_id}-{timestamp} if not
              provided)

          wait_for_ready: Wait for instance to be ready before returning

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/instances/launch",
            body=await async_maybe_transform(
                {
                    "env_vars": env_vars,
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "wait_for_ready": wait_for_ready,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceCreateResponse,
        )

    async def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        Args:
          page: Page number

          page_size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/instances/enumerate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        create_snapshot: bool | Omit = omit,
        keep_storage: bool | Omit = omit,
        snapshot_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Args:
          id: Instance ID

          create_snapshot: Create snapshot before deleting storage

          keep_storage: Keep storage after deletion (default: false - storage deleted)

          snapshot_name: Custom name for the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/instances/{id}/delete",
            body=await async_maybe_transform(
                {
                    "create_snapshot": create_snapshot,
                    "keep_storage": keep_storage,
                    "snapshot_name": snapshot_name,
                },
                instance_delete_params.InstanceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )

    async def purge_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstancePurgeAllResponse:
        return await self._delete(
            "/v1/instances/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstancePurgeAllResponse,
        )

    async def download(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          id: Instance ID

          path: File path in instance (e.g., /data/myfile.txt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/v1/instances/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, instance_download_params.InstanceDownloadParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def execute(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        api_timeout: int | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceExecuteResponse:
        """
        Args:
          id: Instance ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables

          api_timeout: Execution timeout in seconds

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/instances/{id}/execute",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                instance_execute_params.InstanceExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceExecuteResponse,
        )

    async def upload(
        self,
        id: str,
        *,
        path: str,
        file: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUploadResponse:
        """
        Args:
          id: Instance ID

          path: Destination path in instance (e.g., /data/myfile.txt)

          file: File to upload (binary data)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/instances/{id}/upload",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "file": file,
                },
                instance_upload_params.InstanceUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceUploadResponse,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_raw_response_wrapper(
            instances.create,
        )
        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.delete = to_raw_response_wrapper(
            instances.delete,
        )
        self.purge_all = to_raw_response_wrapper(
            instances.purge_all,
        )
        self.download = to_custom_raw_response_wrapper(
            instances.download,
            BinaryAPIResponse,
        )
        self.execute = to_raw_response_wrapper(
            instances.execute,
        )
        self.upload = to_raw_response_wrapper(
            instances.upload,
        )


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_raw_response_wrapper(
            instances.create,
        )
        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instances.delete,
        )
        self.purge_all = async_to_raw_response_wrapper(
            instances.purge_all,
        )
        self.download = async_to_custom_raw_response_wrapper(
            instances.download,
            AsyncBinaryAPIResponse,
        )
        self.execute = async_to_raw_response_wrapper(
            instances.execute,
        )
        self.upload = async_to_raw_response_wrapper(
            instances.upload,
        )


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_streamed_response_wrapper(
            instances.create,
        )
        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = to_streamed_response_wrapper(
            instances.delete,
        )
        self.purge_all = to_streamed_response_wrapper(
            instances.purge_all,
        )
        self.download = to_custom_streamed_response_wrapper(
            instances.download,
            StreamedBinaryAPIResponse,
        )
        self.execute = to_streamed_response_wrapper(
            instances.execute,
        )
        self.upload = to_streamed_response_wrapper(
            instances.upload,
        )


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_streamed_response_wrapper(
            instances.create,
        )
        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instances.delete,
        )
        self.purge_all = async_to_streamed_response_wrapper(
            instances.purge_all,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            instances.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.execute = async_to_streamed_response_wrapper(
            instances.execute,
        )
        self.upload = async_to_streamed_response_wrapper(
            instances.upload,
        )
