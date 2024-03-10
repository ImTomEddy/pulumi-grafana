// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages Grafana public dashboards.
 *
 * **Note:** This resource is available only with Grafana 10.2+.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/dashboard-public/)
 * * [HTTP API](https://grafana.com/docs/grafana/next/developers/http_api/dashboard_public/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumiverse/grafana";
 *
 * // Optional (On-premise, not supported in Grafana Cloud): Create an organization
 * const myOrg = new grafana.Organization("myOrg", {});
 * // Create resources (optional: within the organization)
 * const myFolder = new grafana.Folder("myFolder", {
 *     orgId: myOrg.orgId,
 *     title: "test Folder",
 * });
 * const testDash = new grafana.Dashboard("testDash", {
 *     orgId: myOrg.orgId,
 *     folder: myFolder.id,
 *     configJson: JSON.stringify({
 *         title: "My Terraform Dashboard",
 *         uid: "my-dashboard-uid",
 *     }),
 * });
 * const myPublicDashboard = new grafana.DashboardPublic("myPublicDashboard", {
 *     orgId: myOrg.orgId,
 *     dashboardUid: testDash.uid,
 *     uid: "my-custom-public-uid",
 *     accessToken: "e99e4275da6f410d83760eefa934d8d2",
 *     timeSelectionEnabled: true,
 *     isEnabled: true,
 *     annotationsEnabled: true,
 *     share: "public",
 * });
 * // Optional (On-premise, not supported in Grafana Cloud): Create an organization
 * const myOrg2 = new grafana.Organization("myOrg2", {});
 * const testDash2 = new grafana.Dashboard("testDash2", {
 *     orgId: myOrg2.orgId,
 *     configJson: JSON.stringify({
 *         title: "My Terraform Dashboard2",
 *         uid: "my-dashboard-uid2",
 *     }),
 * });
 * const myPublicDashboard2 = new grafana.DashboardPublic("myPublicDashboard2", {
 *     orgId: myOrg2.orgId,
 *     dashboardUid: testDash2.uid,
 *     share: "public",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import grafana:index/dashboardPublic:DashboardPublic dashboard_name {{dashboard_uid}}:{{public_dashboard_uid}} # To use the default provider org
 * ```
 *
 * ```sh
 *  $ pulumi import grafana:index/dashboardPublic:DashboardPublic dashboard_name {org_id}}:{{dashboard_uid}}:{{public_dashboard_uid}} # When "org_id" is set on the resource
 * ```
 */
export class DashboardPublic extends pulumi.CustomResource {
    /**
     * Get an existing DashboardPublic resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardPublicState, opts?: pulumi.CustomResourceOptions): DashboardPublic {
        return new DashboardPublic(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/dashboardPublic:DashboardPublic';

    /**
     * Returns true if the given object is an instance of DashboardPublic.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DashboardPublic {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DashboardPublic.__pulumiType;
    }

    /**
     * A public unique identifier of a public dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a public dashboard.
     */
    public readonly accessToken!: pulumi.Output<string>;
    /**
     * Set to `true` to show annotations. The default value is `false`.
     */
    public readonly annotationsEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The unique identifier of the original dashboard.
     */
    public readonly dashboardUid!: pulumi.Output<string>;
    /**
     * Set to `true` to enable the public dashboard. The default value is `false`.
     */
    public readonly isEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * Set the share mode. The default value is `public`.
     */
    public readonly share!: pulumi.Output<string | undefined>;
    /**
     * Set to `true` to enable the time picker in the public dashboard. The default value is `false`.
     */
    public readonly timeSelectionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The unique identifier of a public dashboard. It's automatically generated if not provided when creating a public dashboard.
     */
    public readonly uid!: pulumi.Output<string>;

    /**
     * Create a DashboardPublic resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardPublicArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DashboardPublicArgs | DashboardPublicState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DashboardPublicState | undefined;
            resourceInputs["accessToken"] = state ? state.accessToken : undefined;
            resourceInputs["annotationsEnabled"] = state ? state.annotationsEnabled : undefined;
            resourceInputs["dashboardUid"] = state ? state.dashboardUid : undefined;
            resourceInputs["isEnabled"] = state ? state.isEnabled : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["share"] = state ? state.share : undefined;
            resourceInputs["timeSelectionEnabled"] = state ? state.timeSelectionEnabled : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as DashboardPublicArgs | undefined;
            if ((!args || args.dashboardUid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dashboardUid'");
            }
            resourceInputs["accessToken"] = args ? args.accessToken : undefined;
            resourceInputs["annotationsEnabled"] = args ? args.annotationsEnabled : undefined;
            resourceInputs["dashboardUid"] = args ? args.dashboardUid : undefined;
            resourceInputs["isEnabled"] = args ? args.isEnabled : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["share"] = args ? args.share : undefined;
            resourceInputs["timeSelectionEnabled"] = args ? args.timeSelectionEnabled : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DashboardPublic.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DashboardPublic resources.
 */
export interface DashboardPublicState {
    /**
     * A public unique identifier of a public dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a public dashboard.
     */
    accessToken?: pulumi.Input<string>;
    /**
     * Set to `true` to show annotations. The default value is `false`.
     */
    annotationsEnabled?: pulumi.Input<boolean>;
    /**
     * The unique identifier of the original dashboard.
     */
    dashboardUid?: pulumi.Input<string>;
    /**
     * Set to `true` to enable the public dashboard. The default value is `false`.
     */
    isEnabled?: pulumi.Input<boolean>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Set the share mode. The default value is `public`.
     */
    share?: pulumi.Input<string>;
    /**
     * Set to `true` to enable the time picker in the public dashboard. The default value is `false`.
     */
    timeSelectionEnabled?: pulumi.Input<boolean>;
    /**
     * The unique identifier of a public dashboard. It's automatically generated if not provided when creating a public dashboard.
     */
    uid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DashboardPublic resource.
 */
export interface DashboardPublicArgs {
    /**
     * A public unique identifier of a public dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a public dashboard.
     */
    accessToken?: pulumi.Input<string>;
    /**
     * Set to `true` to show annotations. The default value is `false`.
     */
    annotationsEnabled?: pulumi.Input<boolean>;
    /**
     * The unique identifier of the original dashboard.
     */
    dashboardUid: pulumi.Input<string>;
    /**
     * Set to `true` to enable the public dashboard. The default value is `false`.
     */
    isEnabled?: pulumi.Input<boolean>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Set the share mode. The default value is `public`.
     */
    share?: pulumi.Input<string>;
    /**
     * Set to `true` to enable the time picker in the public dashboard. The default value is `false`.
     */
    timeSelectionEnabled?: pulumi.Input<boolean>;
    /**
     * The unique identifier of a public dashboard. It's automatically generated if not provided when creating a public dashboard.
     */
    uid?: pulumi.Input<string>;
}
