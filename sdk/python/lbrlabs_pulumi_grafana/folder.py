# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FolderArgs', 'Folder']

@pulumi.input_type
class FolderArgs:
    def __init__(__self__, *,
                 title: pulumi.Input[str],
                 prevent_destroy_if_not_empty: Optional[pulumi.Input[bool]] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Folder resource.
        :param pulumi.Input[str] title: The title of the folder.
        :param pulumi.Input[bool] prevent_destroy_if_not_empty: Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        :param pulumi.Input[str] uid: Unique identifier.
        """
        pulumi.set(__self__, "title", title)
        if prevent_destroy_if_not_empty is not None:
            pulumi.set(__self__, "prevent_destroy_if_not_empty", prevent_destroy_if_not_empty)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the folder.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="preventDestroyIfNotEmpty")
    def prevent_destroy_if_not_empty(self) -> Optional[pulumi.Input[bool]]:
        """
        Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        """
        return pulumi.get(self, "prevent_destroy_if_not_empty")

    @prevent_destroy_if_not_empty.setter
    def prevent_destroy_if_not_empty(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prevent_destroy_if_not_empty", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


@pulumi.input_type
class _FolderState:
    def __init__(__self__, *,
                 prevent_destroy_if_not_empty: Optional[pulumi.Input[bool]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Folder resources.
        :param pulumi.Input[bool] prevent_destroy_if_not_empty: Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        :param pulumi.Input[str] title: The title of the folder.
        :param pulumi.Input[str] uid: Unique identifier.
        :param pulumi.Input[str] url: The full URL of the folder.
        """
        if prevent_destroy_if_not_empty is not None:
            pulumi.set(__self__, "prevent_destroy_if_not_empty", prevent_destroy_if_not_empty)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="preventDestroyIfNotEmpty")
    def prevent_destroy_if_not_empty(self) -> Optional[pulumi.Input[bool]]:
        """
        Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        """
        return pulumi.get(self, "prevent_destroy_if_not_empty")

    @prevent_destroy_if_not_empty.setter
    def prevent_destroy_if_not_empty(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prevent_destroy_if_not_empty", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the folder.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The full URL of the folder.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Folder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 prevent_destroy_if_not_empty: Optional[pulumi.Input[bool]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        test_folder_folder = grafana.Folder("testFolderFolder", title="Terraform Test Folder")
        test_folder_dashboard = grafana.Dashboard("testFolderDashboard",
            folder=test_folder_folder.id,
            config_json=\"\"\"{
          "title": "Dashboard in folder",
          "uid": "dashboard-in-folder"
        }
        \"\"\")
        test_folder_with_uid = grafana.Folder("testFolderWithUid",
            uid="test-folder-uid",
            title="Terraform Test Folder With UID")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/folder:Folder by_integer_id {{folder_id}}
        ```

        ```sh
         $ pulumi import grafana:index/folder:Folder by_uid {{folder_uid}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] prevent_destroy_if_not_empty: Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        :param pulumi.Input[str] title: The title of the folder.
        :param pulumi.Input[str] uid: Unique identifier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        test_folder_folder = grafana.Folder("testFolderFolder", title="Terraform Test Folder")
        test_folder_dashboard = grafana.Dashboard("testFolderDashboard",
            folder=test_folder_folder.id,
            config_json=\"\"\"{
          "title": "Dashboard in folder",
          "uid": "dashboard-in-folder"
        }
        \"\"\")
        test_folder_with_uid = grafana.Folder("testFolderWithUid",
            uid="test-folder-uid",
            title="Terraform Test Folder With UID")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/folder:Folder by_integer_id {{folder_id}}
        ```

        ```sh
         $ pulumi import grafana:index/folder:Folder by_uid {{folder_uid}}
        ```

        :param str resource_name: The name of the resource.
        :param FolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 prevent_destroy_if_not_empty: Optional[pulumi.Input[bool]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FolderArgs.__new__(FolderArgs)

            __props__.__dict__["prevent_destroy_if_not_empty"] = prevent_destroy_if_not_empty
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["uid"] = uid
            __props__.__dict__["url"] = None
        super(Folder, __self__).__init__(
            'grafana:index/folder:Folder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            prevent_destroy_if_not_empty: Optional[pulumi.Input[bool]] = None,
            title: Optional[pulumi.Input[str]] = None,
            uid: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Folder':
        """
        Get an existing Folder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] prevent_destroy_if_not_empty: Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        :param pulumi.Input[str] title: The title of the folder.
        :param pulumi.Input[str] uid: Unique identifier.
        :param pulumi.Input[str] url: The full URL of the folder.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FolderState.__new__(_FolderState)

        __props__.__dict__["prevent_destroy_if_not_empty"] = prevent_destroy_if_not_empty
        __props__.__dict__["title"] = title
        __props__.__dict__["uid"] = uid
        __props__.__dict__["url"] = url
        return Folder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="preventDestroyIfNotEmpty")
    def prevent_destroy_if_not_empty(self) -> pulumi.Output[Optional[bool]]:
        """
        Prevent deletion of the folder if it is not empty (contains dashboards or alert rules). Defaults to `false`.
        """
        return pulumi.get(self, "prevent_destroy_if_not_empty")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the folder.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Unique identifier.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The full URL of the folder.
        """
        return pulumi.get(self, "url")

