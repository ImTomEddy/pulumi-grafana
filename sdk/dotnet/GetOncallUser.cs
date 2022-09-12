// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs_Pulumi.Grafana
{
    public static class GetOncallUser
    {
        /// <summary>
        /// * [HTTP API](https://grafana.com/docs/grafana-cloud/oncall/oncall-api-reference/users/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var alex = Grafana.GetOncallUser.Invoke(new()
        ///     {
        ///         Username = "alex",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetOncallUserResult> InvokeAsync(GetOncallUserArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetOncallUserResult>("grafana:index/getOncallUser:getOncallUser", args ?? new GetOncallUserArgs(), options.WithDefaults());

        /// <summary>
        /// * [HTTP API](https://grafana.com/docs/grafana-cloud/oncall/oncall-api-reference/users/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var alex = Grafana.GetOncallUser.Invoke(new()
        ///     {
        ///         Username = "alex",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetOncallUserResult> Invoke(GetOncallUserInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetOncallUserResult>("grafana:index/getOncallUser:getOncallUser", args ?? new GetOncallUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOncallUserArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The username of the user.
        /// </summary>
        [Input("username", required: true)]
        public string Username { get; set; } = null!;

        public GetOncallUserArgs()
        {
        }
        public static new GetOncallUserArgs Empty => new GetOncallUserArgs();
    }

    public sealed class GetOncallUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The username of the user.
        /// </summary>
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
        /// <summary>
        /// The email of the user.
        /// </summary>
        public readonly string Email;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The role of the user.
        /// </summary>
        public readonly string Role;
        /// <summary>
        /// The username of the user.
        /// </summary>
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