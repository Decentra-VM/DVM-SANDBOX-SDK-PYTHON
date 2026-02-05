# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from dvm_sdk import DvmClient, AsyncDvmClient
from tests.utils import assert_matches_type
from dvm_sdk.types import (
    InstanceListResponse,
    InstanceCreateResponse,
    InstanceDeleteResponse,
    InstanceUploadResponse,
    InstanceExecuteResponse,
    InstancePurgeAllResponse,
)
from dvm_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: DvmClient) -> None:
        instance = client.instances.create()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DvmClient) -> None:
        instance = client.instances.create(
            env_vars={"foo": "string"},
            image="decentravm/dvm-default-instance",
            name="my-project",
            resources={
                "cpus": 1,
                "memory": 512,
                "storage": 10,
            },
            wait_for_ready=True,
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: DvmClient) -> None:
        instance = client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DvmClient) -> None:
        instance = client.instances.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: DvmClient) -> None:
        instance = client.instances.delete(
            id="id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: DvmClient) -> None:
        instance = client.instances.delete(
            id="id",
            create_snapshot=True,
            keep_storage=False,
            snapshot_name="final-backup",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_all(self, client: DvmClient) -> None:
        instance = client.instances.purge_all()
        assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge_all(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.purge_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge_all(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.purge_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: DvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        instance = client.instances.download(
            id="id",
            path="path",
        )
        assert instance.is_closed
        assert instance.json() == {"foo": "bar"}
        assert cast(Any, instance.is_closed) is True
        assert isinstance(instance, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: DvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        instance = client.instances.with_raw_response.download(
            id="id",
            path="path",
        )

        assert instance.is_closed is True
        assert instance.http_request.headers.get("X-Stainless-Lang") == "python"
        assert instance.json() == {"foo": "bar"}
        assert isinstance(instance, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: DvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.instances.with_streaming_response.download(
            id="id",
            path="path",
        ) as instance:
            assert not instance.is_closed
            assert instance.http_request.headers.get("X-Stainless-Lang") == "python"

            assert instance.json() == {"foo": "bar"}
            assert cast(Any, instance.is_closed) is True
            assert isinstance(instance, StreamedBinaryAPIResponse)

        assert cast(Any, instance.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: DvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.download(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute(self, client: DvmClient) -> None:
        instance = client.instances.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: DvmClient) -> None:
        instance = client.instances.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
            env={"foo": "string"},
            api_timeout=5,
            working_dir="working_dir",
        )
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: DvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.execute(
                id="",
                command="python -c \"print('Hello, World!')\"",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: DvmClient) -> None:
        instance = client.instances.upload(
            id="id",
            path="path",
        )
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: DvmClient) -> None:
        instance = client.instances.upload(
            id="id",
            path="path",
            file={},
        )
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: DvmClient) -> None:
        response = client.instances.with_raw_response.upload(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: DvmClient) -> None:
        with client.instances.with_streaming_response.upload(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceUploadResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: DvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.instances.with_raw_response.upload(
                id="",
                path="path",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.create()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.create(
            env_vars={"foo": "string"},
            image="decentravm/dvm-default-instance",
            name="my-project",
            resources={
                "cpus": 1,
                "memory": 512,
                "storage": 10,
            },
            wait_for_ready=True,
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.delete(
            id="id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.delete(
            id="id",
            create_snapshot=True,
            keep_storage=False,
            snapshot_name="final-backup",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_all(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.purge_all()
        assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge_all(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.purge_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge_all(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.purge_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstancePurgeAllResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncDvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        instance = await async_client.instances.download(
            id="id",
            path="path",
        )
        assert instance.is_closed
        assert await instance.json() == {"foo": "bar"}
        assert cast(Any, instance.is_closed) is True
        assert isinstance(instance, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncDvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        instance = await async_client.instances.with_raw_response.download(
            id="id",
            path="path",
        )

        assert instance.is_closed is True
        assert instance.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await instance.json() == {"foo": "bar"}
        assert isinstance(instance, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncDvmClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/instances/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.instances.with_streaming_response.download(
            id="id",
            path="path",
        ) as instance:
            assert not instance.is_closed
            assert instance.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await instance.json() == {"foo": "bar"}
            assert cast(Any, instance.is_closed) is True
            assert isinstance(instance, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, instance.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncDvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.download(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
            env={"foo": "string"},
            api_timeout=5,
            working_dir="working_dir",
        )
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceExecuteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncDvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.execute(
                id="",
                command="python -c \"print('Hello, World!')\"",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.upload(
            id="id",
            path="path",
        )
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncDvmClient) -> None:
        instance = await async_client.instances.upload(
            id="id",
            path="path",
            file={},
        )
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncDvmClient) -> None:
        response = await async_client.instances.with_raw_response.upload(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceUploadResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncDvmClient) -> None:
        async with async_client.instances.with_streaming_response.upload(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceUploadResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncDvmClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.instances.with_raw_response.upload(
                id="",
                path="path",
            )
