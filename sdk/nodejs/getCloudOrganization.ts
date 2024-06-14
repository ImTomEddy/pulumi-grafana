// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getcloudorganization.getCloudOrganization has been deprecated in favor of grafana.cloud/getorganization.getOrganization */
export function getCloudOrganization(args?: GetCloudOrganizationArgs, opts?: pulumi.InvokeOptions): Promise<GetCloudOrganizationResult> {
    pulumi.log.warn("getCloudOrganization is deprecated: grafana.index/getcloudorganization.getCloudOrganization has been deprecated in favor of grafana.cloud/getorganization.getOrganization")
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getCloudOrganization:getCloudOrganization", {
        "id": args.id,
        "slug": args.slug,
    }, opts);
}

/**
 * A collection of arguments for invoking getCloudOrganization.
 */
export interface GetCloudOrganizationArgs {
    id?: string;
    slug?: string;
}

/**
 * A collection of values returned by getCloudOrganization.
 */
export interface GetCloudOrganizationResult {
    readonly createdAt: string;
    readonly id: string;
    readonly name: string;
    readonly slug: string;
    readonly updatedAt: string;
    readonly url: string;
}
/** @deprecated grafana.index/getcloudorganization.getCloudOrganization has been deprecated in favor of grafana.cloud/getorganization.getOrganization */
export function getCloudOrganizationOutput(args?: GetCloudOrganizationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCloudOrganizationResult> {
    return pulumi.output(args).apply((a: any) => getCloudOrganization(a, opts))
}

/**
 * A collection of arguments for invoking getCloudOrganization.
 */
export interface GetCloudOrganizationOutputArgs {
    id?: pulumi.Input<string>;
    slug?: pulumi.Input<string>;
}
