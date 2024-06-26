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
    [Obsolete(@"grafana.index/getoncallschedule.getOncallSchedule has been deprecated in favor of grafana.oncall/getschedule.getSchedule")]
    public static class GetOncallSchedule
    {
        public static Task<GetOncallScheduleResult> InvokeAsync(GetOncallScheduleArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOncallScheduleResult>("grafana:index/getOncallSchedule:getOncallSchedule", args ?? new GetOncallScheduleArgs(), options.WithDefaults());

        public static Output<GetOncallScheduleResult> Invoke(GetOncallScheduleInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOncallScheduleResult>("grafana:index/getOncallSchedule:getOncallSchedule", args ?? new GetOncallScheduleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOncallScheduleArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOncallScheduleArgs()
        {
        }
        public static new GetOncallScheduleArgs Empty => new GetOncallScheduleArgs();
    }

    public sealed class GetOncallScheduleInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOncallScheduleInvokeArgs()
        {
        }
        public static new GetOncallScheduleInvokeArgs Empty => new GetOncallScheduleInvokeArgs();
    }


    [OutputType]
    public sealed class GetOncallScheduleResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string Type;

        [OutputConstructor]
        private GetOncallScheduleResult(
            string id,

            string name,

            string type)
        {
            Id = id;
            Name = name;
            Type = type;
        }
    }
}
