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

__all__ = ['OncallIntegrationArgs', 'OncallIntegration']

@pulumi.input_type
class OncallIntegrationArgs:
    def __init__(__self__, *,
                 default_route: pulumi.Input['OncallIntegrationDefaultRouteArgs'],
                 type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 templates: Optional[pulumi.Input['OncallIntegrationTemplatesArgs']] = None):
        """
        The set of arguments for constructing a OncallIntegration resource.
        :param pulumi.Input['OncallIntegrationDefaultRouteArgs'] default_route: The Default route for all alerts from the given integration
        :param pulumi.Input[str] type: The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        :param pulumi.Input[str] name: The name of the service integration.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input['OncallIntegrationTemplatesArgs'] templates: Jinja2 templates for Alert payload. An empty templates block will be ignored.
        """
        pulumi.set(__self__, "default_route", default_route)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if templates is not None:
            pulumi.set(__self__, "templates", templates)

    @property
    @pulumi.getter(name="defaultRoute")
    def default_route(self) -> pulumi.Input['OncallIntegrationDefaultRouteArgs']:
        """
        The Default route for all alerts from the given integration
        """
        return pulumi.get(self, "default_route")

    @default_route.setter
    def default_route(self, value: pulumi.Input['OncallIntegrationDefaultRouteArgs']):
        pulumi.set(self, "default_route", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def templates(self) -> Optional[pulumi.Input['OncallIntegrationTemplatesArgs']]:
        """
        Jinja2 templates for Alert payload. An empty templates block will be ignored.
        """
        return pulumi.get(self, "templates")

    @templates.setter
    def templates(self, value: Optional[pulumi.Input['OncallIntegrationTemplatesArgs']]):
        pulumi.set(self, "templates", value)


@pulumi.input_type
class _OncallIntegrationState:
    def __init__(__self__, *,
                 default_route: Optional[pulumi.Input['OncallIntegrationDefaultRouteArgs']] = None,
                 link: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 templates: Optional[pulumi.Input['OncallIntegrationTemplatesArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OncallIntegration resources.
        :param pulumi.Input['OncallIntegrationDefaultRouteArgs'] default_route: The Default route for all alerts from the given integration
        :param pulumi.Input[str] link: The link for using in an integrated tool.
        :param pulumi.Input[str] name: The name of the service integration.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input['OncallIntegrationTemplatesArgs'] templates: Jinja2 templates for Alert payload. An empty templates block will be ignored.
        :param pulumi.Input[str] type: The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        if default_route is not None:
            pulumi.set(__self__, "default_route", default_route)
        if link is not None:
            pulumi.set(__self__, "link", link)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if templates is not None:
            pulumi.set(__self__, "templates", templates)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultRoute")
    def default_route(self) -> Optional[pulumi.Input['OncallIntegrationDefaultRouteArgs']]:
        """
        The Default route for all alerts from the given integration
        """
        return pulumi.get(self, "default_route")

    @default_route.setter
    def default_route(self, value: Optional[pulumi.Input['OncallIntegrationDefaultRouteArgs']]):
        pulumi.set(self, "default_route", value)

    @property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input[str]]:
        """
        The link for using in an integrated tool.
        """
        return pulumi.get(self, "link")

    @link.setter
    def link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "link", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def templates(self) -> Optional[pulumi.Input['OncallIntegrationTemplatesArgs']]:
        """
        Jinja2 templates for Alert payload. An empty templates block will be ignored.
        """
        return pulumi.get(self, "templates")

    @templates.setter
    def templates(self, value: Optional[pulumi.Input['OncallIntegrationTemplatesArgs']]):
        pulumi.set(self, "templates", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class OncallIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_route: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationDefaultRouteArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 templates: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationTemplatesArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        * [Official documentation](https://grafana.com/docs/oncall/latest/integrations/)
        * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/)

        ## Import

        ```sh
         $ pulumi import grafana:index/oncallIntegration:OncallIntegration integration_name {{integration_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OncallIntegrationDefaultRouteArgs']] default_route: The Default route for all alerts from the given integration
        :param pulumi.Input[str] name: The name of the service integration.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[pulumi.InputType['OncallIntegrationTemplatesArgs']] templates: Jinja2 templates for Alert payload. An empty templates block will be ignored.
        :param pulumi.Input[str] type: The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OncallIntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [Official documentation](https://grafana.com/docs/oncall/latest/integrations/)
        * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/)

        ## Import

        ```sh
         $ pulumi import grafana:index/oncallIntegration:OncallIntegration integration_name {{integration_id}}
        ```

        :param str resource_name: The name of the resource.
        :param OncallIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OncallIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_route: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationDefaultRouteArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 templates: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationTemplatesArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OncallIntegrationArgs.__new__(OncallIntegrationArgs)

            if default_route is None and not opts.urn:
                raise TypeError("Missing required property 'default_route'")
            __props__.__dict__["default_route"] = default_route
            __props__.__dict__["name"] = name
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["templates"] = templates
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["link"] = None
        super(OncallIntegration, __self__).__init__(
            'grafana:index/oncallIntegration:OncallIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_route: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationDefaultRouteArgs']]] = None,
            link: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            templates: Optional[pulumi.Input[pulumi.InputType['OncallIntegrationTemplatesArgs']]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'OncallIntegration':
        """
        Get an existing OncallIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OncallIntegrationDefaultRouteArgs']] default_route: The Default route for all alerts from the given integration
        :param pulumi.Input[str] link: The link for using in an integrated tool.
        :param pulumi.Input[str] name: The name of the service integration.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[pulumi.InputType['OncallIntegrationTemplatesArgs']] templates: Jinja2 templates for Alert payload. An empty templates block will be ignored.
        :param pulumi.Input[str] type: The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OncallIntegrationState.__new__(_OncallIntegrationState)

        __props__.__dict__["default_route"] = default_route
        __props__.__dict__["link"] = link
        __props__.__dict__["name"] = name
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["templates"] = templates
        __props__.__dict__["type"] = type
        return OncallIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultRoute")
    def default_route(self) -> pulumi.Output['outputs.OncallIntegrationDefaultRoute']:
        """
        The Default route for all alerts from the given integration
        """
        return pulumi.get(self, "default_route")

    @property
    @pulumi.getter
    def link(self) -> pulumi.Output[str]:
        """
        The link for using in an integrated tool.
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the service integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def templates(self) -> pulumi.Output[Optional['outputs.OncallIntegrationTemplates']]:
        """
        Jinja2 templates for Alert payload. An empty templates block will be ignored.
        """
        return pulumi.get(self, "templates")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        """
        return pulumi.get(self, "type")

