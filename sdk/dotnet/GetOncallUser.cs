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
    [Obsolete(@"grafana.index/getoncalluser.getOncallUser has been deprecated in favor of grafana.oncall/getuser.getUser")]
    public static class GetOncallUser
    {
        public static Task<GetOncallUserResult> InvokeAsync(GetOncallUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOncallUserResult>("grafana:index/getOncallUser:getOncallUser", args ?? new GetOncallUserArgs(), options.WithDefaults());

        public static Output<GetOncallUserResult> Invoke(GetOncallUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOncallUserResult>("grafana:index/getOncallUser:getOncallUser", args ?? new GetOncallUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOncallUserArgs : global::Pulumi.InvokeArgs
    {
        [Input("username", required: true)]
        public string Username { get; set; } = null!;

        public GetOncallUserArgs()
        {
        }
        public static new GetOncallUserArgs Empty => new GetOncallUserArgs();
    }

    public sealed class GetOncallUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public GetOncallUserInvokeArgs()
        {
        }
        public static new GetOncallUserInvokeArgs Empty => new GetOncallUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetOncallUserResult
    {
        public readonly string Email;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Role;
        public readonly string Username;

        [OutputConstructor]
        private GetOncallUserResult(
            string email,

            string id,

            string role,

            string username)
        {
            Email = email;
            Id = id;
            Role = role;
            Username = username;
        }
    }
}
