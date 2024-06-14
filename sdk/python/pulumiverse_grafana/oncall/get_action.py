# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetActionResult',
    'AwaitableGetActionResult',
    'get_action',
    'get_action_output',
]

@pulumi.output_type
class GetActionResult:
    """
    A collection of values returned by getAction.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The action name.
        """
        return pulumi.get(self, "name")


class AwaitableGetActionResult(GetActionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActionResult(
            id=self.id,
            name=self.name)


def get_action(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActionResult:
    """
    **Note:** This data source is going to be deprecated, please use outgoing webhook data source instead.
    * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/outgoing_webhooks/)

    !> Deprecated: Use the `onCall.OutgoingWebhook` data source instead.


    :param str name: The action name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:onCall/getAction:getAction', __args__, opts=opts, typ=GetActionResult).value

    return AwaitableGetActionResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_action)
def get_action_output(name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActionResult]:
    """
    **Note:** This data source is going to be deprecated, please use outgoing webhook data source instead.
    * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/outgoing_webhooks/)

    !> Deprecated: Use the `onCall.OutgoingWebhook` data source instead.


    :param str name: The action name.
    """
    ...
