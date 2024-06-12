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

__all__ = ['SyntheticMonitoringCheckArgs', 'SyntheticMonitoringCheck']

@pulumi.input_type
class SyntheticMonitoringCheckArgs:
    def __init__(__self__, *,
                 job: pulumi.Input[str],
                 probes: pulumi.Input[Sequence[pulumi.Input[int]]],
                 settings: pulumi.Input['SyntheticMonitoringCheckSettingsArgs'],
                 target: pulumi.Input[str],
                 alert_sensitivity: Optional[pulumi.Input[str]] = None,
                 basic_metrics_only: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SyntheticMonitoringCheck resource.
        :param pulumi.Input[str] job: Name used for job label.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] probes: List of probe location IDs where this target will be checked from.
        :param pulumi.Input['SyntheticMonitoringCheckSettingsArgs'] settings: Check settings. Should contain exactly one nested block.
        :param pulumi.Input[str] target: Hostname to ping.
        :param pulumi.Input[str] alert_sensitivity: Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
               levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        :param pulumi.Input[bool] basic_metrics_only: Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
               metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        :param pulumi.Input[bool] enabled: Whether to enable the check.
        :param pulumi.Input[int] frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
               value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
               check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
               the labels cannot be empty, and the maximum length is 32 bytes.
        :param pulumi.Input[int] timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
               and the maximum 10 seconds (10000 ms).
        """
        pulumi.set(__self__, "job", job)
        pulumi.set(__self__, "probes", probes)
        pulumi.set(__self__, "settings", settings)
        pulumi.set(__self__, "target", target)
        if alert_sensitivity is not None:
            pulumi.set(__self__, "alert_sensitivity", alert_sensitivity)
        if basic_metrics_only is not None:
            pulumi.set(__self__, "basic_metrics_only", basic_metrics_only)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter
    def job(self) -> pulumi.Input[str]:
        """
        Name used for job label.
        """
        return pulumi.get(self, "job")

    @job.setter
    def job(self, value: pulumi.Input[str]):
        pulumi.set(self, "job", value)

    @property
    @pulumi.getter
    def probes(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        List of probe location IDs where this target will be checked from.
        """
        return pulumi.get(self, "probes")

    @probes.setter
    def probes(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "probes", value)

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Input['SyntheticMonitoringCheckSettingsArgs']:
        """
        Check settings. Should contain exactly one nested block.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: pulumi.Input['SyntheticMonitoringCheckSettingsArgs']):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        Hostname to ping.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> Optional[pulumi.Input[str]]:
        """
        Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
        levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        """
        return pulumi.get(self, "alert_sensitivity")

    @alert_sensitivity.setter
    def alert_sensitivity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_sensitivity", value)

    @property
    @pulumi.getter(name="basicMetricsOnly")
    def basic_metrics_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
        metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        """
        return pulumi.get(self, "basic_metrics_only")

    @basic_metrics_only.setter
    def basic_metrics_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "basic_metrics_only", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the check.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[int]]:
        """
        How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
        value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
        check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
        the labels cannot be empty, and the maximum length is 32 bytes.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
        and the maximum 10 seconds (10000 ms).
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


@pulumi.input_type
class _SyntheticMonitoringCheckState:
    def __init__(__self__, *,
                 alert_sensitivity: Optional[pulumi.Input[str]] = None,
                 basic_metrics_only: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 job: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 settings: Optional[pulumi.Input['SyntheticMonitoringCheckSettingsArgs']] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[int]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering SyntheticMonitoringCheck resources.
        :param pulumi.Input[str] alert_sensitivity: Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
               levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        :param pulumi.Input[bool] basic_metrics_only: Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
               metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        :param pulumi.Input[bool] enabled: Whether to enable the check.
        :param pulumi.Input[int] frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
               value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        :param pulumi.Input[str] job: Name used for job label.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
               check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
               the labels cannot be empty, and the maximum length is 32 bytes.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] probes: List of probe location IDs where this target will be checked from.
        :param pulumi.Input['SyntheticMonitoringCheckSettingsArgs'] settings: Check settings. Should contain exactly one nested block.
        :param pulumi.Input[str] target: Hostname to ping.
        :param pulumi.Input[int] tenant_id: The tenant ID of the check.
        :param pulumi.Input[int] timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
               and the maximum 10 seconds (10000 ms).
        """
        if alert_sensitivity is not None:
            pulumi.set(__self__, "alert_sensitivity", alert_sensitivity)
        if basic_metrics_only is not None:
            pulumi.set(__self__, "basic_metrics_only", basic_metrics_only)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if job is not None:
            pulumi.set(__self__, "job", job)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if probes is not None:
            pulumi.set(__self__, "probes", probes)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> Optional[pulumi.Input[str]]:
        """
        Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
        levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        """
        return pulumi.get(self, "alert_sensitivity")

    @alert_sensitivity.setter
    def alert_sensitivity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_sensitivity", value)

    @property
    @pulumi.getter(name="basicMetricsOnly")
    def basic_metrics_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
        metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        """
        return pulumi.get(self, "basic_metrics_only")

    @basic_metrics_only.setter
    def basic_metrics_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "basic_metrics_only", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the check.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[int]]:
        """
        How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
        value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def job(self) -> Optional[pulumi.Input[str]]:
        """
        Name used for job label.
        """
        return pulumi.get(self, "job")

    @job.setter
    def job(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
        check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
        the labels cannot be empty, and the maximum length is 32 bytes.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def probes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of probe location IDs where this target will be checked from.
        """
        return pulumi.get(self, "probes")

    @probes.setter
    def probes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "probes", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input['SyntheticMonitoringCheckSettingsArgs']]:
        """
        Check settings. Should contain exactly one nested block.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input['SyntheticMonitoringCheckSettingsArgs']]):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        Hostname to ping.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[int]]:
        """
        The tenant ID of the check.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
        and the maximum 10 seconds (10000 ms).
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


class SyntheticMonitoringCheck(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_sensitivity: Optional[pulumi.Input[str]] = None,
                 basic_metrics_only: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 job: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['SyntheticMonitoringCheckSettingsArgs']]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a SyntheticMonitoringCheck resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_sensitivity: Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
               levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        :param pulumi.Input[bool] basic_metrics_only: Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
               metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        :param pulumi.Input[bool] enabled: Whether to enable the check.
        :param pulumi.Input[int] frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
               value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        :param pulumi.Input[str] job: Name used for job label.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
               check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
               the labels cannot be empty, and the maximum length is 32 bytes.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] probes: List of probe location IDs where this target will be checked from.
        :param pulumi.Input[pulumi.InputType['SyntheticMonitoringCheckSettingsArgs']] settings: Check settings. Should contain exactly one nested block.
        :param pulumi.Input[str] target: Hostname to ping.
        :param pulumi.Input[int] timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
               and the maximum 10 seconds (10000 ms).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyntheticMonitoringCheckArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SyntheticMonitoringCheck resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SyntheticMonitoringCheckArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyntheticMonitoringCheckArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_sensitivity: Optional[pulumi.Input[str]] = None,
                 basic_metrics_only: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 job: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['SyntheticMonitoringCheckSettingsArgs']]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SyntheticMonitoringCheckArgs.__new__(SyntheticMonitoringCheckArgs)

            __props__.__dict__["alert_sensitivity"] = alert_sensitivity
            __props__.__dict__["basic_metrics_only"] = basic_metrics_only
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["frequency"] = frequency
            if job is None and not opts.urn:
                raise TypeError("Missing required property 'job'")
            __props__.__dict__["job"] = job
            __props__.__dict__["labels"] = labels
            if probes is None and not opts.urn:
                raise TypeError("Missing required property 'probes'")
            __props__.__dict__["probes"] = probes
            if settings is None and not opts.urn:
                raise TypeError("Missing required property 'settings'")
            __props__.__dict__["settings"] = settings
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["tenant_id"] = None
        super(SyntheticMonitoringCheck, __self__).__init__(
            'grafana:index/syntheticMonitoringCheck:SyntheticMonitoringCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alert_sensitivity: Optional[pulumi.Input[str]] = None,
            basic_metrics_only: Optional[pulumi.Input[bool]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            frequency: Optional[pulumi.Input[int]] = None,
            job: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            probes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            settings: Optional[pulumi.Input[pulumi.InputType['SyntheticMonitoringCheckSettingsArgs']]] = None,
            target: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[int]] = None,
            timeout: Optional[pulumi.Input[int]] = None) -> 'SyntheticMonitoringCheck':
        """
        Get an existing SyntheticMonitoringCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_sensitivity: Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
               levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        :param pulumi.Input[bool] basic_metrics_only: Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
               metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        :param pulumi.Input[bool] enabled: Whether to enable the check.
        :param pulumi.Input[int] frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
               value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        :param pulumi.Input[str] job: Name used for job label.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
               check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
               the labels cannot be empty, and the maximum length is 32 bytes.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] probes: List of probe location IDs where this target will be checked from.
        :param pulumi.Input[pulumi.InputType['SyntheticMonitoringCheckSettingsArgs']] settings: Check settings. Should contain exactly one nested block.
        :param pulumi.Input[str] target: Hostname to ping.
        :param pulumi.Input[int] tenant_id: The tenant ID of the check.
        :param pulumi.Input[int] timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
               and the maximum 10 seconds (10000 ms).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SyntheticMonitoringCheckState.__new__(_SyntheticMonitoringCheckState)

        __props__.__dict__["alert_sensitivity"] = alert_sensitivity
        __props__.__dict__["basic_metrics_only"] = basic_metrics_only
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["frequency"] = frequency
        __props__.__dict__["job"] = job
        __props__.__dict__["labels"] = labels
        __props__.__dict__["probes"] = probes
        __props__.__dict__["settings"] = settings
        __props__.__dict__["target"] = target
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["timeout"] = timeout
        return SyntheticMonitoringCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> pulumi.Output[Optional[str]]:
        """
        Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
        levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
        """
        return pulumi.get(self, "alert_sensitivity")

    @property
    @pulumi.getter(name="basicMetricsOnly")
    def basic_metrics_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
        metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
        """
        return pulumi.get(self, "basic_metrics_only")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable the check.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[Optional[int]]:
        """
        How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
        value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def job(self) -> pulumi.Output[str]:
        """
        Name used for job label.
        """
        return pulumi.get(self, "job")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
        check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
        the labels cannot be empty, and the maximum length is 32 bytes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def probes(self) -> pulumi.Output[Sequence[int]]:
        """
        List of probe location IDs where this target will be checked from.
        """
        return pulumi.get(self, "probes")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output['outputs.SyntheticMonitoringCheckSettings']:
        """
        Check settings. Should contain exactly one nested block.
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        Hostname to ping.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[int]:
        """
        The tenant ID of the check.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
        and the maximum 10 seconds (10000 ms).
        """
        return pulumi.get(self, "timeout")

