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

__all__ = ['ReportArgs', 'Report']

@pulumi.input_type
class ReportArgs:
    def __init__(__self__, *,
                 recipients: pulumi.Input[Sequence[pulumi.Input[str]]],
                 schedule: pulumi.Input['ReportScheduleArgs'],
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 dashboards: Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]] = None,
                 formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 include_dashboard_link: Optional[pulumi.Input[bool]] = None,
                 include_table_csv: Optional[pulumi.Input[bool]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 orientation: Optional[pulumi.Input[str]] = None,
                 reply_to: Optional[pulumi.Input[str]] = None,
                 time_range: Optional[pulumi.Input['ReportTimeRangeArgs']] = None):
        """
        The set of arguments for constructing a Report resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] recipients: List of recipients of the report.
        :param pulumi.Input['ReportScheduleArgs'] schedule: Schedule of the report.
        :param pulumi.Input[int] dashboard_id: Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: Dashboard to be sent in the report.
        :param pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]] dashboards: List of dashboards to render into the report
        :param pulumi.Input[Sequence[pulumi.Input[str]]] formats: Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        :param pulumi.Input[bool] include_dashboard_link: Whether to include a link to the dashboard in the report.
        :param pulumi.Input[bool] include_table_csv: Whether to include a CSV file of table panel data.
        :param pulumi.Input[str] layout: Layout of the report. Allowed values: `simple`, `grid`.
        :param pulumi.Input[str] message: Message to be sent in the report.
        :param pulumi.Input[str] name: Name of the report.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] orientation: Orientation of the report. Allowed values: `landscape`, `portrait`.
        :param pulumi.Input[str] reply_to: Reply-to email address of the report.
        :param pulumi.Input['ReportTimeRangeArgs'] time_range: Time range of the report.
        """
        pulumi.set(__self__, "recipients", recipients)
        pulumi.set(__self__, "schedule", schedule)
        if dashboard_id is not None:
            warnings.warn("""Use dashboards instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: Use dashboards instead""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            warnings.warn("""Use dashboards instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_uid is deprecated: Use dashboards instead""")
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if dashboards is not None:
            pulumi.set(__self__, "dashboards", dashboards)
        if formats is not None:
            pulumi.set(__self__, "formats", formats)
        if include_dashboard_link is not None:
            pulumi.set(__self__, "include_dashboard_link", include_dashboard_link)
        if include_table_csv is not None:
            pulumi.set(__self__, "include_table_csv", include_table_csv)
        if layout is not None:
            pulumi.set(__self__, "layout", layout)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if orientation is not None:
            pulumi.set(__self__, "orientation", orientation)
        if reply_to is not None:
            pulumi.set(__self__, "reply_to", reply_to)
        if time_range is not None:
            warnings.warn("""Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""", DeprecationWarning)
            pulumi.log.warn("""time_range is deprecated: Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""")
        if time_range is not None:
            pulumi.set(__self__, "time_range", time_range)

    @property
    @pulumi.getter
    def recipients(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of recipients of the report.
        """
        return pulumi.get(self, "recipients")

    @recipients.setter
    def recipients(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "recipients", value)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input['ReportScheduleArgs']:
        """
        Schedule of the report.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input['ReportScheduleArgs']):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        Dashboard to be sent in the report.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_uid is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter
    def dashboards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]]:
        """
        List of dashboards to render into the report
        """
        return pulumi.get(self, "dashboards")

    @dashboards.setter
    def dashboards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]]):
        pulumi.set(self, "dashboards", value)

    @property
    @pulumi.getter
    def formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        """
        return pulumi.get(self, "formats")

    @formats.setter
    def formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "formats", value)

    @property
    @pulumi.getter(name="includeDashboardLink")
    def include_dashboard_link(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to include a link to the dashboard in the report.
        """
        return pulumi.get(self, "include_dashboard_link")

    @include_dashboard_link.setter
    def include_dashboard_link(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_dashboard_link", value)

    @property
    @pulumi.getter(name="includeTableCsv")
    def include_table_csv(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to include a CSV file of table panel data.
        """
        return pulumi.get(self, "include_table_csv")

    @include_table_csv.setter
    def include_table_csv(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_table_csv", value)

    @property
    @pulumi.getter
    def layout(self) -> Optional[pulumi.Input[str]]:
        """
        Layout of the report. Allowed values: `simple`, `grid`.
        """
        return pulumi.get(self, "layout")

    @layout.setter
    def layout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "layout", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Message to be sent in the report.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the report.
        """
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
    def orientation(self) -> Optional[pulumi.Input[str]]:
        """
        Orientation of the report. Allowed values: `landscape`, `portrait`.
        """
        return pulumi.get(self, "orientation")

    @orientation.setter
    def orientation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "orientation", value)

    @property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[str]]:
        """
        Reply-to email address of the report.
        """
        return pulumi.get(self, "reply_to")

    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to", value)

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[pulumi.Input['ReportTimeRangeArgs']]:
        """
        Time range of the report.
        """
        warnings.warn("""Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""", DeprecationWarning)
        pulumi.log.warn("""time_range is deprecated: Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""")

        return pulumi.get(self, "time_range")

    @time_range.setter
    def time_range(self, value: Optional[pulumi.Input['ReportTimeRangeArgs']]):
        pulumi.set(self, "time_range", value)


@pulumi.input_type
class _ReportState:
    def __init__(__self__, *,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 dashboards: Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]] = None,
                 formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 include_dashboard_link: Optional[pulumi.Input[bool]] = None,
                 include_table_csv: Optional[pulumi.Input[bool]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 orientation: Optional[pulumi.Input[str]] = None,
                 recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 reply_to: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['ReportScheduleArgs']] = None,
                 time_range: Optional[pulumi.Input['ReportTimeRangeArgs']] = None):
        """
        Input properties used for looking up and filtering Report resources.
        :param pulumi.Input[int] dashboard_id: Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: Dashboard to be sent in the report.
        :param pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]] dashboards: List of dashboards to render into the report
        :param pulumi.Input[Sequence[pulumi.Input[str]]] formats: Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        :param pulumi.Input[bool] include_dashboard_link: Whether to include a link to the dashboard in the report.
        :param pulumi.Input[bool] include_table_csv: Whether to include a CSV file of table panel data.
        :param pulumi.Input[str] layout: Layout of the report. Allowed values: `simple`, `grid`.
        :param pulumi.Input[str] message: Message to be sent in the report.
        :param pulumi.Input[str] name: Name of the report.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] orientation: Orientation of the report. Allowed values: `landscape`, `portrait`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] recipients: List of recipients of the report.
        :param pulumi.Input[str] reply_to: Reply-to email address of the report.
        :param pulumi.Input['ReportScheduleArgs'] schedule: Schedule of the report.
        :param pulumi.Input['ReportTimeRangeArgs'] time_range: Time range of the report.
        """
        if dashboard_id is not None:
            warnings.warn("""Use dashboards instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: Use dashboards instead""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            warnings.warn("""Use dashboards instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_uid is deprecated: Use dashboards instead""")
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if dashboards is not None:
            pulumi.set(__self__, "dashboards", dashboards)
        if formats is not None:
            pulumi.set(__self__, "formats", formats)
        if include_dashboard_link is not None:
            pulumi.set(__self__, "include_dashboard_link", include_dashboard_link)
        if include_table_csv is not None:
            pulumi.set(__self__, "include_table_csv", include_table_csv)
        if layout is not None:
            pulumi.set(__self__, "layout", layout)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if orientation is not None:
            pulumi.set(__self__, "orientation", orientation)
        if recipients is not None:
            pulumi.set(__self__, "recipients", recipients)
        if reply_to is not None:
            pulumi.set(__self__, "reply_to", reply_to)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if time_range is not None:
            warnings.warn("""Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""", DeprecationWarning)
            pulumi.log.warn("""time_range is deprecated: Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""")
        if time_range is not None:
            pulumi.set(__self__, "time_range", time_range)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        Dashboard to be sent in the report.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_uid is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter
    def dashboards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]]:
        """
        List of dashboards to render into the report
        """
        return pulumi.get(self, "dashboards")

    @dashboards.setter
    def dashboards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportDashboardArgs']]]]):
        pulumi.set(self, "dashboards", value)

    @property
    @pulumi.getter
    def formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        """
        return pulumi.get(self, "formats")

    @formats.setter
    def formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "formats", value)

    @property
    @pulumi.getter(name="includeDashboardLink")
    def include_dashboard_link(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to include a link to the dashboard in the report.
        """
        return pulumi.get(self, "include_dashboard_link")

    @include_dashboard_link.setter
    def include_dashboard_link(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_dashboard_link", value)

    @property
    @pulumi.getter(name="includeTableCsv")
    def include_table_csv(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to include a CSV file of table panel data.
        """
        return pulumi.get(self, "include_table_csv")

    @include_table_csv.setter
    def include_table_csv(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_table_csv", value)

    @property
    @pulumi.getter
    def layout(self) -> Optional[pulumi.Input[str]]:
        """
        Layout of the report. Allowed values: `simple`, `grid`.
        """
        return pulumi.get(self, "layout")

    @layout.setter
    def layout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "layout", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Message to be sent in the report.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the report.
        """
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
    def orientation(self) -> Optional[pulumi.Input[str]]:
        """
        Orientation of the report. Allowed values: `landscape`, `portrait`.
        """
        return pulumi.get(self, "orientation")

    @orientation.setter
    def orientation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "orientation", value)

    @property
    @pulumi.getter
    def recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of recipients of the report.
        """
        return pulumi.get(self, "recipients")

    @recipients.setter
    def recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "recipients", value)

    @property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[str]]:
        """
        Reply-to email address of the report.
        """
        return pulumi.get(self, "reply_to")

    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ReportScheduleArgs']]:
        """
        Schedule of the report.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ReportScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[pulumi.Input['ReportTimeRangeArgs']]:
        """
        Time range of the report.
        """
        warnings.warn("""Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""", DeprecationWarning)
        pulumi.log.warn("""time_range is deprecated: Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""")

        return pulumi.get(self, "time_range")

    @time_range.setter
    def time_range(self, value: Optional[pulumi.Input['ReportTimeRangeArgs']]):
        pulumi.set(self, "time_range", value)


class Report(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportDashboardArgs']]]]] = None,
                 formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 include_dashboard_link: Optional[pulumi.Input[bool]] = None,
                 include_table_csv: Optional[pulumi.Input[bool]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 orientation: Optional[pulumi.Input[str]] = None,
                 recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 reply_to: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
                 time_range: Optional[pulumi.Input[pulumi.InputType['ReportTimeRangeArgs']]] = None,
                 __props__=None):
        """
        Create a Report resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: Dashboard to be sent in the report.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportDashboardArgs']]]] dashboards: List of dashboards to render into the report
        :param pulumi.Input[Sequence[pulumi.Input[str]]] formats: Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        :param pulumi.Input[bool] include_dashboard_link: Whether to include a link to the dashboard in the report.
        :param pulumi.Input[bool] include_table_csv: Whether to include a CSV file of table panel data.
        :param pulumi.Input[str] layout: Layout of the report. Allowed values: `simple`, `grid`.
        :param pulumi.Input[str] message: Message to be sent in the report.
        :param pulumi.Input[str] name: Name of the report.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] orientation: Orientation of the report. Allowed values: `landscape`, `portrait`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] recipients: List of recipients of the report.
        :param pulumi.Input[str] reply_to: Reply-to email address of the report.
        :param pulumi.Input[pulumi.InputType['ReportScheduleArgs']] schedule: Schedule of the report.
        :param pulumi.Input[pulumi.InputType['ReportTimeRangeArgs']] time_range: Time range of the report.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Report resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ReportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportDashboardArgs']]]]] = None,
                 formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 include_dashboard_link: Optional[pulumi.Input[bool]] = None,
                 include_table_csv: Optional[pulumi.Input[bool]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 orientation: Optional[pulumi.Input[str]] = None,
                 recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 reply_to: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
                 time_range: Optional[pulumi.Input[pulumi.InputType['ReportTimeRangeArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReportArgs.__new__(ReportArgs)

            __props__.__dict__["dashboard_id"] = dashboard_id
            __props__.__dict__["dashboard_uid"] = dashboard_uid
            __props__.__dict__["dashboards"] = dashboards
            __props__.__dict__["formats"] = formats
            __props__.__dict__["include_dashboard_link"] = include_dashboard_link
            __props__.__dict__["include_table_csv"] = include_table_csv
            __props__.__dict__["layout"] = layout
            __props__.__dict__["message"] = message
            __props__.__dict__["name"] = name
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["orientation"] = orientation
            if recipients is None and not opts.urn:
                raise TypeError("Missing required property 'recipients'")
            __props__.__dict__["recipients"] = recipients
            __props__.__dict__["reply_to"] = reply_to
            if schedule is None and not opts.urn:
                raise TypeError("Missing required property 'schedule'")
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["time_range"] = time_range
        super(Report, __self__).__init__(
            'grafana:index/report:Report',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_id: Optional[pulumi.Input[int]] = None,
            dashboard_uid: Optional[pulumi.Input[str]] = None,
            dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportDashboardArgs']]]]] = None,
            formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            include_dashboard_link: Optional[pulumi.Input[bool]] = None,
            include_table_csv: Optional[pulumi.Input[bool]] = None,
            layout: Optional[pulumi.Input[str]] = None,
            message: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            orientation: Optional[pulumi.Input[str]] = None,
            recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            reply_to: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
            time_range: Optional[pulumi.Input[pulumi.InputType['ReportTimeRangeArgs']]] = None) -> 'Report':
        """
        Get an existing Report resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: Dashboard to be sent in the report.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportDashboardArgs']]]] dashboards: List of dashboards to render into the report
        :param pulumi.Input[Sequence[pulumi.Input[str]]] formats: Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        :param pulumi.Input[bool] include_dashboard_link: Whether to include a link to the dashboard in the report.
        :param pulumi.Input[bool] include_table_csv: Whether to include a CSV file of table panel data.
        :param pulumi.Input[str] layout: Layout of the report. Allowed values: `simple`, `grid`.
        :param pulumi.Input[str] message: Message to be sent in the report.
        :param pulumi.Input[str] name: Name of the report.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] orientation: Orientation of the report. Allowed values: `landscape`, `portrait`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] recipients: List of recipients of the report.
        :param pulumi.Input[str] reply_to: Reply-to email address of the report.
        :param pulumi.Input[pulumi.InputType['ReportScheduleArgs']] schedule: Schedule of the report.
        :param pulumi.Input[pulumi.InputType['ReportTimeRangeArgs']] time_range: Time range of the report.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReportState.__new__(_ReportState)

        __props__.__dict__["dashboard_id"] = dashboard_id
        __props__.__dict__["dashboard_uid"] = dashboard_uid
        __props__.__dict__["dashboards"] = dashboards
        __props__.__dict__["formats"] = formats
        __props__.__dict__["include_dashboard_link"] = include_dashboard_link
        __props__.__dict__["include_table_csv"] = include_table_csv
        __props__.__dict__["layout"] = layout
        __props__.__dict__["message"] = message
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["orientation"] = orientation
        __props__.__dict__["recipients"] = recipients
        __props__.__dict__["reply_to"] = reply_to
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["time_range"] = time_range
        return Report(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> pulumi.Output[int]:
        """
        Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_id")

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> pulumi.Output[str]:
        """
        Dashboard to be sent in the report.
        """
        warnings.warn("""Use dashboards instead""", DeprecationWarning)
        pulumi.log.warn("""dashboard_uid is deprecated: Use dashboards instead""")

        return pulumi.get(self, "dashboard_uid")

    @property
    @pulumi.getter
    def dashboards(self) -> pulumi.Output[Optional[Sequence['outputs.ReportDashboard']]]:
        """
        List of dashboards to render into the report
        """
        return pulumi.get(self, "dashboards")

    @property
    @pulumi.getter
    def formats(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        """
        return pulumi.get(self, "formats")

    @property
    @pulumi.getter(name="includeDashboardLink")
    def include_dashboard_link(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to include a link to the dashboard in the report.
        """
        return pulumi.get(self, "include_dashboard_link")

    @property
    @pulumi.getter(name="includeTableCsv")
    def include_table_csv(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to include a CSV file of table panel data.
        """
        return pulumi.get(self, "include_table_csv")

    @property
    @pulumi.getter
    def layout(self) -> pulumi.Output[Optional[str]]:
        """
        Layout of the report. Allowed values: `simple`, `grid`.
        """
        return pulumi.get(self, "layout")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        Message to be sent in the report.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the report.
        """
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
    def orientation(self) -> pulumi.Output[Optional[str]]:
        """
        Orientation of the report. Allowed values: `landscape`, `portrait`.
        """
        return pulumi.get(self, "orientation")

    @property
    @pulumi.getter
    def recipients(self) -> pulumi.Output[Sequence[str]]:
        """
        List of recipients of the report.
        """
        return pulumi.get(self, "recipients")

    @property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> pulumi.Output[Optional[str]]:
        """
        Reply-to email address of the report.
        """
        return pulumi.get(self, "reply_to")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.ReportSchedule']:
        """
        Schedule of the report.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Output[Optional['outputs.ReportTimeRange']]:
        """
        Time range of the report.
        """
        warnings.warn("""Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""", DeprecationWarning)
        pulumi.log.warn("""time_range is deprecated: Use time_range in dashboards instead. This field is completely ignored when dashboards is set.""")

        return pulumi.get(self, "time_range")

