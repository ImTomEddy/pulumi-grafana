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

    public sealed class ReportScheduleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Custom interval of the report.
        /// **Note:** This field is only available when frequency is set to `custom`.
        /// </summary>
        [Input("customInterval")]
        public Input<string>? CustomInterval { get; set; }

        /// <summary>
        /// End time of the report. If empty, the report will be sent indefinitely (according to frequency). Note that times will be saved as UTC in Grafana. Use 2006-01-02T15:04:05 format if you want to set a custom timezone
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// Frequency of the report. Allowed values: `never`, `once`, `hourly`, `daily`, `weekly`, `monthly`, `custom`.
        /// </summary>
        [Input("frequency", required: true)]
        public Input<string> Frequency { get; set; } = null!;

        /// <summary>
        /// Send the report on the last day of the month
        /// </summary>
        [Input("lastDayOfMonth")]
        public Input<bool>? LastDayOfMonth { get; set; }

        /// <summary>
        /// Start time of the report. If empty, the start date will be set to the creation time. Note that times will be saved as UTC in Grafana. Use 2006-01-02T15:04:05 format if you want to set a custom timezone
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        /// <summary>
        /// Set the report time zone.
        /// </summary>
        [Input("timezone")]
        public Input<string>? Timezone { get; set; }

        /// <summary>
        /// Whether to send the report only on work days.
        /// </summary>
        [Input("workdaysOnly")]
        public Input<bool>? WorkdaysOnly { get; set; }

        public ReportScheduleArgs()
        {
        }
        public static new ReportScheduleArgs Empty => new ReportScheduleArgs();
    }
}
