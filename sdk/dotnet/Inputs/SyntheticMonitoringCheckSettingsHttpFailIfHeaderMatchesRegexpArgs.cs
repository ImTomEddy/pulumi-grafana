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

    public sealed class SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Allow header to be missing from responses. Defaults to `false`.
        /// </summary>
        [Input("allowMissing")]
        public Input<bool>? AllowMissing { get; set; }

        /// <summary>
        /// Header name.
        /// </summary>
        [Input("header", required: true)]
        public Input<string> Header { get; set; } = null!;

        /// <summary>
        /// Regex that header value should match.
        /// </summary>
        [Input("regexp", required: true)]
        public Input<string> Regexp { get; set; } = null!;

        public SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs()
        {
        }
        public static new SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs Empty => new SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs();
    }
}
