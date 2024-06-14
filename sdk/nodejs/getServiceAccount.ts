// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getserviceaccount.getServiceAccount has been deprecated in favor of grafana.oss/getserviceaccount.getServiceAccount */
export function getServiceAccount(args: GetServiceAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceAccountResult> {
    pulumi.log.warn("getServiceAccount is deprecated: grafana.index/getserviceaccount.getServiceAccount has been deprecated in favor of grafana.oss/getserviceaccount.getServiceAccount")

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getServiceAccount:getServiceAccount", {
        "name": args.name,
        "orgId": args.orgId,
    }, opts);
}

/**
 * A collection of arguments for invoking getServiceAccount.
 */
export interface GetServiceAccountArgs {
    name: string;
    orgId?: string;
}

/**
 * A collection of values returned by getServiceAccount.
 */
export interface GetServiceAccountResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly isDisabled: boolean;
    readonly name: string;
    readonly orgId?: string;
    readonly role: string;
}
/** @deprecated grafana.index/getserviceaccount.getServiceAccount has been deprecated in favor of grafana.oss/getserviceaccount.getServiceAccount */
export function getServiceAccountOutput(args: GetServiceAccountOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceAccountResult> {
    return pulumi.output(args).apply((a: any) => getServiceAccount(a, opts))
}

/**
 * A collection of arguments for invoking getServiceAccount.
 */
export interface GetServiceAccountOutputArgs {
    name: pulumi.Input<string>;
    orgId?: pulumi.Input<string>;
}
