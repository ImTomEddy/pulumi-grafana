// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getoncalloutgoingwebhook.getOncallOutgoingWebhook has been deprecated in favor of grafana.oncall/getoutgoingwebhook.getOutgoingWebhook */
export function getOncallOutgoingWebhook(args: GetOncallOutgoingWebhookArgs, opts?: pulumi.InvokeOptions): Promise<GetOncallOutgoingWebhookResult> {
    pulumi.log.warn("getOncallOutgoingWebhook is deprecated: grafana.index/getoncalloutgoingwebhook.getOncallOutgoingWebhook has been deprecated in favor of grafana.oncall/getoutgoingwebhook.getOutgoingWebhook")

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getOncallOutgoingWebhook:getOncallOutgoingWebhook", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getOncallOutgoingWebhook.
 */
export interface GetOncallOutgoingWebhookArgs {
    name: string;
}

/**
 * A collection of values returned by getOncallOutgoingWebhook.
 */
export interface GetOncallOutgoingWebhookResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
}
/** @deprecated grafana.index/getoncalloutgoingwebhook.getOncallOutgoingWebhook has been deprecated in favor of grafana.oncall/getoutgoingwebhook.getOutgoingWebhook */
export function getOncallOutgoingWebhookOutput(args: GetOncallOutgoingWebhookOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOncallOutgoingWebhookResult> {
    return pulumi.output(args).apply((a: any) => getOncallOutgoingWebhook(a, opts))
}

/**
 * A collection of arguments for invoking getOncallOutgoingWebhook.
 */
export interface GetOncallOutgoingWebhookOutputArgs {
    name: pulumi.Input<string>;
}
