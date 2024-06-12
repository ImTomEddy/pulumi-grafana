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
    'GetCloudStackResult',
    'AwaitableGetCloudStackResult',
    'get_cloud_stack',
    'get_cloud_stack_output',
]

@pulumi.output_type
class GetCloudStackResult:
    """
    A collection of values returned by getCloudStack.
    """
    def __init__(__self__, alertmanager_name=None, alertmanager_status=None, alertmanager_url=None, alertmanager_user_id=None, description=None, graphite_name=None, graphite_status=None, graphite_url=None, graphite_user_id=None, id=None, labels=None, logs_name=None, logs_status=None, logs_url=None, logs_user_id=None, name=None, org_id=None, org_name=None, org_slug=None, otlp_url=None, profiles_name=None, profiles_status=None, profiles_url=None, profiles_user_id=None, prometheus_name=None, prometheus_remote_endpoint=None, prometheus_remote_write_endpoint=None, prometheus_status=None, prometheus_url=None, prometheus_user_id=None, region_slug=None, slug=None, status=None, traces_name=None, traces_status=None, traces_url=None, traces_user_id=None, url=None):
        if alertmanager_name and not isinstance(alertmanager_name, str):
            raise TypeError("Expected argument 'alertmanager_name' to be a str")
        pulumi.set(__self__, "alertmanager_name", alertmanager_name)
        if alertmanager_status and not isinstance(alertmanager_status, str):
            raise TypeError("Expected argument 'alertmanager_status' to be a str")
        pulumi.set(__self__, "alertmanager_status", alertmanager_status)
        if alertmanager_url and not isinstance(alertmanager_url, str):
            raise TypeError("Expected argument 'alertmanager_url' to be a str")
        pulumi.set(__self__, "alertmanager_url", alertmanager_url)
        if alertmanager_user_id and not isinstance(alertmanager_user_id, int):
            raise TypeError("Expected argument 'alertmanager_user_id' to be a int")
        pulumi.set(__self__, "alertmanager_user_id", alertmanager_user_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if graphite_name and not isinstance(graphite_name, str):
            raise TypeError("Expected argument 'graphite_name' to be a str")
        pulumi.set(__self__, "graphite_name", graphite_name)
        if graphite_status and not isinstance(graphite_status, str):
            raise TypeError("Expected argument 'graphite_status' to be a str")
        pulumi.set(__self__, "graphite_status", graphite_status)
        if graphite_url and not isinstance(graphite_url, str):
            raise TypeError("Expected argument 'graphite_url' to be a str")
        pulumi.set(__self__, "graphite_url", graphite_url)
        if graphite_user_id and not isinstance(graphite_user_id, int):
            raise TypeError("Expected argument 'graphite_user_id' to be a int")
        pulumi.set(__self__, "graphite_user_id", graphite_user_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if logs_name and not isinstance(logs_name, str):
            raise TypeError("Expected argument 'logs_name' to be a str")
        pulumi.set(__self__, "logs_name", logs_name)
        if logs_status and not isinstance(logs_status, str):
            raise TypeError("Expected argument 'logs_status' to be a str")
        pulumi.set(__self__, "logs_status", logs_status)
        if logs_url and not isinstance(logs_url, str):
            raise TypeError("Expected argument 'logs_url' to be a str")
        pulumi.set(__self__, "logs_url", logs_url)
        if logs_user_id and not isinstance(logs_user_id, int):
            raise TypeError("Expected argument 'logs_user_id' to be a int")
        pulumi.set(__self__, "logs_user_id", logs_user_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if org_id and not isinstance(org_id, int):
            raise TypeError("Expected argument 'org_id' to be a int")
        pulumi.set(__self__, "org_id", org_id)
        if org_name and not isinstance(org_name, str):
            raise TypeError("Expected argument 'org_name' to be a str")
        pulumi.set(__self__, "org_name", org_name)
        if org_slug and not isinstance(org_slug, str):
            raise TypeError("Expected argument 'org_slug' to be a str")
        pulumi.set(__self__, "org_slug", org_slug)
        if otlp_url and not isinstance(otlp_url, str):
            raise TypeError("Expected argument 'otlp_url' to be a str")
        pulumi.set(__self__, "otlp_url", otlp_url)
        if profiles_name and not isinstance(profiles_name, str):
            raise TypeError("Expected argument 'profiles_name' to be a str")
        pulumi.set(__self__, "profiles_name", profiles_name)
        if profiles_status and not isinstance(profiles_status, str):
            raise TypeError("Expected argument 'profiles_status' to be a str")
        pulumi.set(__self__, "profiles_status", profiles_status)
        if profiles_url and not isinstance(profiles_url, str):
            raise TypeError("Expected argument 'profiles_url' to be a str")
        pulumi.set(__self__, "profiles_url", profiles_url)
        if profiles_user_id and not isinstance(profiles_user_id, int):
            raise TypeError("Expected argument 'profiles_user_id' to be a int")
        pulumi.set(__self__, "profiles_user_id", profiles_user_id)
        if prometheus_name and not isinstance(prometheus_name, str):
            raise TypeError("Expected argument 'prometheus_name' to be a str")
        pulumi.set(__self__, "prometheus_name", prometheus_name)
        if prometheus_remote_endpoint and not isinstance(prometheus_remote_endpoint, str):
            raise TypeError("Expected argument 'prometheus_remote_endpoint' to be a str")
        pulumi.set(__self__, "prometheus_remote_endpoint", prometheus_remote_endpoint)
        if prometheus_remote_write_endpoint and not isinstance(prometheus_remote_write_endpoint, str):
            raise TypeError("Expected argument 'prometheus_remote_write_endpoint' to be a str")
        pulumi.set(__self__, "prometheus_remote_write_endpoint", prometheus_remote_write_endpoint)
        if prometheus_status and not isinstance(prometheus_status, str):
            raise TypeError("Expected argument 'prometheus_status' to be a str")
        pulumi.set(__self__, "prometheus_status", prometheus_status)
        if prometheus_url and not isinstance(prometheus_url, str):
            raise TypeError("Expected argument 'prometheus_url' to be a str")
        pulumi.set(__self__, "prometheus_url", prometheus_url)
        if prometheus_user_id and not isinstance(prometheus_user_id, int):
            raise TypeError("Expected argument 'prometheus_user_id' to be a int")
        pulumi.set(__self__, "prometheus_user_id", prometheus_user_id)
        if region_slug and not isinstance(region_slug, str):
            raise TypeError("Expected argument 'region_slug' to be a str")
        pulumi.set(__self__, "region_slug", region_slug)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if traces_name and not isinstance(traces_name, str):
            raise TypeError("Expected argument 'traces_name' to be a str")
        pulumi.set(__self__, "traces_name", traces_name)
        if traces_status and not isinstance(traces_status, str):
            raise TypeError("Expected argument 'traces_status' to be a str")
        pulumi.set(__self__, "traces_status", traces_status)
        if traces_url and not isinstance(traces_url, str):
            raise TypeError("Expected argument 'traces_url' to be a str")
        pulumi.set(__self__, "traces_url", traces_url)
        if traces_user_id and not isinstance(traces_user_id, int):
            raise TypeError("Expected argument 'traces_user_id' to be a int")
        pulumi.set(__self__, "traces_user_id", traces_user_id)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="alertmanagerName")
    def alertmanager_name(self) -> str:
        """
        Name of the Alertmanager instance configured for this stack.
        """
        return pulumi.get(self, "alertmanager_name")

    @property
    @pulumi.getter(name="alertmanagerStatus")
    def alertmanager_status(self) -> str:
        """
        Status of the Alertmanager instance configured for this stack.
        """
        return pulumi.get(self, "alertmanager_status")

    @property
    @pulumi.getter(name="alertmanagerUrl")
    def alertmanager_url(self) -> str:
        """
        Base URL of the Alertmanager instance configured for this stack.
        """
        return pulumi.get(self, "alertmanager_url")

    @property
    @pulumi.getter(name="alertmanagerUserId")
    def alertmanager_user_id(self) -> int:
        """
        User ID of the Alertmanager instance configured for this stack.
        """
        return pulumi.get(self, "alertmanager_user_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of stack.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="graphiteName")
    def graphite_name(self) -> str:
        return pulumi.get(self, "graphite_name")

    @property
    @pulumi.getter(name="graphiteStatus")
    def graphite_status(self) -> str:
        return pulumi.get(self, "graphite_status")

    @property
    @pulumi.getter(name="graphiteUrl")
    def graphite_url(self) -> str:
        return pulumi.get(self, "graphite_url")

    @property
    @pulumi.getter(name="graphiteUserId")
    def graphite_user_id(self) -> int:
        return pulumi.get(self, "graphite_user_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The stack id assigned to this stack by Grafana.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        A map of labels to assign to the stack. Label keys and values must match the following regexp: "^[a-zA-Z0-9/\\-.]+$" and stacks cannot have more than 10 labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="logsName")
    def logs_name(self) -> str:
        return pulumi.get(self, "logs_name")

    @property
    @pulumi.getter(name="logsStatus")
    def logs_status(self) -> str:
        return pulumi.get(self, "logs_status")

    @property
    @pulumi.getter(name="logsUrl")
    def logs_url(self) -> str:
        return pulumi.get(self, "logs_url")

    @property
    @pulumi.getter(name="logsUserId")
    def logs_user_id(self) -> int:
        return pulumi.get(self, "logs_user_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of stack. Conventionally matches the url of the instance (e.g. `<stack_slug>.grafana.net`).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> int:
        """
        Organization id to assign to this stack.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> str:
        """
        Organization name to assign to this stack.
        """
        return pulumi.get(self, "org_name")

    @property
    @pulumi.getter(name="orgSlug")
    def org_slug(self) -> str:
        """
        Organization slug to assign to this stack.
        """
        return pulumi.get(self, "org_slug")

    @property
    @pulumi.getter(name="otlpUrl")
    def otlp_url(self) -> str:
        """
        Base URL of the OTLP instance configured for this stack. See https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/ for docs on how to use this.
        """
        return pulumi.get(self, "otlp_url")

    @property
    @pulumi.getter(name="profilesName")
    def profiles_name(self) -> str:
        return pulumi.get(self, "profiles_name")

    @property
    @pulumi.getter(name="profilesStatus")
    def profiles_status(self) -> str:
        return pulumi.get(self, "profiles_status")

    @property
    @pulumi.getter(name="profilesUrl")
    def profiles_url(self) -> str:
        return pulumi.get(self, "profiles_url")

    @property
    @pulumi.getter(name="profilesUserId")
    def profiles_user_id(self) -> int:
        return pulumi.get(self, "profiles_user_id")

    @property
    @pulumi.getter(name="prometheusName")
    def prometheus_name(self) -> str:
        """
        Prometheus name for this instance.
        """
        return pulumi.get(self, "prometheus_name")

    @property
    @pulumi.getter(name="prometheusRemoteEndpoint")
    def prometheus_remote_endpoint(self) -> str:
        """
        Use this URL to query hosted metrics data e.g. Prometheus data source in Grafana
        """
        return pulumi.get(self, "prometheus_remote_endpoint")

    @property
    @pulumi.getter(name="prometheusRemoteWriteEndpoint")
    def prometheus_remote_write_endpoint(self) -> str:
        """
        Use this URL to send prometheus metrics to Grafana cloud
        """
        return pulumi.get(self, "prometheus_remote_write_endpoint")

    @property
    @pulumi.getter(name="prometheusStatus")
    def prometheus_status(self) -> str:
        """
        Prometheus status for this instance.
        """
        return pulumi.get(self, "prometheus_status")

    @property
    @pulumi.getter(name="prometheusUrl")
    def prometheus_url(self) -> str:
        """
        Prometheus url for this instance.
        """
        return pulumi.get(self, "prometheus_url")

    @property
    @pulumi.getter(name="prometheusUserId")
    def prometheus_user_id(self) -> int:
        """
        Prometheus user ID. Used for e.g. remote_write.
        """
        return pulumi.get(self, "prometheus_user_id")

    @property
    @pulumi.getter(name="regionSlug")
    def region_slug(self) -> str:
        """
        The region this stack is deployed to.
        """
        return pulumi.get(self, "region_slug")

    @property
    @pulumi.getter
    def slug(self) -> str:
        """
        Subdomain that the Grafana instance will be available at (i.e. setting slug to “\\n\\n” will make the instance
        available at “https://\\n\\n.grafana.net".
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the stack.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="tracesName")
    def traces_name(self) -> str:
        return pulumi.get(self, "traces_name")

    @property
    @pulumi.getter(name="tracesStatus")
    def traces_status(self) -> str:
        return pulumi.get(self, "traces_status")

    @property
    @pulumi.getter(name="tracesUrl")
    def traces_url(self) -> str:
        """
        Base URL of the Traces instance configured for this stack. To use this in the Tempo data source in Grafana, append `/tempo` to the URL.
        """
        return pulumi.get(self, "traces_url")

    @property
    @pulumi.getter(name="tracesUserId")
    def traces_user_id(self) -> int:
        return pulumi.get(self, "traces_user_id")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        Custom URL for the Grafana instance. Must have a CNAME setup to point to `.grafana.net` before creating the stack
        """
        return pulumi.get(self, "url")


class AwaitableGetCloudStackResult(GetCloudStackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudStackResult(
            alertmanager_name=self.alertmanager_name,
            alertmanager_status=self.alertmanager_status,
            alertmanager_url=self.alertmanager_url,
            alertmanager_user_id=self.alertmanager_user_id,
            description=self.description,
            graphite_name=self.graphite_name,
            graphite_status=self.graphite_status,
            graphite_url=self.graphite_url,
            graphite_user_id=self.graphite_user_id,
            id=self.id,
            labels=self.labels,
            logs_name=self.logs_name,
            logs_status=self.logs_status,
            logs_url=self.logs_url,
            logs_user_id=self.logs_user_id,
            name=self.name,
            org_id=self.org_id,
            org_name=self.org_name,
            org_slug=self.org_slug,
            otlp_url=self.otlp_url,
            profiles_name=self.profiles_name,
            profiles_status=self.profiles_status,
            profiles_url=self.profiles_url,
            profiles_user_id=self.profiles_user_id,
            prometheus_name=self.prometheus_name,
            prometheus_remote_endpoint=self.prometheus_remote_endpoint,
            prometheus_remote_write_endpoint=self.prometheus_remote_write_endpoint,
            prometheus_status=self.prometheus_status,
            prometheus_url=self.prometheus_url,
            prometheus_user_id=self.prometheus_user_id,
            region_slug=self.region_slug,
            slug=self.slug,
            status=self.status,
            traces_name=self.traces_name,
            traces_status=self.traces_status,
            traces_url=self.traces_url,
            traces_user_id=self.traces_user_id,
            url=self.url)


def get_cloud_stack(slug: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudStackResult:
    """
    Data source for Grafana Stack


    :param str slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “\\n\\n” will make the instance
           available at “https://\\n\\n.grafana.net".
    """
    __args__ = dict()
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getCloudStack:getCloudStack', __args__, opts=opts, typ=GetCloudStackResult).value

    return AwaitableGetCloudStackResult(
        alertmanager_name=pulumi.get(__ret__, 'alertmanager_name'),
        alertmanager_status=pulumi.get(__ret__, 'alertmanager_status'),
        alertmanager_url=pulumi.get(__ret__, 'alertmanager_url'),
        alertmanager_user_id=pulumi.get(__ret__, 'alertmanager_user_id'),
        description=pulumi.get(__ret__, 'description'),
        graphite_name=pulumi.get(__ret__, 'graphite_name'),
        graphite_status=pulumi.get(__ret__, 'graphite_status'),
        graphite_url=pulumi.get(__ret__, 'graphite_url'),
        graphite_user_id=pulumi.get(__ret__, 'graphite_user_id'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        logs_name=pulumi.get(__ret__, 'logs_name'),
        logs_status=pulumi.get(__ret__, 'logs_status'),
        logs_url=pulumi.get(__ret__, 'logs_url'),
        logs_user_id=pulumi.get(__ret__, 'logs_user_id'),
        name=pulumi.get(__ret__, 'name'),
        org_id=pulumi.get(__ret__, 'org_id'),
        org_name=pulumi.get(__ret__, 'org_name'),
        org_slug=pulumi.get(__ret__, 'org_slug'),
        otlp_url=pulumi.get(__ret__, 'otlp_url'),
        profiles_name=pulumi.get(__ret__, 'profiles_name'),
        profiles_status=pulumi.get(__ret__, 'profiles_status'),
        profiles_url=pulumi.get(__ret__, 'profiles_url'),
        profiles_user_id=pulumi.get(__ret__, 'profiles_user_id'),
        prometheus_name=pulumi.get(__ret__, 'prometheus_name'),
        prometheus_remote_endpoint=pulumi.get(__ret__, 'prometheus_remote_endpoint'),
        prometheus_remote_write_endpoint=pulumi.get(__ret__, 'prometheus_remote_write_endpoint'),
        prometheus_status=pulumi.get(__ret__, 'prometheus_status'),
        prometheus_url=pulumi.get(__ret__, 'prometheus_url'),
        prometheus_user_id=pulumi.get(__ret__, 'prometheus_user_id'),
        region_slug=pulumi.get(__ret__, 'region_slug'),
        slug=pulumi.get(__ret__, 'slug'),
        status=pulumi.get(__ret__, 'status'),
        traces_name=pulumi.get(__ret__, 'traces_name'),
        traces_status=pulumi.get(__ret__, 'traces_status'),
        traces_url=pulumi.get(__ret__, 'traces_url'),
        traces_user_id=pulumi.get(__ret__, 'traces_user_id'),
        url=pulumi.get(__ret__, 'url'))


@_utilities.lift_output_func(get_cloud_stack)
def get_cloud_stack_output(slug: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudStackResult]:
    """
    Data source for Grafana Stack


    :param str slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “\\n\\n” will make the instance
           available at “https://\\n\\n.grafana.net".
    """
    ...
