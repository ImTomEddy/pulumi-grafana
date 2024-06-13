// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Sets the global notification policy for Grafana.
 *
 * !> This resource manages the entire notification policy tree, and will overwrite any existing policies.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/manage-notifications/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)
 *
 * This resource requires Grafana 9.1.0 or later.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumiverse/grafana";
 *
 * const aContactPoint = new grafana.ContactPoint("aContactPoint", {emails: [{
 *     addresses: [
 *         "one@company.org",
 *         "two@company.org",
 *     ],
 *     message: "{{ len .Alerts.Firing }} firing.",
 * }]});
 * const aMuteTiming = new grafana.MuteTiming("aMuteTiming", {intervals: [{
 *     weekdays: ["monday"],
 * }]});
 * const myNotificationPolicy = new grafana.NotificationPolicy("myNotificationPolicy", {
 *     groupBies: ["..."],
 *     contactPoint: aContactPoint.name,
 *     groupWait: "45s",
 *     groupInterval: "6m",
 *     repeatInterval: "3h",
 *     policies: [
 *         {
 *             matchers: [
 *                 {
 *                     label: "mylabel",
 *                     match: "=",
 *                     value: "myvalue",
 *                 },
 *                 {
 *                     label: "alertname",
 *                     match: "=",
 *                     value: "CPU Usage",
 *                 },
 *                 {
 *                     label: "Name",
 *                     match: "=~",
 *                     value: "host.*|host-b.*",
 *                 },
 *             ],
 *             contactPoint: aContactPoint.name,
 *             "continue": true,
 *             muteTimings: [aMuteTiming.name],
 *             groupWait: "45s",
 *             groupInterval: "6m",
 *             repeatInterval: "3h",
 *             policies: [{
 *                 matchers: [{
 *                     label: "sublabel",
 *                     match: "=",
 *                     value: "subvalue",
 *                 }],
 *                 contactPoint: aContactPoint.name,
 *                 groupBies: ["..."],
 *             }],
 *         },
 *         {
 *             matchers: [{
 *                 label: "anotherlabel",
 *                 match: "=~",
 *                 value: "another value.*",
 *             }],
 *             contactPoint: aContactPoint.name,
 *             groupBies: ["..."],
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 * $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ anyString }}"
 * ```
 *
 * ```sh
 * $ pulumi import grafana:index/notificationPolicy:NotificationPolicy name "{{ orgID }}:{{ anyString }}"
 * ```
 */
export class NotificationPolicy extends pulumi.CustomResource {
    /**
     * Get an existing NotificationPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotificationPolicyState, opts?: pulumi.CustomResourceOptions): NotificationPolicy {
        return new NotificationPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/notificationPolicy:NotificationPolicy';

    /**
     * Returns true if the given object is an instance of NotificationPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NotificationPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NotificationPolicy.__pulumiType;
    }

    /**
     * The default contact point to route all unmatched notifications to.
     */
    public readonly contactPoint!: pulumi.Output<string>;
    public readonly disableProvenance!: pulumi.Output<boolean | undefined>;
    /**
     * A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
     */
    public readonly groupBies!: pulumi.Output<string[]>;
    /**
     * Minimum time interval between two notifications for the same group. Default is 5 minutes.
     */
    public readonly groupInterval!: pulumi.Output<string | undefined>;
    /**
     * Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
     */
    public readonly groupWait!: pulumi.Output<string | undefined>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * Routing rules for specific label sets.
     */
    public readonly policies!: pulumi.Output<outputs.NotificationPolicyPolicy[] | undefined>;
    /**
     * Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
     */
    public readonly repeatInterval!: pulumi.Output<string | undefined>;

    /**
     * Create a NotificationPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NotificationPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NotificationPolicyArgs | NotificationPolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NotificationPolicyState | undefined;
            resourceInputs["contactPoint"] = state ? state.contactPoint : undefined;
            resourceInputs["disableProvenance"] = state ? state.disableProvenance : undefined;
            resourceInputs["groupBies"] = state ? state.groupBies : undefined;
            resourceInputs["groupInterval"] = state ? state.groupInterval : undefined;
            resourceInputs["groupWait"] = state ? state.groupWait : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["policies"] = state ? state.policies : undefined;
            resourceInputs["repeatInterval"] = state ? state.repeatInterval : undefined;
        } else {
            const args = argsOrState as NotificationPolicyArgs | undefined;
            if ((!args || args.contactPoint === undefined) && !opts.urn) {
                throw new Error("Missing required property 'contactPoint'");
            }
            if ((!args || args.groupBies === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupBies'");
            }
            resourceInputs["contactPoint"] = args ? args.contactPoint : undefined;
            resourceInputs["disableProvenance"] = args ? args.disableProvenance : undefined;
            resourceInputs["groupBies"] = args ? args.groupBies : undefined;
            resourceInputs["groupInterval"] = args ? args.groupInterval : undefined;
            resourceInputs["groupWait"] = args ? args.groupWait : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["policies"] = args ? args.policies : undefined;
            resourceInputs["repeatInterval"] = args ? args.repeatInterval : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NotificationPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NotificationPolicy resources.
 */
export interface NotificationPolicyState {
    /**
     * The default contact point to route all unmatched notifications to.
     */
    contactPoint?: pulumi.Input<string>;
    disableProvenance?: pulumi.Input<boolean>;
    /**
     * A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
     */
    groupBies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Minimum time interval between two notifications for the same group. Default is 5 minutes.
     */
    groupInterval?: pulumi.Input<string>;
    /**
     * Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
     */
    groupWait?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Routing rules for specific label sets.
     */
    policies?: pulumi.Input<pulumi.Input<inputs.NotificationPolicyPolicy>[]>;
    /**
     * Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
     */
    repeatInterval?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NotificationPolicy resource.
 */
export interface NotificationPolicyArgs {
    /**
     * The default contact point to route all unmatched notifications to.
     */
    contactPoint: pulumi.Input<string>;
    disableProvenance?: pulumi.Input<boolean>;
    /**
     * A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
     */
    groupBies: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Minimum time interval between two notifications for the same group. Default is 5 minutes.
     */
    groupInterval?: pulumi.Input<string>;
    /**
     * Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
     */
    groupWait?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Routing rules for specific label sets.
     */
    policies?: pulumi.Input<pulumi.Input<inputs.NotificationPolicyPolicy>[]>;
    /**
     * Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
     */
    repeatInterval?: pulumi.Input<string>;
}
