// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getTeam(args: GetTeamArgs, opts?: pulumi.InvokeOptions): Promise<GetTeamResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getTeam:getTeam", {
        "name": args.name,
        "orgId": args.orgId,
        "readTeamSync": args.readTeamSync,
    }, opts);
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamArgs {
    name: string;
    orgId?: string;
    readTeamSync?: boolean;
}

/**
 * A collection of values returned by getTeam.
 */
export interface GetTeamResult {
    readonly email: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly members: string[];
    readonly name: string;
    readonly orgId?: string;
    readonly preferences: outputs.GetTeamPreference[];
    readonly readTeamSync?: boolean;
    readonly teamId: number;
    readonly teamSyncs: outputs.GetTeamTeamSync[];
}
export function getTeamOutput(args: GetTeamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTeamResult> {
    return pulumi.output(args).apply((a: any) => getTeam(a, opts))
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamOutputArgs {
    name: pulumi.Input<string>;
    orgId?: pulumi.Input<string>;
    readTeamSync?: pulumi.Input<boolean>;
}
