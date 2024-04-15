// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Inputs
{

    public sealed class SyntheticMonitoringCheckSettingsTcpTlsConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// CA certificate in PEM format.
        /// </summary>
        [Input("caCert")]
        public Input<string>? CaCert { get; set; }

        /// <summary>
        /// Client certificate in PEM format.
        /// </summary>
        [Input("clientCert")]
        public Input<string>? ClientCert { get; set; }

        [Input("clientKey")]
        private Input<string>? _clientKey;

        /// <summary>
        /// Client key in PEM format.
        /// </summary>
        public Input<string>? ClientKey
        {
            get => _clientKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _clientKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Disable target certificate validation.
        /// </summary>
        [Input("insecureSkipVerify")]
        public Input<bool>? InsecureSkipVerify { get; set; }

        /// <summary>
        /// Used to verify the hostname for the targets.
        /// </summary>
        [Input("serverName")]
        public Input<string>? ServerName { get; set; }

        public SyntheticMonitoringCheckSettingsTcpTlsConfigArgs()
        {
        }
        public static new SyntheticMonitoringCheckSettingsTcpTlsConfigArgs Empty => new SyntheticMonitoringCheckSettingsTcpTlsConfigArgs();
    }
}
