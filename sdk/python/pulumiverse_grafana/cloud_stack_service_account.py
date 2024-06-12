# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudStackServiceAccountArgs', 'CloudStackServiceAccount']

@pulumi.input_type
class CloudStackServiceAccountArgs:
    def __init__(__self__, *,
                 role: pulumi.Input[str],
                 stack_slug: pulumi.Input[str],
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudStackServiceAccount resource.
        :param pulumi.Input[str] role: The basic role of the service account in the organization.
        :param pulumi.Input[bool] is_disabled: The disabled status for the service account. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the service account.
        """
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "stack_slug", stack_slug)
        if is_disabled is not None:
            pulumi.set(__self__, "is_disabled", is_disabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The basic role of the service account in the organization.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="stackSlug")
    def stack_slug(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stack_slug")

    @stack_slug.setter
    def stack_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack_slug", value)

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The disabled status for the service account. Defaults to `false`.
        """
        return pulumi.get(self, "is_disabled")

    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_disabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CloudStackServiceAccountState:
    def __init__(__self__, *,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 stack_slug: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudStackServiceAccount resources.
        :param pulumi.Input[bool] is_disabled: The disabled status for the service account. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the service account.
        :param pulumi.Input[str] role: The basic role of the service account in the organization.
        """
        if is_disabled is not None:
            pulumi.set(__self__, "is_disabled", is_disabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if stack_slug is not None:
            pulumi.set(__self__, "stack_slug", stack_slug)

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The disabled status for the service account. Defaults to `false`.
        """
        return pulumi.get(self, "is_disabled")

    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_disabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The basic role of the service account in the organization.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="stackSlug")
    def stack_slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stack_slug")

    @stack_slug.setter
    def stack_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_slug", value)


class CloudStackServiceAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 stack_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages service accounts of a Grafana Cloud stack using the Cloud API
        This can be used to bootstrap a management service account for a new stack

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)

        Required access policy scopes:

        * stacks:read
        * stack-service-accounts:write

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        cloud_sa = grafana.CloudStackServiceAccount("cloudSa",
            is_disabled=False,
            role="Admin",
            stack_slug="<your stack slug>")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/cloudStackServiceAccount:CloudStackServiceAccount name "{{ stackSlug }}:{{ serviceAccountID }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_disabled: The disabled status for the service account. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the service account.
        :param pulumi.Input[str] role: The basic role of the service account in the organization.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudStackServiceAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages service accounts of a Grafana Cloud stack using the Cloud API
        This can be used to bootstrap a management service account for a new stack

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)

        Required access policy scopes:

        * stacks:read
        * stack-service-accounts:write

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        cloud_sa = grafana.CloudStackServiceAccount("cloudSa",
            is_disabled=False,
            role="Admin",
            stack_slug="<your stack slug>")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/cloudStackServiceAccount:CloudStackServiceAccount name "{{ stackSlug }}:{{ serviceAccountID }}"
        ```

        :param str resource_name: The name of the resource.
        :param CloudStackServiceAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudStackServiceAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 stack_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudStackServiceAccountArgs.__new__(CloudStackServiceAccountArgs)

            __props__.__dict__["is_disabled"] = is_disabled
            __props__.__dict__["name"] = name
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if stack_slug is None and not opts.urn:
                raise TypeError("Missing required property 'stack_slug'")
            __props__.__dict__["stack_slug"] = stack_slug
        super(CloudStackServiceAccount, __self__).__init__(
            'grafana:index/cloudStackServiceAccount:CloudStackServiceAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            is_disabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            stack_slug: Optional[pulumi.Input[str]] = None) -> 'CloudStackServiceAccount':
        """
        Get an existing CloudStackServiceAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_disabled: The disabled status for the service account. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the service account.
        :param pulumi.Input[str] role: The basic role of the service account in the organization.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudStackServiceAccountState.__new__(_CloudStackServiceAccountState)

        __props__.__dict__["is_disabled"] = is_disabled
        __props__.__dict__["name"] = name
        __props__.__dict__["role"] = role
        __props__.__dict__["stack_slug"] = stack_slug
        return CloudStackServiceAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        The disabled status for the service account. Defaults to `false`.
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the service account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The basic role of the service account in the organization.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="stackSlug")
    def stack_slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_slug")

