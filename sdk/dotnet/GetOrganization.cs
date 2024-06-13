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
    public static class GetOrganization
    {
        /// <summary>
        /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
        /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/org/)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// using Grafana = Pulumiverse.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = new Grafana.Organization("test", new()
        ///     {
        ///         AdminUser = "admin",
        ///         CreateUsers = true,
        ///         Viewers = new[]
        ///         {
        ///             "viewer-01@example.com",
        ///             "viewer-02@example.com",
        ///         },
        ///     });
        /// 
        ///     var fromName = Grafana.GetOrganization.Invoke(new()
        ///     {
        ///         Name = test.Name,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetOrganizationResult> InvokeAsync(GetOrganizationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationResult>("grafana:index/getOrganization:getOrganization", args ?? new GetOrganizationArgs(), options.WithDefaults());

        /// <summary>
        /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
        /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/org/)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// using Grafana = Pulumiverse.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = new Grafana.Organization("test", new()
        ///     {
        ///         AdminUser = "admin",
        ///         CreateUsers = true,
        ///         Viewers = new[]
        ///         {
        ///             "viewer-01@example.com",
        ///             "viewer-02@example.com",
        ///         },
        ///     });
        /// 
        ///     var fromName = Grafana.GetOrganization.Invoke(new()
        ///     {
        ///         Name = test.Name,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetOrganizationResult> Invoke(GetOrganizationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationResult>("grafana:index/getOrganization:getOrganization", args ?? new GetOrganizationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrganizationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Organization.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOrganizationArgs()
        {
        }
        public static new GetOrganizationArgs Empty => new GetOrganizationArgs();
    }

    public sealed class GetOrganizationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Organization.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOrganizationInvokeArgs()
        {
        }
        public static new GetOrganizationInvokeArgs Empty => new GetOrganizationInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrganizationResult
    {
        /// <summary>
        /// A list of email addresses corresponding to users given admin access to the organization.
        /// </summary>
        public readonly ImmutableArray<string> Admins;
        /// <summary>
        /// A list of email addresses corresponding to users given editor access to the organization.
        /// </summary>
        public readonly ImmutableArray<string> Editors;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the Organization.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// A list of email addresses corresponding to users given viewer access to the organization.
        /// </summary>
        public readonly ImmutableArray<string> Viewers;

        [OutputConstructor]
        private GetOrganizationResult(
            ImmutableArray<string> admins,

            ImmutableArray<string> editors,

            string id,

            string name,

            ImmutableArray<string> viewers)
        {
            Admins = admins;
            Editors = editors;
            Id = id;
            Name = name;
            Viewers = viewers;
        }
    }
}
