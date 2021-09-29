# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AuthorizationManagementClientConfiguration
from .operations import Operations
from .operations import AccessReviewScheduleDefinitionsOperations
from .operations import AccessReviewInstancesOperations
from .operations import AccessReviewInstanceOperations
from .operations import AccessReviewInstanceDecisionsOperations
from .operations import AccessReviewDefaultSettingsOperations
from .operations import AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations
from .operations import AccessReviewInstancesAssignedForMyApprovalOperations
from .operations import AccessReviewInstanceMyDecisionsOperations
from .. import models


class AuthorizationManagementClient(object):
    """Access reviews service provides the workflow for running access reviews on different kind of resources.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.Operations
    :ivar access_review_schedule_definitions: AccessReviewScheduleDefinitionsOperations operations
    :vartype access_review_schedule_definitions: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewScheduleDefinitionsOperations
    :ivar access_review_instances: AccessReviewInstancesOperations operations
    :vartype access_review_instances: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewInstancesOperations
    :ivar access_review_instance: AccessReviewInstanceOperations operations
    :vartype access_review_instance: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewInstanceOperations
    :ivar access_review_instance_decisions: AccessReviewInstanceDecisionsOperations operations
    :vartype access_review_instance_decisions: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewInstanceDecisionsOperations
    :ivar access_review_default_settings: AccessReviewDefaultSettingsOperations operations
    :vartype access_review_default_settings: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewDefaultSettingsOperations
    :ivar access_review_schedule_definitions_assigned_for_my_approval: AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations operations
    :vartype access_review_schedule_definitions_assigned_for_my_approval: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations
    :ivar access_review_instances_assigned_for_my_approval: AccessReviewInstancesAssignedForMyApprovalOperations operations
    :vartype access_review_instances_assigned_for_my_approval: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewInstancesAssignedForMyApprovalOperations
    :ivar access_review_instance_my_decisions: AccessReviewInstanceMyDecisionsOperations operations
    :vartype access_review_instance_my_decisions: azure.mgmt.authorization.v2018_05_01_preview.aio.operations.AccessReviewInstanceMyDecisionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AuthorizationManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_schedule_definitions = AccessReviewScheduleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_instances = AccessReviewInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_instance = AccessReviewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_instance_decisions = AccessReviewInstanceDecisionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_default_settings = AccessReviewDefaultSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_schedule_definitions_assigned_for_my_approval = AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_instances_assigned_for_my_approval = AccessReviewInstancesAssignedForMyApprovalOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_instance_my_decisions = AccessReviewInstanceMyDecisionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AuthorizationManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)