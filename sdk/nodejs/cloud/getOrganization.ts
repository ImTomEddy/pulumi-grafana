// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const test = grafana.cloud.getOrganization({
 *     slug: "my-org",
 * });
 * ```
 */
export function getOrganization(args?: GetOrganizationArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:cloud/getOrganization:getOrganization", {
        "id": args.id,
        "slug": args.slug,
    }, opts);
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationArgs {
    /**
     * The ID of this resource.
     */
    id?: string;
    slug?: string;
}

/**
 * A collection of values returned by getOrganization.
 */
export interface GetOrganizationResult {
    readonly createdAt: string;
    /**
     * The ID of this resource.
     */
    readonly id: string;
    readonly name: string;
    readonly slug: string;
    readonly updatedAt: string;
    readonly url: string;
}
/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const test = grafana.cloud.getOrganization({
 *     slug: "my-org",
 * });
 * ```
 */
export function getOrganizationOutput(args?: GetOrganizationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationResult> {
    return pulumi.output(args).apply((a: any) => getOrganization(a, opts))
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationOutputArgs {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    slug?: pulumi.Input<string>;
}
