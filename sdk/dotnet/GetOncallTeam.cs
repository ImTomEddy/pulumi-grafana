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
    [Obsolete(@"grafana.index/getoncallteam.getOncallTeam has been deprecated in favor of grafana.oncall/getteam.getTeam")]
    public static class GetOncallTeam
    {
        public static Task<GetOncallTeamResult> InvokeAsync(GetOncallTeamArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOncallTeamResult>("grafana:index/getOncallTeam:getOncallTeam", args ?? new GetOncallTeamArgs(), options.WithDefaults());

        public static Output<GetOncallTeamResult> Invoke(GetOncallTeamInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOncallTeamResult>("grafana:index/getOncallTeam:getOncallTeam", args ?? new GetOncallTeamInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOncallTeamArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOncallTeamArgs()
        {
        }
        public static new GetOncallTeamArgs Empty => new GetOncallTeamArgs();
    }

    public sealed class GetOncallTeamInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOncallTeamInvokeArgs()
        {
        }
        public static new GetOncallTeamInvokeArgs Empty => new GetOncallTeamInvokeArgs();
    }


    [OutputType]
    public sealed class GetOncallTeamResult
    {
        public readonly string AvatarUrl;
        public readonly string Email;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;

        [OutputConstructor]
        private GetOncallTeamResult(
            string avatarUrl,

            string email,

            string id,

            string name)
        {
            AvatarUrl = avatarUrl;
            Email = email;
            Id = id;
            Name = name;
        }
    }
}
