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

    public sealed class ReportDashboardTimeRangeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Start of the time range.
        /// </summary>
        [Input("from")]
        public Input<string>? From { get; set; }

        /// <summary>
        /// End of the time range.
        /// </summary>
        [Input("to")]
        public Input<string>? To { get; set; }

        public ReportDashboardTimeRangeArgs()
        {
        }
        public static new ReportDashboardTimeRangeArgs Empty => new ReportDashboardTimeRangeArgs();
    }
}
