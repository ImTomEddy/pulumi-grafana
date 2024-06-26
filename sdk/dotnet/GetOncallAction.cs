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
    [Obsolete(@"grafana.index/getoncallaction.getOncallAction has been deprecated in favor of grafana.oncall/getaction.getAction")]
    public static class GetOncallAction
    {
        public static Task<GetOncallActionResult> InvokeAsync(GetOncallActionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOncallActionResult>("grafana:index/getOncallAction:getOncallAction", args ?? new GetOncallActionArgs(), options.WithDefaults());

        public static Output<GetOncallActionResult> Invoke(GetOncallActionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOncallActionResult>("grafana:index/getOncallAction:getOncallAction", args ?? new GetOncallActionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOncallActionArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOncallActionArgs()
        {
        }
        public static new GetOncallActionArgs Empty => new GetOncallActionArgs();
    }

    public sealed class GetOncallActionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOncallActionInvokeArgs()
        {
        }
        public static new GetOncallActionInvokeArgs Empty => new GetOncallActionInvokeArgs();
    }


    [OutputType]
    public sealed class GetOncallActionResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;

        [OutputConstructor]
        private GetOncallActionResult(
            string id,

            string name)
        {
            Id = id;
            Name = name;
        }
    }
}
