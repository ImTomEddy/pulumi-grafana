// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/team-management/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/team/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumiverse/grafana";
 *
 * const viewer = new grafana.User("viewer", {
 *     email: "viewer@example.com",
 *     login: "viewer",
 *     password: "my-password",
 * });
 * const test_team = new grafana.Team("test-team", {
 *     email: "teamemail@example.com",
 *     members: [viewer.email],
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 * $ pulumi import grafana:index/team:Team name "{{ id }}"
 * ```
 *
 * ```sh
 * $ pulumi import grafana:index/team:Team name "{{ orgID }}:{{ id }}"
 * ```
 */
export class Team extends pulumi.CustomResource {
    /**
     * Get an existing Team resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TeamState, opts?: pulumi.CustomResourceOptions): Team {
        return new Team(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/team:Team';

    /**
     * Returns true if the given object is an instance of Team.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Team {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Team.__pulumiType;
    }

    /**
     * An email address for the team.
     */
    public readonly email!: pulumi.Output<string | undefined>;
    public readonly ignoreExternallySyncedMembers!: pulumi.Output<boolean | undefined>;
    /**
     * A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
     * must already exist in Grafana.
     */
    public readonly members!: pulumi.Output<string[] | undefined>;
    /**
     * The display name for the Grafana team created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    public readonly preferences!: pulumi.Output<outputs.TeamPreferences | undefined>;
    /**
     * The team id assigned to this team by Grafana.
     */
    public /*out*/ readonly teamId!: pulumi.Output<number>;
    /**
     * Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
     * documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
     * API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
     */
    public readonly teamSync!: pulumi.Output<outputs.TeamTeamSync | undefined>;

    /**
     * Create a Team resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: TeamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TeamArgs | TeamState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TeamState | undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["ignoreExternallySyncedMembers"] = state ? state.ignoreExternallySyncedMembers : undefined;
            resourceInputs["members"] = state ? state.members : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["preferences"] = state ? state.preferences : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
            resourceInputs["teamSync"] = state ? state.teamSync : undefined;
        } else {
            const args = argsOrState as TeamArgs | undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["ignoreExternallySyncedMembers"] = args ? args.ignoreExternallySyncedMembers : undefined;
            resourceInputs["members"] = args ? args.members : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["preferences"] = args ? args.preferences : undefined;
            resourceInputs["teamSync"] = args ? args.teamSync : undefined;
            resourceInputs["teamId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Team.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Team resources.
 */
export interface TeamState {
    /**
     * An email address for the team.
     */
    email?: pulumi.Input<string>;
    ignoreExternallySyncedMembers?: pulumi.Input<boolean>;
    /**
     * A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
     * must already exist in Grafana.
     */
    members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the Grafana team created.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    preferences?: pulumi.Input<inputs.TeamPreferences>;
    /**
     * The team id assigned to this team by Grafana.
     */
    teamId?: pulumi.Input<number>;
    /**
     * Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
     * documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
     * API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
     */
    teamSync?: pulumi.Input<inputs.TeamTeamSync>;
}

/**
 * The set of arguments for constructing a Team resource.
 */
export interface TeamArgs {
    /**
     * An email address for the team.
     */
    email?: pulumi.Input<string>;
    ignoreExternallySyncedMembers?: pulumi.Input<boolean>;
    /**
     * A set of email addresses corresponding to users who should be given membership to the team. Note: users specified here
     * must already exist in Grafana.
     */
    members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the Grafana team created.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    preferences?: pulumi.Input<inputs.TeamPreferences>;
    /**
     * Sync external auth provider groups with this Grafana team. Only available in Grafana Enterprise. * [Official
     * documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-team-sync/) * [HTTP
     * API](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
     */
    teamSync?: pulumi.Input<inputs.TeamTeamSync>;
}
