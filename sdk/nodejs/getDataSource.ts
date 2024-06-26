// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getdatasource.getDataSource has been deprecated in favor of grafana.oss/getdatasource.getDataSource */
export function getDataSource(args?: GetDataSourceArgs, opts?: pulumi.InvokeOptions): Promise<GetDataSourceResult> {
    pulumi.log.warn("getDataSource is deprecated: grafana.index/getdatasource.getDataSource has been deprecated in favor of grafana.oss/getdatasource.getDataSource")
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getDataSource:getDataSource", {
        "id": args.id,
        "name": args.name,
        "orgId": args.orgId,
        "uid": args.uid,
    }, opts);
}

/**
 * A collection of arguments for invoking getDataSource.
 */
export interface GetDataSourceArgs {
    /**
     * @deprecated Use `uid` instead of `id`
     */
    id?: string;
    name?: string;
    orgId?: string;
    uid?: string;
}

/**
 * A collection of values returned by getDataSource.
 */
export interface GetDataSourceResult {
    readonly accessMode: string;
    readonly basicAuthEnabled: boolean;
    readonly basicAuthUsername: string;
    readonly databaseName: string;
    /**
     * @deprecated Use `uid` instead of `id`
     */
    readonly id: string;
    readonly isDefault: boolean;
    readonly jsonDataEncoded: string;
    readonly name: string;
    readonly orgId?: string;
    readonly type: string;
    readonly uid: string;
    readonly url: string;
    readonly username: string;
}
/** @deprecated grafana.index/getdatasource.getDataSource has been deprecated in favor of grafana.oss/getdatasource.getDataSource */
export function getDataSourceOutput(args?: GetDataSourceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDataSourceResult> {
    return pulumi.output(args).apply((a: any) => getDataSource(a, opts))
}

/**
 * A collection of arguments for invoking getDataSource.
 */
export interface GetDataSourceOutputArgs {
    /**
     * @deprecated Use `uid` instead of `id`
     */
    id?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    orgId?: pulumi.Input<string>;
    uid?: pulumi.Input<string>;
}
