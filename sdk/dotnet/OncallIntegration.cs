// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana
{
    /// <summary>
    /// * [Official documentation](https://grafana.com/docs/oncall/latest/integrations/)
    /// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/)
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import grafana:index/oncallIntegration:OncallIntegration integration_name {{integration_id}}
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/oncallIntegration:OncallIntegration")]
    public partial class OncallIntegration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Default route for all alerts from the given integration
        /// </summary>
        [Output("defaultRoute")]
        public Output<Outputs.OncallIntegrationDefaultRoute> DefaultRoute { get; private set; } = null!;

        /// <summary>
        /// The link for using in an integrated tool.
        /// </summary>
        [Output("link")]
        public Output<string> Link { get; private set; } = null!;

        /// <summary>
        /// The name of the service integration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
        /// </summary>
        [Output("teamId")]
        public Output<string?> TeamId { get; private set; } = null!;

        /// <summary>
        /// Jinja2 templates for Alert payload. An empty templates block will be ignored.
        /// </summary>
        [Output("templates")]
        public Output<Outputs.OncallIntegrationTemplates?> Templates { get; private set; } = null!;

        /// <summary>
        /// The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a OncallIntegration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OncallIntegration(string name, OncallIntegrationArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/oncallIntegration:OncallIntegration", name, args ?? new OncallIntegrationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OncallIntegration(string name, Input<string> id, OncallIntegrationState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/oncallIntegration:OncallIntegration", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing OncallIntegration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OncallIntegration Get(string name, Input<string> id, OncallIntegrationState? state = null, CustomResourceOptions? options = null)
        {
            return new OncallIntegration(name, id, state, options);
        }
    }

    public sealed class OncallIntegrationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Default route for all alerts from the given integration
        /// </summary>
        [Input("defaultRoute", required: true)]
        public Input<Inputs.OncallIntegrationDefaultRouteArgs> DefaultRoute { get; set; } = null!;

        /// <summary>
        /// The name of the service integration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// Jinja2 templates for Alert payload. An empty templates block will be ignored.
        /// </summary>
        [Input("templates")]
        public Input<Inputs.OncallIntegrationTemplatesArgs>? Templates { get; set; }

        /// <summary>
        /// The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public OncallIntegrationArgs()
        {
        }
        public static new OncallIntegrationArgs Empty => new OncallIntegrationArgs();
    }

    public sealed class OncallIntegrationState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Default route for all alerts from the given integration
        /// </summary>
        [Input("defaultRoute")]
        public Input<Inputs.OncallIntegrationDefaultRouteGetArgs>? DefaultRoute { get; set; }

        /// <summary>
        /// The link for using in an integrated tool.
        /// </summary>
        [Input("link")]
        public Input<string>? Link { get; set; }

        /// <summary>
        /// The name of the service integration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// Jinja2 templates for Alert payload. An empty templates block will be ignored.
        /// </summary>
        [Input("templates")]
        public Input<Inputs.OncallIntegrationTemplatesGetArgs>? Templates { get; set; }

        /// <summary>
        /// The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging, jira.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public OncallIntegrationState()
        {
        }
        public static new OncallIntegrationState Empty => new OncallIntegrationState();
    }
}
