// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages Grafana Alerting message templates.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/template-notifications/create-notification-templates/)
 * * [HTTP API](https://grafana.com/docs/grafana/next/developers/http_api/alerting_provisioning/#templates)
 *
 * This resource requires Grafana 9.1.0 or later.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumiverse/grafana";
 *
 * const myTemplate = new grafana.MessageTemplate("myTemplate", {template: `{{define "My Reusable Template" }}
 *  template content
 * {{ end }}
 * `});
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * ```sh
 * $ pulumi import grafana:index/messageTemplate:MessageTemplate name "{{ name }}"
 * ```
 *
 * ```sh
 * $ pulumi import grafana:index/messageTemplate:MessageTemplate name "{{ orgID }}:{{ name }}"
 * ```
 */
export class MessageTemplate extends pulumi.CustomResource {
    /**
     * Get an existing MessageTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MessageTemplateState, opts?: pulumi.CustomResourceOptions): MessageTemplate {
        return new MessageTemplate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/messageTemplate:MessageTemplate';

    /**
     * Returns true if the given object is an instance of MessageTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MessageTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MessageTemplate.__pulumiType;
    }

    /**
     * Allow modifying the message template from other sources than Terraform or the Grafana API.
     */
    public readonly disableProvenance!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the message template.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * The content of the message template.
     */
    public readonly template!: pulumi.Output<string>;

    /**
     * Create a MessageTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MessageTemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MessageTemplateArgs | MessageTemplateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MessageTemplateState | undefined;
            resourceInputs["disableProvenance"] = state ? state.disableProvenance : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["template"] = state ? state.template : undefined;
        } else {
            const args = argsOrState as MessageTemplateArgs | undefined;
            if ((!args || args.template === undefined) && !opts.urn) {
                throw new Error("Missing required property 'template'");
            }
            resourceInputs["disableProvenance"] = args ? args.disableProvenance : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["template"] = args ? args.template : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MessageTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MessageTemplate resources.
 */
export interface MessageTemplateState {
    /**
     * Allow modifying the message template from other sources than Terraform or the Grafana API.
     */
    disableProvenance?: pulumi.Input<boolean>;
    /**
     * The name of the message template.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The content of the message template.
     */
    template?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MessageTemplate resource.
 */
export interface MessageTemplateArgs {
    /**
     * Allow modifying the message template from other sources than Terraform or the Grafana API.
     */
    disableProvenance?: pulumi.Input<boolean>;
    /**
     * The name of the message template.
     */
    name?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The content of the message template.
     */
    template: pulumi.Input<string>;
}
