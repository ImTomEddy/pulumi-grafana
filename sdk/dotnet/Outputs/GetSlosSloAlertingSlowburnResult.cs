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
    public sealed class GetSlosSloAlertingSlowburnResult
    {
        /// <summary>
        /// Annotations to attach only to Slow Burn alerts.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSlosSloAlertingSlowburnAnnotationResult> Annotations;
        /// <summary>
        /// Labels to attach only to Slow Burn alerts.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSlosSloAlertingSlowburnLabelResult> Labels;

        [OutputConstructor]
        private GetSlosSloAlertingSlowburnResult(
            ImmutableArray<Outputs.GetSlosSloAlertingSlowburnAnnotationResult> annotations,

            ImmutableArray<Outputs.GetSlosSloAlertingSlowburnLabelResult> labels)
        {
            Annotations = annotations;
            Labels = labels;
        }
    }
}
