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

    public sealed class ReportDashboardGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("reportVariables")]
        private InputMap<object>? _reportVariables;

        /// <summary>
        /// Add report variables to the dashboard. Values should be separated by commas.
        /// </summary>
        public InputMap<object> ReportVariables
        {
            get => _reportVariables ?? (_reportVariables = new InputMap<object>());
            set => _reportVariables = value;
        }

        /// <summary>
        /// Time range of the report.
        /// </summary>
        [Input("timeRange")]
        public Input<Inputs.ReportDashboardTimeRangeGetArgs>? TimeRange { get; set; }

        /// <summary>
        /// Dashboard uid.
        /// </summary>
        [Input("uid", required: true)]
        public Input<string> Uid { get; set; } = null!;

        public ReportDashboardGetArgs()
        {
        }
        public static new ReportDashboardGetArgs Empty => new ReportDashboardGetArgs();
    }
}
