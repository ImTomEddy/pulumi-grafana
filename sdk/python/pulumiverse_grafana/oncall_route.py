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
from ._inputs import *

__all__ = ['OncallRouteArgs', 'OncallRoute']

@pulumi.input_type
class OncallRouteArgs:
    def __init__(__self__, *,
                 escalation_chain_id: pulumi.Input[str],
                 integration_id: pulumi.Input[str],
                 position: pulumi.Input[int],
                 routing_regex: pulumi.Input[str],
                 msteams: Optional[pulumi.Input['OncallRouteMsteamsArgs']] = None,
                 routing_type: Optional[pulumi.Input[str]] = None,
                 slack: Optional[pulumi.Input['OncallRouteSlackArgs']] = None,
                 telegram: Optional[pulumi.Input['OncallRouteTelegramArgs']] = None):
        """
        The set of arguments for constructing a OncallRoute resource.
        :param pulumi.Input[str] escalation_chain_id: The ID of the escalation chain.
        :param pulumi.Input[str] integration_id: The ID of the integration.
        :param pulumi.Input[int] position: The position of the route (starts from 0).
        :param pulumi.Input[str] routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        :param pulumi.Input['OncallRouteMsteamsArgs'] msteams: MS teams-specific settings for a route.
        :param pulumi.Input[str] routing_type: The type of route. Can be jinja2, regex
        :param pulumi.Input['OncallRouteSlackArgs'] slack: Slack-specific settings for a route.
        :param pulumi.Input['OncallRouteTelegramArgs'] telegram: Telegram-specific settings for a route.
        """
        pulumi.set(__self__, "escalation_chain_id", escalation_chain_id)
        pulumi.set(__self__, "integration_id", integration_id)
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "routing_regex", routing_regex)
        if msteams is not None:
            pulumi.set(__self__, "msteams", msteams)
        if routing_type is not None:
            pulumi.set(__self__, "routing_type", routing_type)
        if slack is not None:
            pulumi.set(__self__, "slack", slack)
        if telegram is not None:
            pulumi.set(__self__, "telegram", telegram)

    @property
    @pulumi.getter(name="escalationChainId")
    def escalation_chain_id(self) -> pulumi.Input[str]:
        """
        The ID of the escalation chain.
        """
        return pulumi.get(self, "escalation_chain_id")

    @escalation_chain_id.setter
    def escalation_chain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "escalation_chain_id", value)

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Input[str]:
        """
        The ID of the integration.
        """
        return pulumi.get(self, "integration_id")

    @integration_id.setter
    def integration_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_id", value)

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[int]:
        """
        The position of the route (starts from 0).
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: pulumi.Input[int]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="routingRegex")
    def routing_regex(self) -> pulumi.Input[str]:
        """
        Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        """
        return pulumi.get(self, "routing_regex")

    @routing_regex.setter
    def routing_regex(self, value: pulumi.Input[str]):
        pulumi.set(self, "routing_regex", value)

    @property
    @pulumi.getter
    def msteams(self) -> Optional[pulumi.Input['OncallRouteMsteamsArgs']]:
        """
        MS teams-specific settings for a route.
        """
        return pulumi.get(self, "msteams")

    @msteams.setter
    def msteams(self, value: Optional[pulumi.Input['OncallRouteMsteamsArgs']]):
        pulumi.set(self, "msteams", value)

    @property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of route. Can be jinja2, regex
        """
        return pulumi.get(self, "routing_type")

    @routing_type.setter
    def routing_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_type", value)

    @property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input['OncallRouteSlackArgs']]:
        """
        Slack-specific settings for a route.
        """
        return pulumi.get(self, "slack")

    @slack.setter
    def slack(self, value: Optional[pulumi.Input['OncallRouteSlackArgs']]):
        pulumi.set(self, "slack", value)

    @property
    @pulumi.getter
    def telegram(self) -> Optional[pulumi.Input['OncallRouteTelegramArgs']]:
        """
        Telegram-specific settings for a route.
        """
        return pulumi.get(self, "telegram")

    @telegram.setter
    def telegram(self, value: Optional[pulumi.Input['OncallRouteTelegramArgs']]):
        pulumi.set(self, "telegram", value)


@pulumi.input_type
class _OncallRouteState:
    def __init__(__self__, *,
                 escalation_chain_id: Optional[pulumi.Input[str]] = None,
                 integration_id: Optional[pulumi.Input[str]] = None,
                 msteams: Optional[pulumi.Input['OncallRouteMsteamsArgs']] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 routing_regex: Optional[pulumi.Input[str]] = None,
                 routing_type: Optional[pulumi.Input[str]] = None,
                 slack: Optional[pulumi.Input['OncallRouteSlackArgs']] = None,
                 telegram: Optional[pulumi.Input['OncallRouteTelegramArgs']] = None):
        """
        Input properties used for looking up and filtering OncallRoute resources.
        :param pulumi.Input[str] escalation_chain_id: The ID of the escalation chain.
        :param pulumi.Input[str] integration_id: The ID of the integration.
        :param pulumi.Input['OncallRouteMsteamsArgs'] msteams: MS teams-specific settings for a route.
        :param pulumi.Input[int] position: The position of the route (starts from 0).
        :param pulumi.Input[str] routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        :param pulumi.Input[str] routing_type: The type of route. Can be jinja2, regex
        :param pulumi.Input['OncallRouteSlackArgs'] slack: Slack-specific settings for a route.
        :param pulumi.Input['OncallRouteTelegramArgs'] telegram: Telegram-specific settings for a route.
        """
        if escalation_chain_id is not None:
            pulumi.set(__self__, "escalation_chain_id", escalation_chain_id)
        if integration_id is not None:
            pulumi.set(__self__, "integration_id", integration_id)
        if msteams is not None:
            pulumi.set(__self__, "msteams", msteams)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if routing_regex is not None:
            pulumi.set(__self__, "routing_regex", routing_regex)
        if routing_type is not None:
            pulumi.set(__self__, "routing_type", routing_type)
        if slack is not None:
            pulumi.set(__self__, "slack", slack)
        if telegram is not None:
            pulumi.set(__self__, "telegram", telegram)

    @property
    @pulumi.getter(name="escalationChainId")
    def escalation_chain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the escalation chain.
        """
        return pulumi.get(self, "escalation_chain_id")

    @escalation_chain_id.setter
    def escalation_chain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "escalation_chain_id", value)

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the integration.
        """
        return pulumi.get(self, "integration_id")

    @integration_id.setter
    def integration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_id", value)

    @property
    @pulumi.getter
    def msteams(self) -> Optional[pulumi.Input['OncallRouteMsteamsArgs']]:
        """
        MS teams-specific settings for a route.
        """
        return pulumi.get(self, "msteams")

    @msteams.setter
    def msteams(self, value: Optional[pulumi.Input['OncallRouteMsteamsArgs']]):
        pulumi.set(self, "msteams", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[int]]:
        """
        The position of the route (starts from 0).
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="routingRegex")
    def routing_regex(self) -> Optional[pulumi.Input[str]]:
        """
        Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        """
        return pulumi.get(self, "routing_regex")

    @routing_regex.setter
    def routing_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_regex", value)

    @property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of route. Can be jinja2, regex
        """
        return pulumi.get(self, "routing_type")

    @routing_type.setter
    def routing_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_type", value)

    @property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input['OncallRouteSlackArgs']]:
        """
        Slack-specific settings for a route.
        """
        return pulumi.get(self, "slack")

    @slack.setter
    def slack(self, value: Optional[pulumi.Input['OncallRouteSlackArgs']]):
        pulumi.set(self, "slack", value)

    @property
    @pulumi.getter
    def telegram(self) -> Optional[pulumi.Input['OncallRouteTelegramArgs']]:
        """
        Telegram-specific settings for a route.
        """
        return pulumi.get(self, "telegram")

    @telegram.setter
    def telegram(self, value: Optional[pulumi.Input['OncallRouteTelegramArgs']]):
        pulumi.set(self, "telegram", value)


class OncallRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 escalation_chain_id: Optional[pulumi.Input[str]] = None,
                 integration_id: Optional[pulumi.Input[str]] = None,
                 msteams: Optional[pulumi.Input[pulumi.InputType['OncallRouteMsteamsArgs']]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 routing_regex: Optional[pulumi.Input[str]] = None,
                 routing_type: Optional[pulumi.Input[str]] = None,
                 slack: Optional[pulumi.Input[pulumi.InputType['OncallRouteSlackArgs']]] = None,
                 telegram: Optional[pulumi.Input[pulumi.InputType['OncallRouteTelegramArgs']]] = None,
                 __props__=None):
        """
        Create a OncallRoute resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] escalation_chain_id: The ID of the escalation chain.
        :param pulumi.Input[str] integration_id: The ID of the integration.
        :param pulumi.Input[pulumi.InputType['OncallRouteMsteamsArgs']] msteams: MS teams-specific settings for a route.
        :param pulumi.Input[int] position: The position of the route (starts from 0).
        :param pulumi.Input[str] routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        :param pulumi.Input[str] routing_type: The type of route. Can be jinja2, regex
        :param pulumi.Input[pulumi.InputType['OncallRouteSlackArgs']] slack: Slack-specific settings for a route.
        :param pulumi.Input[pulumi.InputType['OncallRouteTelegramArgs']] telegram: Telegram-specific settings for a route.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OncallRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OncallRoute resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OncallRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OncallRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 escalation_chain_id: Optional[pulumi.Input[str]] = None,
                 integration_id: Optional[pulumi.Input[str]] = None,
                 msteams: Optional[pulumi.Input[pulumi.InputType['OncallRouteMsteamsArgs']]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 routing_regex: Optional[pulumi.Input[str]] = None,
                 routing_type: Optional[pulumi.Input[str]] = None,
                 slack: Optional[pulumi.Input[pulumi.InputType['OncallRouteSlackArgs']]] = None,
                 telegram: Optional[pulumi.Input[pulumi.InputType['OncallRouteTelegramArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OncallRouteArgs.__new__(OncallRouteArgs)

            if escalation_chain_id is None and not opts.urn:
                raise TypeError("Missing required property 'escalation_chain_id'")
            __props__.__dict__["escalation_chain_id"] = escalation_chain_id
            if integration_id is None and not opts.urn:
                raise TypeError("Missing required property 'integration_id'")
            __props__.__dict__["integration_id"] = integration_id
            __props__.__dict__["msteams"] = msteams
            if position is None and not opts.urn:
                raise TypeError("Missing required property 'position'")
            __props__.__dict__["position"] = position
            if routing_regex is None and not opts.urn:
                raise TypeError("Missing required property 'routing_regex'")
            __props__.__dict__["routing_regex"] = routing_regex
            __props__.__dict__["routing_type"] = routing_type
            __props__.__dict__["slack"] = slack
            __props__.__dict__["telegram"] = telegram
        super(OncallRoute, __self__).__init__(
            'grafana:index/oncallRoute:OncallRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            escalation_chain_id: Optional[pulumi.Input[str]] = None,
            integration_id: Optional[pulumi.Input[str]] = None,
            msteams: Optional[pulumi.Input[pulumi.InputType['OncallRouteMsteamsArgs']]] = None,
            position: Optional[pulumi.Input[int]] = None,
            routing_regex: Optional[pulumi.Input[str]] = None,
            routing_type: Optional[pulumi.Input[str]] = None,
            slack: Optional[pulumi.Input[pulumi.InputType['OncallRouteSlackArgs']]] = None,
            telegram: Optional[pulumi.Input[pulumi.InputType['OncallRouteTelegramArgs']]] = None) -> 'OncallRoute':
        """
        Get an existing OncallRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] escalation_chain_id: The ID of the escalation chain.
        :param pulumi.Input[str] integration_id: The ID of the integration.
        :param pulumi.Input[pulumi.InputType['OncallRouteMsteamsArgs']] msteams: MS teams-specific settings for a route.
        :param pulumi.Input[int] position: The position of the route (starts from 0).
        :param pulumi.Input[str] routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        :param pulumi.Input[str] routing_type: The type of route. Can be jinja2, regex
        :param pulumi.Input[pulumi.InputType['OncallRouteSlackArgs']] slack: Slack-specific settings for a route.
        :param pulumi.Input[pulumi.InputType['OncallRouteTelegramArgs']] telegram: Telegram-specific settings for a route.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OncallRouteState.__new__(_OncallRouteState)

        __props__.__dict__["escalation_chain_id"] = escalation_chain_id
        __props__.__dict__["integration_id"] = integration_id
        __props__.__dict__["msteams"] = msteams
        __props__.__dict__["position"] = position
        __props__.__dict__["routing_regex"] = routing_regex
        __props__.__dict__["routing_type"] = routing_type
        __props__.__dict__["slack"] = slack
        __props__.__dict__["telegram"] = telegram
        return OncallRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="escalationChainId")
    def escalation_chain_id(self) -> pulumi.Output[str]:
        """
        The ID of the escalation chain.
        """
        return pulumi.get(self, "escalation_chain_id")

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Output[str]:
        """
        The ID of the integration.
        """
        return pulumi.get(self, "integration_id")

    @property
    @pulumi.getter
    def msteams(self) -> pulumi.Output[Optional['outputs.OncallRouteMsteams']]:
        """
        MS teams-specific settings for a route.
        """
        return pulumi.get(self, "msteams")

    @property
    @pulumi.getter
    def position(self) -> pulumi.Output[int]:
        """
        The position of the route (starts from 0).
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="routingRegex")
    def routing_regex(self) -> pulumi.Output[str]:
        """
        Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.
        """
        return pulumi.get(self, "routing_regex")

    @property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of route. Can be jinja2, regex
        """
        return pulumi.get(self, "routing_type")

    @property
    @pulumi.getter
    def slack(self) -> pulumi.Output[Optional['outputs.OncallRouteSlack']]:
        """
        Slack-specific settings for a route.
        """
        return pulumi.get(self, "slack")

    @property
    @pulumi.getter
    def telegram(self) -> pulumi.Output[Optional['outputs.OncallRouteTelegram']]:
        """
        Telegram-specific settings for a route.
        """
        return pulumi.get(self, "telegram")

