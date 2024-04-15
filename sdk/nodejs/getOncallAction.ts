// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getOncallAction(args: GetOncallActionArgs, opts?: pulumi.InvokeOptions): Promise<GetOncallActionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getOncallAction:getOncallAction", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getOncallAction.
 */
export interface GetOncallActionArgs {
    name: string;
}

/**
 * A collection of values returned by getOncallAction.
 */
export interface GetOncallActionResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
}
export function getOncallActionOutput(args: GetOncallActionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOncallActionResult> {
    return pulumi.output(args).apply((a: any) => getOncallAction(a, opts))
}

/**
 * A collection of arguments for invoking getOncallAction.
 */
export interface GetOncallActionOutputArgs {
    name: pulumi.Input<string>;
}
