// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages the entire set of permissions for a service account. Permissions that aren't specified when applying this resource will be removed.
 *
 * **Note:** This resource is available from Grafana 9.2.4 onwards.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/#manage-users-and-teams-permissions-for-a-service-account-in-grafana)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumiverse/grafana";
 *
 * const test = new grafana.ServiceAccount("test", {
 *     role: "Editor",
 *     isDisabled: false,
 * });
 * const testTeam = new grafana.Team("testTeam", {});
 * const testUser = new grafana.User("testUser", {
 *     email: "tf_user@test.com",
 *     login: "tf_user@test.com",
 *     password: "password",
 * });
 * const testPermissions = new grafana.ServiceAccountPermission("testPermissions", {
 *     serviceAccountId: test.id,
 *     permissions: [
 *         {
 *             userId: testUser.id,
 *             permission: "Edit",
 *         },
 *         {
 *             teamId: testTeam.id,
 *             permission: "Admin",
 *         },
 *     ],
 * });
 * ```
 */
export class ServiceAccountPermission extends pulumi.CustomResource {
    /**
     * Get an existing ServiceAccountPermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceAccountPermissionState, opts?: pulumi.CustomResourceOptions): ServiceAccountPermission {
        return new ServiceAccountPermission(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/serviceAccountPermission:ServiceAccountPermission';

    /**
     * Returns true if the given object is an instance of ServiceAccountPermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServiceAccountPermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServiceAccountPermission.__pulumiType;
    }

    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    public readonly permissions!: pulumi.Output<outputs.ServiceAccountPermissionPermission[] | undefined>;
    /**
     * The id of the service account.
     */
    public readonly serviceAccountId!: pulumi.Output<string>;

    /**
     * Create a ServiceAccountPermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServiceAccountPermissionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServiceAccountPermissionArgs | ServiceAccountPermissionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServiceAccountPermissionState | undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["permissions"] = state ? state.permissions : undefined;
            resourceInputs["serviceAccountId"] = state ? state.serviceAccountId : undefined;
        } else {
            const args = argsOrState as ServiceAccountPermissionArgs | undefined;
            if ((!args || args.serviceAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceAccountId'");
            }
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["permissions"] = args ? args.permissions : undefined;
            resourceInputs["serviceAccountId"] = args ? args.serviceAccountId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ServiceAccountPermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServiceAccountPermission resources.
 */
export interface ServiceAccountPermissionState {
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.ServiceAccountPermissionPermission>[]>;
    /**
     * The id of the service account.
     */
    serviceAccountId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ServiceAccountPermission resource.
 */
export interface ServiceAccountPermissionArgs {
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.ServiceAccountPermissionPermission>[]>;
    /**
     * The id of the service account.
     */
    serviceAccountId: pulumi.Input<string>;
}
