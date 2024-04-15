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

    public sealed class OncallRouteSlackArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Slack channel id. Alerts will be directed to this channel in Slack.
        /// </summary>
        [Input("channelId")]
        public Input<string>? ChannelId { get; set; }

        /// <summary>
        /// Enable notification in Slack.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public OncallRouteSlackArgs()
        {
        }
        public static new OncallRouteSlackArgs Empty => new OncallRouteSlackArgs();
    }
}
