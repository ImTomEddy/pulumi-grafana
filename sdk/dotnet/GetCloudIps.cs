// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana
{
    [Obsolete(@"grafana.index/getcloudips.getCloudIps has been deprecated in favor of grafana.cloud/getips.getIps")]
    public static class GetCloudIps
    {
        public static Task<GetCloudIpsResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCloudIpsResult>("grafana:index/getCloudIps:getCloudIps", InvokeArgs.Empty, options.WithDefaults());

        public static Output<GetCloudIpsResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCloudIpsResult>("grafana:index/getCloudIps:getCloudIps", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetCloudIpsResult
    {
        public readonly ImmutableArray<string> HostedAlerts;
        public readonly ImmutableArray<string> HostedGrafanas;
        public readonly ImmutableArray<string> HostedLogs;
        public readonly ImmutableArray<string> HostedMetrics;
        public readonly ImmutableArray<string> HostedTraces;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetCloudIpsResult(
            ImmutableArray<string> hostedAlerts,

            ImmutableArray<string> hostedGrafanas,

            ImmutableArray<string> hostedLogs,

            ImmutableArray<string> hostedMetrics,

            ImmutableArray<string> hostedTraces,

            string id)
        {
            HostedAlerts = hostedAlerts;
            HostedGrafanas = hostedGrafanas;
            HostedLogs = hostedLogs;
            HostedMetrics = hostedMetrics;
            HostedTraces = hostedTraces;
            Id = id;
        }
    }
}
