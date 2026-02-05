# Instances

Types:

```python
from dvm_sdk.types import (
    Pagination,
    Instance,
    InstanceCreateResponse,
    InstanceListResponse,
    InstanceDeleteResponse,
    InstancePurgeAllResponse,
    InstanceExecuteResponse,
    InstanceUploadResponse,
)
```

Methods:

- <code title="post /v1/instances/launch">client.instances.<a href="./src/dvm_sdk/resources/instances.py">create</a>(\*\*<a href="src/dvm_sdk/types/instance_create_params.py">params</a>) -> <a href="./src/dvm_sdk/types/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="get /v1/instances/enumerate">client.instances.<a href="./src/dvm_sdk/resources/instances.py">list</a>(\*\*<a href="src/dvm_sdk/types/instance_list_params.py">params</a>) -> <a href="./src/dvm_sdk/types/instance_list_response.py">InstanceListResponse</a></code>
- <code title="delete /v1/instances/{id}/delete">client.instances.<a href="./src/dvm_sdk/resources/instances.py">delete</a>(id, \*\*<a href="src/dvm_sdk/types/instance_delete_params.py">params</a>) -> <a href="./src/dvm_sdk/types/instance_delete_response.py">InstanceDeleteResponse</a></code>
- <code title="delete /v1/instances/purge">client.instances.<a href="./src/dvm_sdk/resources/instances.py">purge_all</a>() -> <a href="./src/dvm_sdk/types/instance_purge_all_response.py">InstancePurgeAllResponse</a></code>
- <code title="get /v1/instances/{id}/download">client.instances.<a href="./src/dvm_sdk/resources/instances.py">download</a>(id, \*\*<a href="src/dvm_sdk/types/instance_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/instances/{id}/execute">client.instances.<a href="./src/dvm_sdk/resources/instances.py">execute</a>(id, \*\*<a href="src/dvm_sdk/types/instance_execute_params.py">params</a>) -> <a href="./src/dvm_sdk/types/instance_execute_response.py">InstanceExecuteResponse</a></code>
- <code title="post /v1/instances/{id}/upload">client.instances.<a href="./src/dvm_sdk/resources/instances.py">upload</a>(id, \*\*<a href="src/dvm_sdk/types/instance_upload_params.py">params</a>) -> <a href="./src/dvm_sdk/types/instance_upload_response.py">InstanceUploadResponse</a></code>
