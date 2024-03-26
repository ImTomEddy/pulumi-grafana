# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetOncallEscalationChainResult',
    'AwaitableGetOncallEscalationChainResult',
    'get_oncall_escalation_chain',
    'get_oncall_escalation_chain_output',
]

@pulumi.output_type
class GetOncallEscalationChainResult:
    """
    A collection of values returned by getOncallEscalationChain.
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
        The escalation chain name.
        """
        return pulumi.get(self, "name")


class AwaitableGetOncallEscalationChainResult(GetOncallEscalationChainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOncallEscalationChainResult(
            id=self.id,
            name=self.name)


def get_oncall_escalation_chain(name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOncallEscalationChainResult:
    """
    * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/escalation_chains/)

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_grafana as grafana

    default = grafana.get_oncall_escalation_chain(name="default")
    ```
    <!--End PulumiCodeChooser -->


    :param str name: The escalation chain name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getOncallEscalationChain:getOncallEscalationChain', __args__, opts=opts, typ=GetOncallEscalationChainResult).value

    return AwaitableGetOncallEscalationChainResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_oncall_escalation_chain)
def get_oncall_escalation_chain_output(name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOncallEscalationChainResult]:
    """
    * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/escalation_chains/)

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_grafana as grafana

    default = grafana.get_oncall_escalation_chain(name="default")
    ```
    <!--End PulumiCodeChooser -->


    :param str name: The escalation chain name.
    """
    ...
