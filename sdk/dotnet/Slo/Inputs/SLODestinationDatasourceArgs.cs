// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Slo.Inputs
{

    public sealed class SLODestinationDatasourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// UID for the Mimir Datasource
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public SLODestinationDatasourceArgs()
        {
        }
        public static new SLODestinationDatasourceArgs Empty => new SLODestinationDatasourceArgs();
    }
}
