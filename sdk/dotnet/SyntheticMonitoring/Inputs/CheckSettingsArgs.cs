// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring.Inputs
{

    public sealed class CheckSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Settings for DNS check. The target must be a valid hostname (or IP address for `PTR` records).
        /// </summary>
        [Input("dns")]
        public Input<Inputs.CheckSettingsDnsArgs>? Dns { get; set; }

        /// <summary>
        /// Settings for HTTP check. The target must be a URL (http or https).
        /// </summary>
        [Input("http")]
        public Input<Inputs.CheckSettingsHttpArgs>? Http { get; set; }

        /// <summary>
        /// Settings for MultiHTTP check. The target must be a URL (http or https)
        /// </summary>
        [Input("multihttp")]
        public Input<Inputs.CheckSettingsMultihttpArgs>? Multihttp { get; set; }

        /// <summary>
        /// Settings for ping (ICMP) check. The target must be a valid hostname or IP address.
        /// </summary>
        [Input("ping")]
        public Input<Inputs.CheckSettingsPingArgs>? Ping { get; set; }

        /// <summary>
        /// Settings for TCP check. The target must be of the form `&lt;host&gt;:&lt;port&gt;`, where the host portion must be a valid hostname or IP address.
        /// </summary>
        [Input("tcp")]
        public Input<Inputs.CheckSettingsTcpArgs>? Tcp { get; set; }

        /// <summary>
        /// Settings for traceroute check. The target must be a valid hostname or IP address
        /// </summary>
        [Input("traceroute")]
        public Input<Inputs.CheckSettingsTracerouteArgs>? Traceroute { get; set; }

        public CheckSettingsArgs()
        {
        }
        public static new CheckSettingsArgs Empty => new CheckSettingsArgs();
    }
}
