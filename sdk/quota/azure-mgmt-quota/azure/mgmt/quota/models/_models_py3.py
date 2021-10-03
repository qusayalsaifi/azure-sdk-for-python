# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._azure_quota_extension_api_enums import *


class CommonResourceProperties(msrest.serialization.Model):
    """Resource properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type. Example: "Microsoft.Quota/quotas".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommonResourceProperties, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class CreateGenericQuotaRequestParameters(msrest.serialization.Model):
    """Quota change requests information.

    :param value: Quota change requests.
    :type value: list[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CurrentQuotaLimitBase]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CurrentQuotaLimitBase"]] = None,
        **kwargs
    ):
        super(CreateGenericQuotaRequestParameters, self).__init__(**kwargs)
        self.value = value


class CurrentQuotaLimitBase(msrest.serialization.Model):
    """Quota limit.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    :param properties: Quota properties for the specified resource, based on the API called, Quotas
     or Usages.
    :type properties: ~azure.mgmt.quota.models.QuotaProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'QuotaProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["QuotaProperties"] = None,
        **kwargs
    ):
        super(CurrentQuotaLimitBase, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = properties


class CurrentUsagesBase(msrest.serialization.Model):
    """Resource usage.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    :param properties: Usage properties for the specified resource.
    :type properties: ~azure.mgmt.quota.models.UsagesProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'UsagesProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["UsagesProperties"] = None,
        **kwargs
    ):
        super(CurrentUsagesBase, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = properties


class ExceptionResponse(msrest.serialization.Model):
    """Error.

    :param error: API error details.
    :type error: ~azure.mgmt.quota.models.ServiceError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ServiceError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ServiceError"] = None,
        **kwargs
    ):
        super(ExceptionResponse, self).__init__(**kwargs)
        self.error = error


class LimitJsonObject(msrest.serialization.Model):
    """LimitJson abstract class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: LimitValue.

    All required parameters must be populated in order to send to Azure.

    :param limit_object_type: Required. The limit object type.Constant filled by server.  Possible
     values include: "LimitValue".
    :type limit_object_type: str or ~azure.mgmt.quota.models.LimitType
    """

    _validation = {
        'limit_object_type': {'required': True},
    }

    _attribute_map = {
        'limit_object_type': {'key': 'limitObjectType', 'type': 'str'},
    }

    _subtype_map = {
        'limit_object_type': {'LimitValue': 'LimitValue'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LimitJsonObject, self).__init__(**kwargs)
        self.limit_object_type = None  # type: Optional[str]


class LimitObject(msrest.serialization.Model):
    """The resource quota limit value.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The quota/limit value.
    :type value: int
    :param limit_object_type: The limit object type. Possible values include: "LimitValue".
    :type limit_object_type: str or ~azure.mgmt.quota.models.LimitType
    :param limit_type: The quota or usages limit types. Possible values include: "Independent",
     "Shared".
    :type limit_type: str or ~azure.mgmt.quota.models.QuotaLimitTypes
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
        'limit_object_type': {'key': 'limitObjectType', 'type': 'str'},
        'limit_type': {'key': 'limitType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: int,
        limit_object_type: Optional[Union[str, "LimitType"]] = None,
        limit_type: Optional[Union[str, "QuotaLimitTypes"]] = None,
        **kwargs
    ):
        super(LimitObject, self).__init__(**kwargs)
        self.value = value
        self.limit_object_type = limit_object_type
        self.limit_type = limit_type


class LimitValue(LimitJsonObject, LimitObject):
    """The resource quota limit.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The quota/limit value.
    :type value: int
    :param limit_type: The quota or usages limit types. Possible values include: "Independent",
     "Shared".
    :type limit_type: str or ~azure.mgmt.quota.models.QuotaLimitTypes
    :param limit_object_type: Required. The limit object type.Constant filled by server.  Possible
     values include: "LimitValue".
    :type limit_object_type: str or ~azure.mgmt.quota.models.LimitType
    """

    _validation = {
        'value': {'required': True},
        'limit_object_type': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
        'limit_type': {'key': 'limitType', 'type': 'str'},
        'limit_object_type': {'key': 'limitObjectType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: int,
        limit_type: Optional[Union[str, "QuotaLimitTypes"]] = None,
        **kwargs
    ):
        super(LimitValue, self).__init__(value=value, limit_type=limit_type, **kwargs)
        self.value = value
        self.limit_type = limit_type
        self.limit_object_type = 'LimitValue'  # type: str
        self.limit_object_type = 'LimitValue'  # type: str


class OperationDisplay(msrest.serialization.Model):
    """OperationDisplay.

    :param provider: Provider name.
    :type provider: str
    :param resource: Resource name.
    :type resource: str
    :param operation: Operation name.
    :type operation: str
    :param description: Operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(msrest.serialization.Model):
    """OperationList.

    :param value:
    :type value: list[~azure.mgmt.quota.models.OperationResponse]
    :param next_link: URL to get the next page of items.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationResponse]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["OperationResponse"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class OperationResponse(msrest.serialization.Model):
    """OperationResponse.

    :param name:
    :type name: str
    :param display:
    :type display: ~azure.mgmt.quota.models.OperationDisplay
    :param origin:
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        origin: Optional[str] = None,
        **kwargs
    ):
        super(OperationResponse, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class QuotaLimits(msrest.serialization.Model):
    """Quota limits.

    :param value: List of quota limits.
    :type value: list[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this string is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CurrentQuotaLimitBase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CurrentQuotaLimitBase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(QuotaLimits, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class QuotaLimitsResponse(msrest.serialization.Model):
    """Quota limits request response.

    :param value: List of quota limits with the quota request status.
    :type value: list[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CurrentQuotaLimitBase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CurrentQuotaLimitBase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(QuotaLimitsResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class QuotaProperties(msrest.serialization.Model):
    """Quota properties for the specified resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param limit: Resource quota limit properties.
    :type limit: ~azure.mgmt.quota.models.LimitJsonObject
    :ivar unit: The quota units, such as Count and Bytes. When requesting quota, use the **unit**
     value returned in the GET response in the request body of your PUT operation.
    :vartype unit: str
    :param name: Resource name provided by the resource provider. Use this property name when
     requesting quota.
    :type name: ~azure.mgmt.quota.models.ResourceName
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param properties: Additional properties for the specific resource provider.
    :type properties: any
    """

    _validation = {
        'unit': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'LimitJsonObject'},
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'ResourceName'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'isQuotaApplicable', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["LimitJsonObject"] = None,
        name: Optional["ResourceName"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[Any] = None,
        **kwargs
    ):
        super(QuotaProperties, self).__init__(**kwargs)
        self.limit = limit
        self.unit = None
        self.name = name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.properties = properties


class QuotaRequestDetails(msrest.serialization.Model):
    """List of quota requests with details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: Quota request name.
    :vartype name: str
    :ivar type: Resource type. "Microsoft.Quota/quotas".
    :vartype type: str
    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure.mgmt.quota.models.QuotaRequestState
    :ivar message: User-friendly status message.
    :vartype message: str
    :param error: Error details of the quota request.
    :type error: ~azure.mgmt.quota.models.ServiceErrorDetail
    :ivar request_submit_time: The quota request submission time. The date conforms to the
     following format specified by the ISO 8601 standard: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param value: Quota request details.
    :type value: list[~azure.mgmt.quota.models.SubRequest]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'error': {'key': 'properties.error', 'type': 'ServiceErrorDetail'},
        'request_submit_time': {'key': 'properties.requestSubmitTime', 'type': 'iso-8601'},
        'value': {'key': 'properties.value', 'type': '[SubRequest]'},
    }

    def __init__(
        self,
        *,
        error: Optional["ServiceErrorDetail"] = None,
        value: Optional[List["SubRequest"]] = None,
        **kwargs
    ):
        super(QuotaRequestDetails, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.error = error
        self.request_submit_time = None
        self.value = value


class QuotaRequestDetailsList(msrest.serialization.Model):
    """Quota request information.

    :param value: Quota request details.
    :type value: list[~azure.mgmt.quota.models.QuotaRequestDetails]
    :param next_link: The URI for fetching the next page of quota limits. When there are no more
     pages, this string is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[QuotaRequestDetails]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["QuotaRequestDetails"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(QuotaRequestDetailsList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class QuotaRequestOneResourceSubmitResponse(msrest.serialization.Model):
    """Quota request response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: The name of the quota request.
    :vartype name: str
    :ivar type: Resource type. "Microsoft.Quota/ServiceLimitRequests".
    :vartype type: str
    :ivar provisioning_state: Quota request status. Possible values include: "Accepted", "Invalid",
     "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure.mgmt.quota.models.QuotaRequestState
    :ivar message: User-friendly status message.
    :vartype message: str
    :ivar request_submit_time: Quota request submission time. The date conforms to the following
     ISO 8601 standard format: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param limit: Resource quota limit properties.
    :type limit: ~azure.mgmt.quota.models.LimitObject
    :ivar current_value: Usage information for the current resource.
    :vartype current_value: int
    :param unit: The quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :param name_properties_name: Resource name provided by the resource provider. Use this property
     name when requesting quota.
    :type name_properties_name: ~azure.mgmt.quota.models.ResourceName
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param error: Error details of the quota request.
    :type error: ~azure.mgmt.quota.models.ServiceErrorDetail
    :param properties: Additional properties for the specific resource provider.
    :type properties: any
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
        'current_value': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'request_submit_time': {'key': 'properties.requestSubmitTime', 'type': 'iso-8601'},
        'limit': {'key': 'properties.limit', 'type': 'LimitObject'},
        'current_value': {'key': 'properties.currentValue', 'type': 'int'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'name_properties_name': {'key': 'properties.name', 'type': 'ResourceName'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'quota_period': {'key': 'properties.quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'properties.isQuotaApplicable', 'type': 'bool'},
        'error': {'key': 'properties.error', 'type': 'ServiceErrorDetail'},
        'properties': {'key': 'properties.properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["LimitObject"] = None,
        unit: Optional[str] = None,
        name_properties_name: Optional["ResourceName"] = None,
        resource_type: Optional[str] = None,
        error: Optional["ServiceErrorDetail"] = None,
        properties: Optional[Any] = None,
        **kwargs
    ):
        super(QuotaRequestOneResourceSubmitResponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.request_submit_time = None
        self.limit = limit
        self.current_value = None
        self.unit = unit
        self.name_properties_name = name_properties_name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.error = error
        self.properties = properties


class QuotaRequestProperties(msrest.serialization.Model):
    """Quota request properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure.mgmt.quota.models.QuotaRequestState
    :ivar message: User-friendly status message.
    :vartype message: str
    :param error: Error details of the quota request.
    :type error: ~azure.mgmt.quota.models.ServiceErrorDetail
    :ivar request_submit_time: The quota request submission time. The date conforms to the
     following format specified by the ISO 8601 standard: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param value: Quota request details.
    :type value: list[~azure.mgmt.quota.models.SubRequest]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'error': {'key': 'error', 'type': 'ServiceErrorDetail'},
        'request_submit_time': {'key': 'requestSubmitTime', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': '[SubRequest]'},
    }

    def __init__(
        self,
        *,
        error: Optional["ServiceErrorDetail"] = None,
        value: Optional[List["SubRequest"]] = None,
        **kwargs
    ):
        super(QuotaRequestProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.message = None
        self.error = error
        self.request_submit_time = None
        self.value = value


class QuotaRequestSubmitResponse(msrest.serialization.Model):
    """Quota request response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: Quota request name.
    :vartype name: str
    :param properties: Quota request details.
    :type properties: ~azure.mgmt.quota.models.QuotaRequestProperties
    :ivar type: Resource type. "Microsoft.Quota/quotas".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'QuotaRequestProperties'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        properties: Optional["QuotaRequestProperties"] = None,
        **kwargs
    ):
        super(QuotaRequestSubmitResponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.properties = properties
        self.type = None


class QuotaRequestSubmitResponse202(msrest.serialization.Model):
    """The quota request response with the quota request ID.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The quota request ID. To check the request status, use the **id** value in a `Quota
     Request Status
     <https://docs.microsoft.com/en-us/rest/api/reserved-vm-instances/quotarequeststatus/get>`_ GET
     operation.
    :vartype id: str
    :ivar name: Operation ID.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar provisioning_state: Quota request status. Possible values include: "Accepted", "Invalid",
     "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure.mgmt.quota.models.QuotaRequestState
    :ivar message: User-friendly message.
    :vartype message: str
    :param limit: Resource quota limit properties.
    :type limit: ~azure.mgmt.quota.models.LimitObject
    :param unit: The quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :param name_properties_name: Resource name provided by the resource provider. Use this property
     name when requesting quota.
    :type name_properties_name: ~azure.mgmt.quota.models.ResourceName
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :param properties: Additional properties for the specific resource provider.
    :type properties: any
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'quota_period': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'limit': {'key': 'properties.limit', 'type': 'LimitObject'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'name_properties_name': {'key': 'properties.name', 'type': 'ResourceName'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'quota_period': {'key': 'properties.quotaPeriod', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["LimitObject"] = None,
        unit: Optional[str] = None,
        name_properties_name: Optional["ResourceName"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[Any] = None,
        **kwargs
    ):
        super(QuotaRequestSubmitResponse202, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.limit = limit
        self.unit = unit
        self.name_properties_name = name_properties_name
        self.resource_type = resource_type
        self.quota_period = None
        self.properties = properties


class ResourceName(msrest.serialization.Model):
    """Name of the resource provided by the resource Provider. When requesting quota, use this property name.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: Resource name.
    :type value: str
    :ivar localized_value: Resource display name.
    :vartype localized_value: str
    """

    _validation = {
        'localized_value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[str] = None,
        **kwargs
    ):
        super(ResourceName, self).__init__(**kwargs)
        self.value = value
        self.localized_value = None


class ServiceError(msrest.serialization.Model):
    """API error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param code: Error code.
    :type code: str
    :param message: Error message.
    :type message: str
    :ivar details: List of error details.
    :vartype details: list[~azure.mgmt.quota.models.ServiceErrorDetail]
    """

    _validation = {
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ServiceErrorDetail]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ServiceError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = None


class ServiceErrorDetail(msrest.serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ServiceErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None


class SubRequest(msrest.serialization.Model):
    """Request property.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: Resource name.
    :type name: ~azure.mgmt.quota.models.ResourceName
    :ivar resource_type: Resource type for which the quota properties were requested.
    :vartype resource_type: str
    :param unit: Quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure.mgmt.quota.models.QuotaRequestState
    :ivar message: User-friendly status message.
    :vartype message: str
    :ivar sub_request_id: Quota request ID.
    :vartype sub_request_id: str
    :param limit: Resource quota limit properties.
    :type limit: ~azure.mgmt.quota.models.LimitJsonObject
    """

    _validation = {
        'resource_type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'sub_request_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'ResourceName'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'sub_request_id': {'key': 'subRequestId', 'type': 'str'},
        'limit': {'key': 'limit', 'type': 'LimitJsonObject'},
    }

    def __init__(
        self,
        *,
        name: Optional["ResourceName"] = None,
        unit: Optional[str] = None,
        limit: Optional["LimitJsonObject"] = None,
        **kwargs
    ):
        super(SubRequest, self).__init__(**kwargs)
        self.name = name
        self.resource_type = None
        self.unit = unit
        self.provisioning_state = None
        self.message = None
        self.sub_request_id = None
        self.limit = limit


class UsagesLimits(msrest.serialization.Model):
    """Quota limits.

    :param value: List of quota limits.
    :type value: list[~azure.mgmt.quota.models.CurrentUsagesBase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CurrentUsagesBase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CurrentUsagesBase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(UsagesLimits, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class UsagesObject(msrest.serialization.Model):
    """The resource usages value.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The usages value.
    :type value: int
    :param usages_type: The quota or usages limit types. Possible values include: "Individual",
     "Combined".
    :type usages_type: str or ~azure.mgmt.quota.models.UsagesTypes
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
        'usages_type': {'key': 'usagesType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: int,
        usages_type: Optional[Union[str, "UsagesTypes"]] = None,
        **kwargs
    ):
        super(UsagesObject, self).__init__(**kwargs)
        self.value = value
        self.usages_type = usages_type


class UsagesProperties(msrest.serialization.Model):
    """Usage properties for the specified resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param usages: The quota limit properties for this resource.
    :type usages: ~azure.mgmt.quota.models.UsagesObject
    :ivar unit: The units for the quota usage, such as Count and Bytes. When requesting quota, use
     the **unit** value returned in the GET response in the request body of your PUT operation.
    :vartype unit: str
    :param name: Resource name provided by the resource provider. Use this property name when
     requesting quota.
    :type name: ~azure.mgmt.quota.models.ResourceName
    :param resource_type: The name of the resource type.
    :type resource_type: str
    :ivar quota_period: The time period for the summary of the quota usage values. For example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because it is not relevant for all resources such as compute.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param properties: Additional properties for the specific resource provider.
    :type properties: any
    """

    _validation = {
        'unit': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'usages': {'key': 'usages', 'type': 'UsagesObject'},
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'ResourceName'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'isQuotaApplicable', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        usages: Optional["UsagesObject"] = None,
        name: Optional["ResourceName"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[Any] = None,
        **kwargs
    ):
        super(UsagesProperties, self).__init__(**kwargs)
        self.usages = usages
        self.unit = None
        self.name = name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.properties = properties