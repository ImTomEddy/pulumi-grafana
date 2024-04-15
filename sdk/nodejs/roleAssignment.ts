// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class RoleAssignment extends pulumi.CustomResource {
    /**
     * Get an existing RoleAssignment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RoleAssignmentState, opts?: pulumi.CustomResourceOptions): RoleAssignment {
        return new RoleAssignment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/roleAssignment:RoleAssignment';

    /**
     * Returns true if the given object is an instance of RoleAssignment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RoleAssignment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RoleAssignment.__pulumiType;
    }

    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * Grafana RBAC role UID.
     */
    public readonly roleUid!: pulumi.Output<string>;
    /**
     * IDs of service accounts that the role should be assigned to.
     */
    public readonly serviceAccounts!: pulumi.Output<string[] | undefined>;
    /**
     * IDs of teams that the role should be assigned to.
     */
    public readonly teams!: pulumi.Output<string[] | undefined>;
    /**
     * IDs of users that the role should be assigned to.
     */
    public readonly users!: pulumi.Output<number[] | undefined>;

    /**
     * Create a RoleAssignment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RoleAssignmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RoleAssignmentArgs | RoleAssignmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RoleAssignmentState | undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["roleUid"] = state ? state.roleUid : undefined;
            resourceInputs["serviceAccounts"] = state ? state.serviceAccounts : undefined;
            resourceInputs["teams"] = state ? state.teams : undefined;
            resourceInputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as RoleAssignmentArgs | undefined;
            if ((!args || args.roleUid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleUid'");
            }
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["roleUid"] = args ? args.roleUid : undefined;
            resourceInputs["serviceAccounts"] = args ? args.serviceAccounts : undefined;
            resourceInputs["teams"] = args ? args.teams : undefined;
            resourceInputs["users"] = args ? args.users : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RoleAssignment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RoleAssignment resources.
 */
export interface RoleAssignmentState {
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Grafana RBAC role UID.
     */
    roleUid?: pulumi.Input<string>;
    /**
     * IDs of service accounts that the role should be assigned to.
     */
    serviceAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * IDs of teams that the role should be assigned to.
     */
    teams?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * IDs of users that the role should be assigned to.
     */
    users?: pulumi.Input<pulumi.Input<number>[]>;
}

/**
 * The set of arguments for constructing a RoleAssignment resource.
 */
export interface RoleAssignmentArgs {
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Grafana RBAC role UID.
     */
    roleUid: pulumi.Input<string>;
    /**
     * IDs of service accounts that the role should be assigned to.
     */
    serviceAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * IDs of teams that the role should be assigned to.
     */
    teams?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * IDs of users that the role should be assigned to.
     */
    users?: pulumi.Input<pulumi.Input<number>[]>;
}
