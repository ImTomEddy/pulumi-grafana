// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/integrations/)
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const exampleIntegration = grafana.getOncallIntegration({
 *     id: "CEXAMPLEID123",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getOncallIntegration(args: GetOncallIntegrationArgs, opts?: pulumi.InvokeOptions): Promise<GetOncallIntegrationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getOncallIntegration:getOncallIntegration", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getOncallIntegration.
 */
export interface GetOncallIntegrationArgs {
    /**
     * The integration ID.
     */
    id: string;
}

/**
 * A collection of values returned by getOncallIntegration.
 */
export interface GetOncallIntegrationResult {
    /**
     * The integration ID.
     */
    readonly id: string;
    /**
     * The integration name.
     */
    readonly name: string;
}
/**
 * * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/integrations/)
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const exampleIntegration = grafana.getOncallIntegration({
 *     id: "CEXAMPLEID123",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getOncallIntegrationOutput(args: GetOncallIntegrationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOncallIntegrationResult> {
    return pulumi.output(args).apply((a: any) => getOncallIntegration(a, opts))
}

/**
 * A collection of arguments for invoking getOncallIntegration.
 */
export interface GetOncallIntegrationOutputArgs {
    /**
     * The integration ID.
     */
    id: pulumi.Input<string>;
}
