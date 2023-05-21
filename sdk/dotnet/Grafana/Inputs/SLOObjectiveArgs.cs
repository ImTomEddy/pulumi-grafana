// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Inputs
{

    public sealed class SLOObjectiveArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Value between 0 and 1. If the value of the query is above the objective, the SLO is met.
        /// </summary>
        [Input("value", required: true)]
        public Input<double> Value { get; set; } = null!;

        /// <summary>
        /// A Prometheus-parsable time duration string like 24h, 60m. This is the time window the objective is measured over.
        /// </summary>
        [Input("window", required: true)]
        public Input<string> Window { get; set; } = null!;

        public SLOObjectiveArgs()
        {
        }
        public static new SLOObjectiveArgs Empty => new SLOObjectiveArgs();
    }
}
