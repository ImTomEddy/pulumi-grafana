// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs_Pulumi.Grafana
{
    /// <summary>
    /// Besides the public probes run by Grafana Labs, you can also install your
    /// own private probes. These are only accessible to you and only write data to
    /// your Grafana Cloud account. Private probes are instances of the open source
    /// Grafana Synthetic Monitoring Agent.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Grafana = Lbrlabs_Pulumi.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = new Grafana.SyntheticMonitoringProbe("main", new()
    ///     {
    ///         Labels = 
    ///         {
    ///             { "type", "mountain" },
    ///         },
    ///         Latitude = 27.98606,
    ///         Longitude = 86.92262,
    ///         Region = "APAC",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe probe {{probe-id}}
    /// ```
    /// 
    /// ```sh
    ///  $ pulumi import grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe probe {{probe-id}}:{{auth_token}}
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe")]
    public partial class SyntheticMonitoringProbe : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
        /// </summary>
        [Output("authToken")]
        public Output<string> AuthToken { get; private set; } = null!;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Latitude coordinates.
        /// </summary>
        [Output("latitude")]
        public Output<double> Latitude { get; private set; } = null!;

        /// <summary>
        /// Longitude coordinates.
        /// </summary>
        [Output("longitude")]
        public Output<double> Longitude { get; private set; } = null!;

        /// <summary>
        /// Name of the probe.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set to `true`. Defaults to `false`.
        /// </summary>
        [Output("public")]
        public Output<bool?> Public { get; private set; } = null!;

        /// <summary>
        /// Region of the probe.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The tenant ID of the probe.
        /// </summary>
        [Output("tenantId")]
        public Output<int> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a SyntheticMonitoringProbe resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SyntheticMonitoringProbe(string name, SyntheticMonitoringProbeArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe", name, args ?? new SyntheticMonitoringProbeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SyntheticMonitoringProbe(string name, Input<string> id, SyntheticMonitoringProbeState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/lbrlabs",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SyntheticMonitoringProbe resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SyntheticMonitoringProbe Get(string name, Input<string> id, SyntheticMonitoringProbeState? state = null, CustomResourceOptions? options = null)
        {
            return new SyntheticMonitoringProbe(name, id, state, options);
        }
    }

    public sealed class SyntheticMonitoringProbeArgs : global::Pulumi.ResourceArgs
    {
        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Latitude coordinates.
        /// </summary>
        [Input("latitude", required: true)]
        public Input<double> Latitude { get; set; } = null!;

        /// <summary>
        /// Longitude coordinates.
        /// </summary>
        [Input("longitude", required: true)]
        public Input<double> Longitude { get; set; } = null!;

        /// <summary>
        /// Name of the probe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set to `true`. Defaults to `false`.
        /// </summary>
        [Input("public")]
        public Input<bool>? Public { get; set; }

        /// <summary>
        /// Region of the probe.
        /// </summary>
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        public SyntheticMonitoringProbeArgs()
        {
        }
        public static new SyntheticMonitoringProbeArgs Empty => new SyntheticMonitoringProbeArgs();
    }

    public sealed class SyntheticMonitoringProbeState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
        /// </summary>
        [Input("authToken")]
        public Input<string>? AuthToken { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Latitude coordinates.
        /// </summary>
        [Input("latitude")]
        public Input<double>? Latitude { get; set; }

        /// <summary>
        /// Longitude coordinates.
        /// </summary>
        [Input("longitude")]
        public Input<double>? Longitude { get; set; }

        /// <summary>
        /// Name of the probe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set to `true`. Defaults to `false`.
        /// </summary>
        [Input("public")]
        public Input<bool>? Public { get; set; }

        /// <summary>
        /// Region of the probe.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The tenant ID of the probe.
        /// </summary>
        [Input("tenantId")]
        public Input<int>? TenantId { get; set; }

        public SyntheticMonitoringProbeState()
        {
        }
        public static new SyntheticMonitoringProbeState Empty => new SyntheticMonitoringProbeState();
    }
}