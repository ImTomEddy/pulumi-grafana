# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ApiKeyArgs', 'ApiKey']

@pulumi.input_type
class ApiKeyArgs:
    def __init__(__self__, *,
                 role: pulumi.Input[str],
                 cloud_stack_slug: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ApiKey resource.
        :param pulumi.Input[str] cloud_stack_slug: Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        pulumi.set(__self__, "role", role)
        if cloud_stack_slug is not None:
            warnings.warn("""Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""", DeprecationWarning)
            pulumi.log.warn("""cloud_stack_slug is deprecated: Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""")
        if cloud_stack_slug is not None:
            pulumi.set(__self__, "cloud_stack_slug", cloud_stack_slug)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if seconds_to_live is not None:
            pulumi.set(__self__, "seconds_to_live", seconds_to_live)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="cloudStackSlug")
    def cloud_stack_slug(self) -> Optional[pulumi.Input[str]]:
        """
        Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        """
        return pulumi.get(self, "cloud_stack_slug")

    @cloud_stack_slug.setter
    def cloud_stack_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_stack_slug", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seconds_to_live", value)


@pulumi.input_type
class _ApiKeyState:
    def __init__(__self__, *,
                 cloud_stack_slug: Optional[pulumi.Input[str]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ApiKey resources.
        :param pulumi.Input[str] cloud_stack_slug: Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        if cloud_stack_slug is not None:
            warnings.warn("""Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""", DeprecationWarning)
            pulumi.log.warn("""cloud_stack_slug is deprecated: Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""")
        if cloud_stack_slug is not None:
            pulumi.set(__self__, "cloud_stack_slug", cloud_stack_slug)
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if seconds_to_live is not None:
            pulumi.set(__self__, "seconds_to_live", seconds_to_live)

    @property
    @pulumi.getter(name="cloudStackSlug")
    def cloud_stack_slug(self) -> Optional[pulumi.Input[str]]:
        """
        Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        """
        return pulumi.get(self, "cloud_stack_slug")

    @cloud_stack_slug.setter
    def cloud_stack_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_stack_slug", value)

    @property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiration")

    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seconds_to_live", value)


class ApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_stack_slug: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        foo = grafana.ApiKey("foo", role="Viewer")
        bar = grafana.ApiKey("bar",
            role="Admin",
            seconds_to_live=30)
        pulumi.export("apiKeyFooKeyOnly", foo.key)
        pulumi.export("apiKeyBar", bar)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_stack_slug: Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        foo = grafana.ApiKey("foo", role="Viewer")
        bar = grafana.ApiKey("bar",
            role="Admin",
            seconds_to_live=30)
        pulumi.export("apiKeyFooKeyOnly", foo.key)
        pulumi.export("apiKeyBar", bar)
        ```

        :param str resource_name: The name of the resource.
        :param ApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_stack_slug: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiKeyArgs.__new__(ApiKeyArgs)

            if cloud_stack_slug is not None and not opts.urn:
                warnings.warn("""Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""", DeprecationWarning)
                pulumi.log.warn("""cloud_stack_slug is deprecated: Use `grafana_cloud_stack_service_account` and `grafana_cloud_stack_service_account_token` resources instead""")
            __props__.__dict__["cloud_stack_slug"] = cloud_stack_slug
            __props__.__dict__["name"] = name
            __props__.__dict__["org_id"] = org_id
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["seconds_to_live"] = seconds_to_live
            __props__.__dict__["expiration"] = None
            __props__.__dict__["key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["key"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ApiKey, __self__).__init__(
            'grafana:index/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloud_stack_slug: Optional[pulumi.Input[str]] = None,
            expiration: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            seconds_to_live: Optional[pulumi.Input[int]] = None) -> 'ApiKey':
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_stack_slug: Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiKeyState.__new__(_ApiKeyState)

        __props__.__dict__["cloud_stack_slug"] = cloud_stack_slug
        __props__.__dict__["expiration"] = expiration
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["role"] = role
        __props__.__dict__["seconds_to_live"] = seconds_to_live
        return ApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudStackSlug")
    def cloud_stack_slug(self) -> pulumi.Output[Optional[str]]:
        """
        Deprecated: Use `CloudStackServiceAccount` and `CloudStackServiceAccountToken` resources instead
        """
        return pulumi.get(self, "cloud_stack_slug")

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[str]:
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "seconds_to_live")

