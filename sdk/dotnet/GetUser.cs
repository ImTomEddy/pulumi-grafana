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
    public static class GetUser
    {
        public static Task<GetUserResult> InvokeAsync(GetUserArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("grafana:index/getUser:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        public static Output<GetUserResult> Invoke(GetUserInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("grafana:index/getUser:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : global::Pulumi.InvokeArgs
    {
        [Input("email")]
        public string? Email { get; set; }

        [Input("login")]
        public string? Login { get; set; }

        [Input("userId")]
        public int? UserId { get; set; }

        public GetUserArgs()
        {
        }
        public static new GetUserArgs Empty => new GetUserArgs();
    }

    public sealed class GetUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("email")]
        public Input<string>? Email { get; set; }

        [Input("login")]
        public Input<string>? Login { get; set; }

        [Input("userId")]
        public Input<int>? UserId { get; set; }

        public GetUserInvokeArgs()
        {
        }
        public static new GetUserInvokeArgs Empty => new GetUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserResult
    {
        public readonly string? Email;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly bool IsAdmin;
        public readonly string? Login;
        public readonly string Name;
        public readonly int? UserId;

        [OutputConstructor]
        private GetUserResult(
            string? email,

            string id,

            bool isAdmin,

            string? login,

            string name,

            int? userId)
        {
            Email = email;
            Id = id;
            IsAdmin = isAdmin;
            Login = login;
            Name = name;
            UserId = userId;
        }
    }
}
