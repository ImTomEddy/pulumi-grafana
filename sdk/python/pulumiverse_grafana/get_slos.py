# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetSlosResult',
    'AwaitableGetSlosResult',
    'get_slos',
    'get_slos_output',
]

@pulumi.output_type
class GetSlosResult:
    """
    A collection of values returned by getSlos.
    """
    def __init__(__self__, id=None, slos=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if slos and not isinstance(slos, list):
            raise TypeError("Expected argument 'slos' to be a list")
        pulumi.set(__self__, "slos", slos)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def slos(self) -> Sequence['outputs.GetSlosSloResult']:
        return pulumi.get(self, "slos")


class AwaitableGetSlosResult(GetSlosResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSlosResult(
            id=self.id,
            slos=self.slos)


def get_slos(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSlosResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getSlos:getSlos', __args__, opts=opts, typ=GetSlosResult).value

    return AwaitableGetSlosResult(
        id=pulumi.get(__ret__, 'id'),
        slos=pulumi.get(__ret__, 'slos'))


@_utilities.lift_output_func(get_slos)
def get_slos_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSlosResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
