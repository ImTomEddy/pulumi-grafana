// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [HTTP API](https://grafana.com/docs/grafana-cloud/oncall/oncall-api-reference/escalation_chains/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const defaultOncallEscalationChain = pulumi.output(grafana.getOncallEscalationChain({
 *     name: "default",
 * }));
 * ```
 */
export function getOncallEscalationChain(args: GetOncallEscalationChainArgs, opts?: pulumi.InvokeOptions): Promise<GetOncallEscalationChainResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("grafana:index/getOncallEscalationChain:getOncallEscalationChain", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getOncallEscalationChain.
 */
export interface GetOncallEscalationChainArgs {
    /**
     * The escalation chain name.
     */
    name: string;
}

/**
 * A collection of values returned by getOncallEscalationChain.
 */
export interface GetOncallEscalationChainResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The escalation chain name.
     */
    readonly name: string;
}

export function getOncallEscalationChainOutput(args: GetOncallEscalationChainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOncallEscalationChainResult> {
    return pulumi.output(args).apply(a => getOncallEscalationChain(a, opts))
}

/**
 * A collection of arguments for invoking getOncallEscalationChain.
 */
export interface GetOncallEscalationChainOutputArgs {
    /**
     * The escalation chain name.
     */
    name: pulumi.Input<string>;
}