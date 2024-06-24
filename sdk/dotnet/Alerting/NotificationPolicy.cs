// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Alerting
{
    /// <summary>
    /// Sets the global notification policy for Grafana.
    /// 
    /// !&gt; This resource manages the entire notification policy tree, and will overwrite any existing policies.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)
    /// 
    /// This resource requires Grafana 9.1.0 or later.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var aContactPoint = new Grafana.Alerting.ContactPoint("aContactPoint", new()
    ///     {
    ///         Emails = new[]
    ///         {
    ///             new Grafana.Alerting.Inputs.ContactPointEmailArgs
    ///             {
    ///                 Addresses = new[]
    ///                 {
    ///                     "one@company.org",
    ///                     "two@company.org",
    ///                 },
    ///                 Message = "{{ len .Alerts.Firing }} firing.",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var aMuteTiming = new Grafana.Alerting.MuteTiming("aMuteTiming", new()
    ///     {
    ///         Intervals = new[]
    ///         {
    ///             new Grafana.Alerting.Inputs.MuteTimingIntervalArgs
    ///             {
    ///                 Weekdays = new[]
    ///                 {
    ///                     "monday",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    ///     var myNotificationPolicy = new Grafana.Alerting.NotificationPolicy("myNotificationPolicy", new()
    ///     {
    ///         GroupBies = new[]
    ///         {
    ///             "...",
    ///         },
    ///         ContactPoint = aContactPoint.Name,
    ///         GroupWait = "45s",
    ///         GroupInterval = "6m",
    ///         RepeatInterval = "3h",
    ///         Policies = new[]
    ///         {
    ///             new Grafana.Alerting.Inputs.NotificationPolicyPolicyArgs
    ///             {
    ///                 Matchers = new[]
    ///                 {
    ///                     new Grafana.Alerting.Inputs.NotificationPolicyPolicyMatcherArgs
    ///                     {
    ///                         Label = "mylabel",
    ///                         Match = "=",
    ///                         Value = "myvalue",
    ///                     },
    ///                     new Grafana.Alerting.Inputs.NotificationPolicyPolicyMatcherArgs
    ///                     {
    ///                         Label = "alertname",
    ///                         Match = "=",
    ///                         Value = "CPU Usage",
    ///                     },
    ///                     new Grafana.Alerting.Inputs.NotificationPolicyPolicyMatcherArgs
    ///                     {
    ///                         Label = "Name",
    ///                         Match = "=~",
    ///                         Value = "host.*|host-b.*",
    ///                     },
    ///                 },
    ///                 ContactPoint = aContactPoint.Name,
    ///                 Continue = true,
    ///                 MuteTimings = new[]
    ///                 {
    ///                     aMuteTiming.Name,
    ///                 },
    ///                 GroupWait = "45s",
    ///                 GroupInterval = "6m",
    ///                 RepeatInterval = "3h",
    ///                 Policies = new[]
    ///                 {
    ///                     new Grafana.Alerting.Inputs.NotificationPolicyPolicyPolicyArgs
    ///                     {
    ///                         Matchers = new[]
    ///                         {
    ///                             new Grafana.Alerting.Inputs.NotificationPolicyPolicyPolicyMatcherArgs
    ///                             {
    ///                                 Label = "sublabel",
    ///                                 Match = "=",
    ///                                 Value = "subvalue",
    ///                             },
    ///                         },
    ///                         ContactPoint = aContactPoint.Name,
    ///                         GroupBies = new[]
    ///                         {
    ///                             "...",
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///             new Grafana.Alerting.Inputs.NotificationPolicyPolicyArgs
    ///             {
    ///                 Matchers = new[]
    ///                 {
    ///                     new Grafana.Alerting.Inputs.NotificationPolicyPolicyMatcherArgs
    ///                     {
    ///                         Label = "anotherlabel",
    ///                         Match = "=~",
    ///                         Value = "another value.*",
    ///                     },
    ///                 },
    ///                 ContactPoint = aContactPoint.Name,
    ///                 GroupBies = new[]
    ///                 {
    ///                     "...",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:alerting/notificationPolicy:NotificationPolicy name "{{ anyString }}"
    /// ```
    /// 
    /// ```sh
    /// $ pulumi import grafana:alerting/notificationPolicy:NotificationPolicy name "{{ orgID }}:{{ anyString }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:alerting/notificationPolicy:NotificationPolicy")]
    public partial class NotificationPolicy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The default contact point to route all unmatched notifications to.
        /// </summary>
        [Output("contactPoint")]
        public Output<string> ContactPoint { get; private set; } = null!;

        [Output("disableProvenance")]
        public Output<bool?> DisableProvenance { get; private set; } = null!;

        /// <summary>
        /// A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
        /// </summary>
        [Output("groupBies")]
        public Output<ImmutableArray<string>> GroupBies { get; private set; } = null!;

        /// <summary>
        /// Minimum time interval between two notifications for the same group. Default is 5 minutes.
        /// </summary>
        [Output("groupInterval")]
        public Output<string?> GroupInterval { get; private set; } = null!;

        /// <summary>
        /// Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        /// </summary>
        [Output("groupWait")]
        public Output<string?> GroupWait { get; private set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// Routing rules for specific label sets.
        /// </summary>
        [Output("policies")]
        public Output<ImmutableArray<Outputs.NotificationPolicyPolicy>> Policies { get; private set; } = null!;

        /// <summary>
        /// Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        /// </summary>
        [Output("repeatInterval")]
        public Output<string?> RepeatInterval { get; private set; } = null!;


        /// <summary>
        /// Create a NotificationPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NotificationPolicy(string name, NotificationPolicyArgs args, CustomResourceOptions? options = null)
            : base("grafana:alerting/notificationPolicy:NotificationPolicy", name, args ?? new NotificationPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NotificationPolicy(string name, Input<string> id, NotificationPolicyState? state = null, CustomResourceOptions? options = null)
            : base("grafana:alerting/notificationPolicy:NotificationPolicy", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "grafana:index/notificationPolicy:NotificationPolicy" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NotificationPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NotificationPolicy Get(string name, Input<string> id, NotificationPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new NotificationPolicy(name, id, state, options);
        }
    }

    public sealed class NotificationPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The default contact point to route all unmatched notifications to.
        /// </summary>
        [Input("contactPoint", required: true)]
        public Input<string> ContactPoint { get; set; } = null!;

        [Input("disableProvenance")]
        public Input<bool>? DisableProvenance { get; set; }

        [Input("groupBies", required: true)]
        private InputList<string>? _groupBies;

        /// <summary>
        /// A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
        /// </summary>
        public InputList<string> GroupBies
        {
            get => _groupBies ?? (_groupBies = new InputList<string>());
            set => _groupBies = value;
        }

        /// <summary>
        /// Minimum time interval between two notifications for the same group. Default is 5 minutes.
        /// </summary>
        [Input("groupInterval")]
        public Input<string>? GroupInterval { get; set; }

        /// <summary>
        /// Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        /// </summary>
        [Input("groupWait")]
        public Input<string>? GroupWait { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("policies")]
        private InputList<Inputs.NotificationPolicyPolicyArgs>? _policies;

        /// <summary>
        /// Routing rules for specific label sets.
        /// </summary>
        public InputList<Inputs.NotificationPolicyPolicyArgs> Policies
        {
            get => _policies ?? (_policies = new InputList<Inputs.NotificationPolicyPolicyArgs>());
            set => _policies = value;
        }

        /// <summary>
        /// Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        /// </summary>
        [Input("repeatInterval")]
        public Input<string>? RepeatInterval { get; set; }

        public NotificationPolicyArgs()
        {
        }
        public static new NotificationPolicyArgs Empty => new NotificationPolicyArgs();
    }

    public sealed class NotificationPolicyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The default contact point to route all unmatched notifications to.
        /// </summary>
        [Input("contactPoint")]
        public Input<string>? ContactPoint { get; set; }

        [Input("disableProvenance")]
        public Input<bool>? DisableProvenance { get; set; }

        [Input("groupBies")]
        private InputList<string>? _groupBies;

        /// <summary>
        /// A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping.
        /// </summary>
        public InputList<string> GroupBies
        {
            get => _groupBies ?? (_groupBies = new InputList<string>());
            set => _groupBies = value;
        }

        /// <summary>
        /// Minimum time interval between two notifications for the same group. Default is 5 minutes.
        /// </summary>
        [Input("groupInterval")]
        public Input<string>? GroupInterval { get; set; }

        /// <summary>
        /// Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        /// </summary>
        [Input("groupWait")]
        public Input<string>? GroupWait { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("policies")]
        private InputList<Inputs.NotificationPolicyPolicyGetArgs>? _policies;

        /// <summary>
        /// Routing rules for specific label sets.
        /// </summary>
        public InputList<Inputs.NotificationPolicyPolicyGetArgs> Policies
        {
            get => _policies ?? (_policies = new InputList<Inputs.NotificationPolicyPolicyGetArgs>());
            set => _policies = value;
        }

        /// <summary>
        /// Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        /// </summary>
        [Input("repeatInterval")]
        public Input<string>? RepeatInterval { get; set; }

        public NotificationPolicyState()
        {
        }
        public static new NotificationPolicyState Empty => new NotificationPolicyState();
    }
}