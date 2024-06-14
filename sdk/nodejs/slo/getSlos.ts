// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Datasource for retrieving all SLOs.
 *
 * * [Official documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/)
 * * [API documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/api/)
 * * [Additional Information On Alerting Rule Annotations and Labels](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/#templating/)
 */
export function getSlos(opts?: pulumi.InvokeOptions): Promise<GetSlosResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:slo/getSlos:getSlos", {
    }, opts);
}

/**
 * A collection of values returned by getSlos.
 */
export interface GetSlosResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Returns a list of all SLOs"
     */
    readonly slos: outputs.slo.GetSlosSlo[];
}
/**
 * Datasource for retrieving all SLOs.
 *
 * * [Official documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/)
 * * [API documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/api/)
 * * [Additional Information On Alerting Rule Annotations and Labels](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/#templating/)
 */
export function getSlosOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetSlosResult> {
    return pulumi.output(getSlos(opts))
}
