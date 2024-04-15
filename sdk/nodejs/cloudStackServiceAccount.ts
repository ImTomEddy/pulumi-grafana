// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class CloudStackServiceAccount extends pulumi.CustomResource {
    /**
     * Get an existing CloudStackServiceAccount resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudStackServiceAccountState, opts?: pulumi.CustomResourceOptions): CloudStackServiceAccount {
        return new CloudStackServiceAccount(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/cloudStackServiceAccount:CloudStackServiceAccount';

    /**
     * Returns true if the given object is an instance of CloudStackServiceAccount.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudStackServiceAccount {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudStackServiceAccount.__pulumiType;
    }

    /**
     * The disabled status for the service account.
     */
    public readonly isDisabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the service account.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The basic role of the service account in the organization.
     */
    public readonly role!: pulumi.Output<string | undefined>;
    public readonly stackSlug!: pulumi.Output<string>;

    /**
     * Create a CloudStackServiceAccount resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CloudStackServiceAccountArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CloudStackServiceAccountArgs | CloudStackServiceAccountState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CloudStackServiceAccountState | undefined;
            resourceInputs["isDisabled"] = state ? state.isDisabled : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
            resourceInputs["stackSlug"] = state ? state.stackSlug : undefined;
        } else {
            const args = argsOrState as CloudStackServiceAccountArgs | undefined;
            if ((!args || args.stackSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stackSlug'");
            }
            resourceInputs["isDisabled"] = args ? args.isDisabled : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["stackSlug"] = args ? args.stackSlug : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CloudStackServiceAccount.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudStackServiceAccount resources.
 */
export interface CloudStackServiceAccountState {
    /**
     * The disabled status for the service account.
     */
    isDisabled?: pulumi.Input<boolean>;
    /**
     * The name of the service account.
     */
    name?: pulumi.Input<string>;
    /**
     * The basic role of the service account in the organization.
     */
    role?: pulumi.Input<string>;
    stackSlug?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudStackServiceAccount resource.
 */
export interface CloudStackServiceAccountArgs {
    /**
     * The disabled status for the service account.
     */
    isDisabled?: pulumi.Input<boolean>;
    /**
     * The name of the service account.
     */
    name?: pulumi.Input<string>;
    /**
     * The basic role of the service account in the organization.
     */
    role?: pulumi.Input<string>;
    stackSlug: pulumi.Input<string>;
}
