// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * @deprecated grafana.index/datasource.DataSource has been deprecated in favor of grafana.oss/datasource.DataSource
 */
export class DataSource extends pulumi.CustomResource {
    /**
     * Get an existing DataSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataSourceState, opts?: pulumi.CustomResourceOptions): DataSource {
        pulumi.log.warn("DataSource is deprecated: grafana.index/datasource.DataSource has been deprecated in favor of grafana.oss/datasource.DataSource")
        return new DataSource(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/dataSource:DataSource';

    /**
     * Returns true if the given object is an instance of DataSource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSource.__pulumiType;
    }

    /**
     * The method by which Grafana will access the data source: `proxy` or `direct`.
     */
    public readonly accessMode!: pulumi.Output<string | undefined>;
    /**
     * Whether to enable basic auth for the data source.
     */
    public readonly basicAuthEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Basic auth username.
     */
    public readonly basicAuthUsername!: pulumi.Output<string | undefined>;
    /**
     * (Required by some data source types) The name of the database to use on the selected data source server.
     */
    public readonly databaseName!: pulumi.Output<string | undefined>;
    /**
     * Custom HTTP headers
     */
    public readonly httpHeaders!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Whether to set the data source as default. This should only be `true` to a single data source.
     */
    public readonly isDefault!: pulumi.Output<boolean | undefined>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    public readonly jsonDataEncoded!: pulumi.Output<string | undefined>;
    /**
     * A unique name for the data source.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    public readonly secureJsonDataEncoded!: pulumi.Output<string | undefined>;
    /**
     * The data source type. Must be one of the supported data source keywords.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    public readonly uid!: pulumi.Output<string>;
    /**
     * The URL for the data source. The type of URL required varies depending on the chosen data source type.
     */
    public readonly url!: pulumi.Output<string | undefined>;
    /**
     * (Required by some data source types) The username to use to authenticate to the data source.
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a DataSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated grafana.index/datasource.DataSource has been deprecated in favor of grafana.oss/datasource.DataSource */
    constructor(name: string, args: DataSourceArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated grafana.index/datasource.DataSource has been deprecated in favor of grafana.oss/datasource.DataSource */
    constructor(name: string, argsOrState?: DataSourceArgs | DataSourceState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DataSource is deprecated: grafana.index/datasource.DataSource has been deprecated in favor of grafana.oss/datasource.DataSource")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DataSourceState | undefined;
            resourceInputs["accessMode"] = state ? state.accessMode : undefined;
            resourceInputs["basicAuthEnabled"] = state ? state.basicAuthEnabled : undefined;
            resourceInputs["basicAuthUsername"] = state ? state.basicAuthUsername : undefined;
            resourceInputs["databaseName"] = state ? state.databaseName : undefined;
            resourceInputs["httpHeaders"] = state ? state.httpHeaders : undefined;
            resourceInputs["isDefault"] = state ? state.isDefault : undefined;
            resourceInputs["jsonDataEncoded"] = state ? state.jsonDataEncoded : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["secureJsonDataEncoded"] = state ? state.secureJsonDataEncoded : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
            resourceInputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as DataSourceArgs | undefined;
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["accessMode"] = args ? args.accessMode : undefined;
            resourceInputs["basicAuthEnabled"] = args ? args.basicAuthEnabled : undefined;
            resourceInputs["basicAuthUsername"] = args ? args.basicAuthUsername : undefined;
            resourceInputs["databaseName"] = args ? args.databaseName : undefined;
            resourceInputs["httpHeaders"] = args?.httpHeaders ? pulumi.secret(args.httpHeaders) : undefined;
            resourceInputs["isDefault"] = args ? args.isDefault : undefined;
            resourceInputs["jsonDataEncoded"] = args ? args.jsonDataEncoded : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["secureJsonDataEncoded"] = args?.secureJsonDataEncoded ? pulumi.secret(args.secureJsonDataEncoded) : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
            resourceInputs["username"] = args ? args.username : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "grafana:index/dataSource:DataSource" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        const secretOpts = { additionalSecretOutputs: ["httpHeaders", "secureJsonDataEncoded"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(DataSource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DataSource resources.
 */
export interface DataSourceState {
    /**
     * The method by which Grafana will access the data source: `proxy` or `direct`.
     */
    accessMode?: pulumi.Input<string>;
    /**
     * Whether to enable basic auth for the data source.
     */
    basicAuthEnabled?: pulumi.Input<boolean>;
    /**
     * Basic auth username.
     */
    basicAuthUsername?: pulumi.Input<string>;
    /**
     * (Required by some data source types) The name of the database to use on the selected data source server.
     */
    databaseName?: pulumi.Input<string>;
    /**
     * Custom HTTP headers
     */
    httpHeaders?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether to set the data source as default. This should only be `true` to a single data source.
     */
    isDefault?: pulumi.Input<boolean>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    jsonDataEncoded?: pulumi.Input<string>;
    /**
     * A unique name for the data source.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    secureJsonDataEncoded?: pulumi.Input<string>;
    /**
     * The data source type. Must be one of the supported data source keywords.
     */
    type?: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
    /**
     * The URL for the data source. The type of URL required varies depending on the chosen data source type.
     */
    url?: pulumi.Input<string>;
    /**
     * (Required by some data source types) The username to use to authenticate to the data source.
     */
    username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DataSource resource.
 */
export interface DataSourceArgs {
    /**
     * The method by which Grafana will access the data source: `proxy` or `direct`.
     */
    accessMode?: pulumi.Input<string>;
    /**
     * Whether to enable basic auth for the data source.
     */
    basicAuthEnabled?: pulumi.Input<boolean>;
    /**
     * Basic auth username.
     */
    basicAuthUsername?: pulumi.Input<string>;
    /**
     * (Required by some data source types) The name of the database to use on the selected data source server.
     */
    databaseName?: pulumi.Input<string>;
    /**
     * Custom HTTP headers
     */
    httpHeaders?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether to set the data source as default. This should only be `true` to a single data source.
     */
    isDefault?: pulumi.Input<boolean>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    jsonDataEncoded?: pulumi.Input<string>;
    /**
     * A unique name for the data source.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    secureJsonDataEncoded?: pulumi.Input<string>;
    /**
     * The data source type. Must be one of the supported data source keywords.
     */
    type: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
    /**
     * The URL for the data source. The type of URL required varies depending on the chosen data source type.
     */
    url?: pulumi.Input<string>;
    /**
     * (Required by some data source types) The username to use to authenticate to the data source.
     */
    username?: pulumi.Input<string>;
}
