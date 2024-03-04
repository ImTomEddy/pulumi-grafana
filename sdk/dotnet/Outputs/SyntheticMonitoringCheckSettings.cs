// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Outputs
{

    [OutputType]
    public sealed class SyntheticMonitoringCheckSettings
    {
        /// <summary>
        /// Settings for DNS check. The target must be a valid hostname (or IP address for `PTR` records).
        /// </summary>
        public readonly Outputs.SyntheticMonitoringCheckSettingsDns? Dns;
        /// <summary>
        /// Settings for HTTP check. The target must be a URL (http or https).
        /// </summary>
        public readonly Outputs.SyntheticMonitoringCheckSettingsHttp? Http;
        /// <summary>
        /// Settings for ping (ICMP) check. The target must be a valid hostname or IP address.
        /// </summary>
        public readonly Outputs.SyntheticMonitoringCheckSettingsPing? Ping;
        /// <summary>
        /// Settings for TCP check. The target must be of the form `&lt;host&gt;:&lt;port&gt;`, where the host portion must be a valid hostname or IP address.
        /// </summary>
        public readonly Outputs.SyntheticMonitoringCheckSettingsTcp? Tcp;
        /// <summary>
        /// Settings for traceroute check. The target must be a valid hostname or IP address
        /// </summary>
        public readonly Outputs.SyntheticMonitoringCheckSettingsTraceroute? Traceroute;

        [OutputConstructor]
        private SyntheticMonitoringCheckSettings(
            Outputs.SyntheticMonitoringCheckSettingsDns? dns,

            Outputs.SyntheticMonitoringCheckSettingsHttp? http,

            Outputs.SyntheticMonitoringCheckSettingsPing? ping,

            Outputs.SyntheticMonitoringCheckSettingsTcp? tcp,

            Outputs.SyntheticMonitoringCheckSettingsTraceroute? traceroute)
        {
            Dns = dns;
            Http = http;
            Ping = ping;
            Tcp = tcp;
            Traceroute = traceroute;
        }
    }
}