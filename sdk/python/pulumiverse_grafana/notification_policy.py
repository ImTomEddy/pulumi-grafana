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

__all__ = ['NotificationPolicyArgs', 'NotificationPolicy']

@pulumi.input_type
class NotificationPolicyArgs:
    def __init__(__self__, *,
                 contact_point: pulumi.Input[str],
                 group_bies: pulumi.Input[Sequence[pulumi.Input[str]]],
                 disable_provenance: Optional[pulumi.Input[bool]] = None,
                 group_interval: Optional[pulumi.Input[str]] = None,
                 group_wait: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]] = None,
                 repeat_interval: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NotificationPolicy resource.
        :param pulumi.Input[str] contact_point: The contact point to route notifications that match this rule to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        :param pulumi.Input[bool] disable_provenance: Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        :param pulumi.Input[str] group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes.
        :param pulumi.Input[str] group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]] policies: Routing rules for specific label sets.
        :param pulumi.Input[str] repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        pulumi.set(__self__, "contact_point", contact_point)
        pulumi.set(__self__, "group_bies", group_bies)
        if disable_provenance is not None:
            pulumi.set(__self__, "disable_provenance", disable_provenance)
        if group_interval is not None:
            pulumi.set(__self__, "group_interval", group_interval)
        if group_wait is not None:
            pulumi.set(__self__, "group_wait", group_wait)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if repeat_interval is not None:
            pulumi.set(__self__, "repeat_interval", repeat_interval)

    @property
    @pulumi.getter(name="contactPoint")
    def contact_point(self) -> pulumi.Input[str]:
        """
        The contact point to route notifications that match this rule to.
        """
        return pulumi.get(self, "contact_point")

    @contact_point.setter
    def contact_point(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_point", value)

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        """
        return pulumi.get(self, "group_bies")

    @group_bies.setter
    def group_bies(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "group_bies", value)

    @property
    @pulumi.getter(name="disableProvenance")
    def disable_provenance(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        """
        return pulumi.get(self, "disable_provenance")

    @disable_provenance.setter
    def disable_provenance(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_provenance", value)

    @property
    @pulumi.getter(name="groupInterval")
    def group_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum time interval between two notifications for the same group. Default is 5 minutes.
        """
        return pulumi.get(self, "group_interval")

    @group_interval.setter
    def group_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_interval", value)

    @property
    @pulumi.getter(name="groupWait")
    def group_wait(self) -> Optional[pulumi.Input[str]]:
        """
        Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        """
        return pulumi.get(self, "group_wait")

    @group_wait.setter
    def group_wait(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_wait", value)

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
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]]:
        """
        Routing rules for specific label sets.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        return pulumi.get(self, "repeat_interval")

    @repeat_interval.setter
    def repeat_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repeat_interval", value)


@pulumi.input_type
class _NotificationPolicyState:
    def __init__(__self__, *,
                 contact_point: Optional[pulumi.Input[str]] = None,
                 disable_provenance: Optional[pulumi.Input[bool]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_interval: Optional[pulumi.Input[str]] = None,
                 group_wait: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]] = None,
                 repeat_interval: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NotificationPolicy resources.
        :param pulumi.Input[str] contact_point: The contact point to route notifications that match this rule to.
        :param pulumi.Input[bool] disable_provenance: Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        :param pulumi.Input[str] group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes.
        :param pulumi.Input[str] group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]] policies: Routing rules for specific label sets.
        :param pulumi.Input[str] repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        if contact_point is not None:
            pulumi.set(__self__, "contact_point", contact_point)
        if disable_provenance is not None:
            pulumi.set(__self__, "disable_provenance", disable_provenance)
        if group_bies is not None:
            pulumi.set(__self__, "group_bies", group_bies)
        if group_interval is not None:
            pulumi.set(__self__, "group_interval", group_interval)
        if group_wait is not None:
            pulumi.set(__self__, "group_wait", group_wait)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if repeat_interval is not None:
            pulumi.set(__self__, "repeat_interval", repeat_interval)

    @property
    @pulumi.getter(name="contactPoint")
    def contact_point(self) -> Optional[pulumi.Input[str]]:
        """
        The contact point to route notifications that match this rule to.
        """
        return pulumi.get(self, "contact_point")

    @contact_point.setter
    def contact_point(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_point", value)

    @property
    @pulumi.getter(name="disableProvenance")
    def disable_provenance(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        """
        return pulumi.get(self, "disable_provenance")

    @disable_provenance.setter
    def disable_provenance(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_provenance", value)

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        """
        return pulumi.get(self, "group_bies")

    @group_bies.setter
    def group_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_bies", value)

    @property
    @pulumi.getter(name="groupInterval")
    def group_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum time interval between two notifications for the same group. Default is 5 minutes.
        """
        return pulumi.get(self, "group_interval")

    @group_interval.setter
    def group_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_interval", value)

    @property
    @pulumi.getter(name="groupWait")
    def group_wait(self) -> Optional[pulumi.Input[str]]:
        """
        Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        """
        return pulumi.get(self, "group_wait")

    @group_wait.setter
    def group_wait(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_wait", value)

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
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]]:
        """
        Routing rules for specific label sets.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPolicyPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        return pulumi.get(self, "repeat_interval")

    @repeat_interval.setter
    def repeat_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repeat_interval", value)


class NotificationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_point: Optional[pulumi.Input[str]] = None,
                 disable_provenance: Optional[pulumi.Input[bool]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_interval: Optional[pulumi.Input[str]] = None,
                 group_wait: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationPolicyPolicyArgs']]]]] = None,
                 repeat_interval: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Sets the global notification policy for Grafana.

        !> This resource manages the entire notification policy tree, and will overwrite any existing policies.

        * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/manage-notifications/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)

        This resource requires Grafana 9.1.0 or later.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        a_contact_point = grafana.ContactPoint("aContactPoint", emails=[grafana.ContactPointEmailArgs(
            addresses=[
                "one@company.org",
                "two@company.org",
            ],
            message="{{ len .Alerts.Firing }} firing.",
        )])
        a_mute_timing = grafana.MuteTiming("aMuteTiming", intervals=[grafana.MuteTimingIntervalArgs(
            weekdays=["monday"],
        )])
        my_notification_policy = grafana.NotificationPolicy("myNotificationPolicy",
            group_bies=["..."],
            contact_point=a_contact_point.name,
            group_wait="45s",
            group_interval="6m",
            repeat_interval="3h",
            policies=[
                grafana.NotificationPolicyPolicyArgs(
                    matchers=[
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="mylabel",
                            match="=",
                            value="myvalue",
                        ),
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="alertname",
                            match="=",
                            value="CPU Usage",
                        ),
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="Name",
                            match="=~",
                            value="host.*|host-b.*",
                        ),
                    ],
                    contact_point=a_contact_point.name,
                    continue_=True,
                    mute_timings=[a_mute_timing.name],
                    group_wait="45s",
                    group_interval="6m",
                    repeat_interval="3h",
                    policies=[grafana.NotificationPolicyPolicyPolicyArgs(
                        matchers=[grafana.NotificationPolicyPolicyPolicyMatcherArgs(
                            label="sublabel",
                            match="=",
                            value="subvalue",
                        )],
                        contact_point=a_contact_point.name,
                        group_bies=["..."],
                    )],
                ),
                grafana.NotificationPolicyPolicyArgs(
                    matchers=[grafana.NotificationPolicyPolicyMatcherArgs(
                        label="anotherlabel",
                        match="=~",
                        value="another value.*",
                    )],
                    contact_point=a_contact_point.name,
                    group_bies=["..."],
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ anyString }}"
        ```

        ```sh
        $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ orgID }}:{{ anyString }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] contact_point: The contact point to route notifications that match this rule to.
        :param pulumi.Input[bool] disable_provenance: Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        :param pulumi.Input[str] group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes.
        :param pulumi.Input[str] group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationPolicyPolicyArgs']]]] policies: Routing rules for specific label sets.
        :param pulumi.Input[str] repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Sets the global notification policy for Grafana.

        !> This resource manages the entire notification policy tree, and will overwrite any existing policies.

        * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/manage-notifications/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)

        This resource requires Grafana 9.1.0 or later.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        a_contact_point = grafana.ContactPoint("aContactPoint", emails=[grafana.ContactPointEmailArgs(
            addresses=[
                "one@company.org",
                "two@company.org",
            ],
            message="{{ len .Alerts.Firing }} firing.",
        )])
        a_mute_timing = grafana.MuteTiming("aMuteTiming", intervals=[grafana.MuteTimingIntervalArgs(
            weekdays=["monday"],
        )])
        my_notification_policy = grafana.NotificationPolicy("myNotificationPolicy",
            group_bies=["..."],
            contact_point=a_contact_point.name,
            group_wait="45s",
            group_interval="6m",
            repeat_interval="3h",
            policies=[
                grafana.NotificationPolicyPolicyArgs(
                    matchers=[
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="mylabel",
                            match="=",
                            value="myvalue",
                        ),
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="alertname",
                            match="=",
                            value="CPU Usage",
                        ),
                        grafana.NotificationPolicyPolicyMatcherArgs(
                            label="Name",
                            match="=~",
                            value="host.*|host-b.*",
                        ),
                    ],
                    contact_point=a_contact_point.name,
                    continue_=True,
                    mute_timings=[a_mute_timing.name],
                    group_wait="45s",
                    group_interval="6m",
                    repeat_interval="3h",
                    policies=[grafana.NotificationPolicyPolicyPolicyArgs(
                        matchers=[grafana.NotificationPolicyPolicyPolicyMatcherArgs(
                            label="sublabel",
                            match="=",
                            value="subvalue",
                        )],
                        contact_point=a_contact_point.name,
                        group_bies=["..."],
                    )],
                ),
                grafana.NotificationPolicyPolicyArgs(
                    matchers=[grafana.NotificationPolicyPolicyMatcherArgs(
                        label="anotherlabel",
                        match="=~",
                        value="another value.*",
                    )],
                    contact_point=a_contact_point.name,
                    group_bies=["..."],
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ anyString }}"
        ```

        ```sh
        $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ orgID }}:{{ anyString }}"
        ```

        :param str resource_name: The name of the resource.
        :param NotificationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_point: Optional[pulumi.Input[str]] = None,
                 disable_provenance: Optional[pulumi.Input[bool]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_interval: Optional[pulumi.Input[str]] = None,
                 group_wait: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationPolicyPolicyArgs']]]]] = None,
                 repeat_interval: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationPolicyArgs.__new__(NotificationPolicyArgs)

            if contact_point is None and not opts.urn:
                raise TypeError("Missing required property 'contact_point'")
            __props__.__dict__["contact_point"] = contact_point
            __props__.__dict__["disable_provenance"] = disable_provenance
            if group_bies is None and not opts.urn:
                raise TypeError("Missing required property 'group_bies'")
            __props__.__dict__["group_bies"] = group_bies
            __props__.__dict__["group_interval"] = group_interval
            __props__.__dict__["group_wait"] = group_wait
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["policies"] = policies
            __props__.__dict__["repeat_interval"] = repeat_interval
        super(NotificationPolicy, __self__).__init__(
            'grafana:index/notificationPolicy:NotificationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            contact_point: Optional[pulumi.Input[str]] = None,
            disable_provenance: Optional[pulumi.Input[bool]] = None,
            group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            group_interval: Optional[pulumi.Input[str]] = None,
            group_wait: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationPolicyPolicyArgs']]]]] = None,
            repeat_interval: Optional[pulumi.Input[str]] = None) -> 'NotificationPolicy':
        """
        Get an existing NotificationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] contact_point: The contact point to route notifications that match this rule to.
        :param pulumi.Input[bool] disable_provenance: Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        :param pulumi.Input[str] group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes.
        :param pulumi.Input[str] group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationPolicyPolicyArgs']]]] policies: Routing rules for specific label sets.
        :param pulumi.Input[str] repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationPolicyState.__new__(_NotificationPolicyState)

        __props__.__dict__["contact_point"] = contact_point
        __props__.__dict__["disable_provenance"] = disable_provenance
        __props__.__dict__["group_bies"] = group_bies
        __props__.__dict__["group_interval"] = group_interval
        __props__.__dict__["group_wait"] = group_wait
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["policies"] = policies
        __props__.__dict__["repeat_interval"] = repeat_interval
        return NotificationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contactPoint")
    def contact_point(self) -> pulumi.Output[str]:
        """
        The contact point to route notifications that match this rule to.
        """
        return pulumi.get(self, "contact_point")

    @property
    @pulumi.getter(name="disableProvenance")
    def disable_provenance(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow modifying the notification policy from other sources than Terraform or the Grafana API.
        """
        return pulumi.get(self, "disable_provenance")

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
        """
        return pulumi.get(self, "group_bies")

    @property
    @pulumi.getter(name="groupInterval")
    def group_interval(self) -> pulumi.Output[Optional[str]]:
        """
        Minimum time interval between two notifications for the same group. Default is 5 minutes.
        """
        return pulumi.get(self, "group_interval")

    @property
    @pulumi.getter(name="groupWait")
    def group_wait(self) -> pulumi.Output[Optional[str]]:
        """
        Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        """
        return pulumi.get(self, "group_wait")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationPolicyPolicy']]]:
        """
        Routing rules for specific label sets.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> pulumi.Output[Optional[str]]:
        """
        Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        """
        return pulumi.get(self, "repeat_interval")

