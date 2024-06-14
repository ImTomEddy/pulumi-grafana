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

__all__ = ['TeamArgs', 'Team']

@pulumi.input_type
class TeamArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 ignore_externally_synced_members: Optional[pulumi.Input[bool]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 preferences: Optional[pulumi.Input['TeamPreferencesArgs']] = None,
                 team_sync: Optional[pulumi.Input['TeamTeamSyncArgs']] = None):
        """
        The set of arguments for constructing a Team resource.
        :param pulumi.Input[str] email: An email address for the team.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
               must already exist in Grafana.
        :param pulumi.Input[str] name: The display name for the Grafana team created.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input['TeamTeamSyncArgs'] team_sync: Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
               documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
               API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if ignore_externally_synced_members is not None:
            pulumi.set(__self__, "ignore_externally_synced_members", ignore_externally_synced_members)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if preferences is not None:
            pulumi.set(__self__, "preferences", preferences)
        if team_sync is not None:
            pulumi.set(__self__, "team_sync", team_sync)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address for the team.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="ignoreExternallySyncedMembers")
    def ignore_externally_synced_members(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ignore_externally_synced_members")

    @ignore_externally_synced_members.setter
    def ignore_externally_synced_members(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_externally_synced_members", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
        must already exist in Grafana.
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the Grafana team created.
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
    def preferences(self) -> Optional[pulumi.Input['TeamPreferencesArgs']]:
        return pulumi.get(self, "preferences")

    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input['TeamPreferencesArgs']]):
        pulumi.set(self, "preferences", value)

    @property
    @pulumi.getter(name="teamSync")
    def team_sync(self) -> Optional[pulumi.Input['TeamTeamSyncArgs']]:
        """
        Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
        documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
        API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        return pulumi.get(self, "team_sync")

    @team_sync.setter
    def team_sync(self, value: Optional[pulumi.Input['TeamTeamSyncArgs']]):
        pulumi.set(self, "team_sync", value)


@pulumi.input_type
class _TeamState:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 ignore_externally_synced_members: Optional[pulumi.Input[bool]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 preferences: Optional[pulumi.Input['TeamPreferencesArgs']] = None,
                 team_id: Optional[pulumi.Input[int]] = None,
                 team_sync: Optional[pulumi.Input['TeamTeamSyncArgs']] = None):
        """
        Input properties used for looking up and filtering Team resources.
        :param pulumi.Input[str] email: An email address for the team.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
               must already exist in Grafana.
        :param pulumi.Input[str] name: The display name for the Grafana team created.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] team_id: The team id assigned to this team by Grafana.
        :param pulumi.Input['TeamTeamSyncArgs'] team_sync: Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
               documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
               API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if ignore_externally_synced_members is not None:
            pulumi.set(__self__, "ignore_externally_synced_members", ignore_externally_synced_members)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if preferences is not None:
            pulumi.set(__self__, "preferences", preferences)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if team_sync is not None:
            pulumi.set(__self__, "team_sync", team_sync)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address for the team.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="ignoreExternallySyncedMembers")
    def ignore_externally_synced_members(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ignore_externally_synced_members")

    @ignore_externally_synced_members.setter
    def ignore_externally_synced_members(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_externally_synced_members", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
        must already exist in Grafana.
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the Grafana team created.
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
    def preferences(self) -> Optional[pulumi.Input['TeamPreferencesArgs']]:
        return pulumi.get(self, "preferences")

    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input['TeamPreferencesArgs']]):
        pulumi.set(self, "preferences", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[int]]:
        """
        The team id assigned to this team by Grafana.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="teamSync")
    def team_sync(self) -> Optional[pulumi.Input['TeamTeamSyncArgs']]:
        """
        Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
        documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
        API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        return pulumi.get(self, "team_sync")

    @team_sync.setter
    def team_sync(self, value: Optional[pulumi.Input['TeamTeamSyncArgs']]):
        pulumi.set(self, "team_sync", value)


warnings.warn("""grafana.index/team.Team has been deprecated in favor of grafana.oss/team.Team""", DeprecationWarning)


class Team(pulumi.CustomResource):
    warnings.warn("""grafana.index/team.Team has been deprecated in favor of grafana.oss/team.Team""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 ignore_externally_synced_members: Optional[pulumi.Input[bool]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 preferences: Optional[pulumi.Input[pulumi.InputType['TeamPreferencesArgs']]] = None,
                 team_sync: Optional[pulumi.Input[pulumi.InputType['TeamTeamSyncArgs']]] = None,
                 __props__=None):
        """
        Create a Team resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: An email address for the team.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
               must already exist in Grafana.
        :param pulumi.Input[str] name: The display name for the Grafana team created.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[pulumi.InputType['TeamTeamSyncArgs']] team_sync: Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
               documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
               API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TeamArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Team resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TeamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 ignore_externally_synced_members: Optional[pulumi.Input[bool]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 preferences: Optional[pulumi.Input[pulumi.InputType['TeamPreferencesArgs']]] = None,
                 team_sync: Optional[pulumi.Input[pulumi.InputType['TeamTeamSyncArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Team is deprecated: grafana.index/team.Team has been deprecated in favor of grafana.oss/team.Team""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamArgs.__new__(TeamArgs)

            __props__.__dict__["email"] = email
            __props__.__dict__["ignore_externally_synced_members"] = ignore_externally_synced_members
            __props__.__dict__["members"] = members
            __props__.__dict__["name"] = name
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["preferences"] = preferences
            __props__.__dict__["team_sync"] = team_sync
            __props__.__dict__["team_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="grafana:index/team:Team")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Team, __self__).__init__(
            'grafana:index/team:Team',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            email: Optional[pulumi.Input[str]] = None,
            ignore_externally_synced_members: Optional[pulumi.Input[bool]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            preferences: Optional[pulumi.Input[pulumi.InputType['TeamPreferencesArgs']]] = None,
            team_id: Optional[pulumi.Input[int]] = None,
            team_sync: Optional[pulumi.Input[pulumi.InputType['TeamTeamSyncArgs']]] = None) -> 'Team':
        """
        Get an existing Team resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: An email address for the team.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
               must already exist in Grafana.
        :param pulumi.Input[str] name: The display name for the Grafana team created.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] team_id: The team id assigned to this team by Grafana.
        :param pulumi.Input[pulumi.InputType['TeamTeamSyncArgs']] team_sync: Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
               documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
               API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamState.__new__(_TeamState)

        __props__.__dict__["email"] = email
        __props__.__dict__["ignore_externally_synced_members"] = ignore_externally_synced_members
        __props__.__dict__["members"] = members
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["preferences"] = preferences
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["team_sync"] = team_sync
        return Team(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        An email address for the team.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="ignoreExternallySyncedMembers")
    def ignore_externally_synced_members(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "ignore_externally_synced_members")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
        must already exist in Grafana.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name for the Grafana team created.
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
    def preferences(self) -> pulumi.Output[Optional['outputs.TeamPreferences']]:
        return pulumi.get(self, "preferences")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[int]:
        """
        The team id assigned to this team by Grafana.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="teamSync")
    def team_sync(self) -> pulumi.Output[Optional['outputs.TeamTeamSync']]:
        """
        Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
        documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
        API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
        """
        return pulumi.get(self, "team_sync")

