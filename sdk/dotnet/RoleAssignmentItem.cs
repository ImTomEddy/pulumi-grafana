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
    /// <summary>
    /// Manages a single assignment for a role. Conflicts with the "grafana.RoleAssignment" resource which manages the entire set of assignments for a role.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var testRole = new Grafana.Role("testRole", new()
    ///     {
    ///         Uid = "testrole",
    ///         Version = 1,
    ///         Global = true,
    ///         Permissions = new[]
    ///         {
    ///             new Grafana.Inputs.RolePermissionArgs
    ///             {
    ///                 Action = "org.users:add",
    ///                 Scope = "users:*",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var testTeam = new Grafana.Team("testTeam");
    /// 
    ///     var testUser = new Grafana.User("testUser", new()
    ///     {
    ///         Email = "terraform_user@test.com",
    ///         Login = "terraform_user@test.com",
    ///         Password = "password",
    ///     });
    /// 
    ///     var testSa = new Grafana.ServiceAccount("testSa", new()
    ///     {
    ///         Role = "Viewer",
    ///     });
    /// 
    ///     var user = new Grafana.RoleAssignmentItem("user", new()
    ///     {
    ///         RoleUid = testRole.Uid,
    ///         UserId = testUser.Id,
    ///     });
    /// 
    ///     var team = new Grafana.RoleAssignmentItem("team", new()
    ///     {
    ///         RoleUid = testRole.Uid,
    ///         TeamId = testTeam.Id,
    ///     });
    /// 
    ///     var serviceAccount = new Grafana.RoleAssignmentItem("serviceAccount", new()
    ///     {
    ///         RoleUid = testRole.Uid,
    ///         ServiceAccountId = testSa.Id,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:index/roleAssignmentItem:RoleAssignmentItem name "{{ roleUID }}:{{ type (user, team or service_account) }}:{{ identifier }}"
    /// ```
    /// 
    /// ```sh
    /// $ pulumi import grafana:index/roleAssignmentItem:RoleAssignmentItem name "{{ orgID }}:{{ roleUID }}:{{ type (user, team or service_account) }}:{{ identifier }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/roleAssignmentItem:RoleAssignmentItem")]
    public partial class RoleAssignmentItem : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string> OrgId { get; private set; } = null!;

        /// <summary>
        /// the role UID onto which to assign an actor
        /// </summary>
        [Output("roleUid")]
        public Output<string> RoleUid { get; private set; } = null!;

        /// <summary>
        /// the service account onto which the role is to be assigned
        /// </summary>
        [Output("serviceAccountId")]
        public Output<string?> ServiceAccountId { get; private set; } = null!;

        /// <summary>
        /// the team onto which the role is to be assigned
        /// </summary>
        [Output("teamId")]
        public Output<string?> TeamId { get; private set; } = null!;

        /// <summary>
        /// the user onto which the role is to be assigned
        /// </summary>
        [Output("userId")]
        public Output<string?> UserId { get; private set; } = null!;


        /// <summary>
        /// Create a RoleAssignmentItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RoleAssignmentItem(string name, RoleAssignmentItemArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/roleAssignmentItem:RoleAssignmentItem", name, args ?? new RoleAssignmentItemArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RoleAssignmentItem(string name, Input<string> id, RoleAssignmentItemState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/roleAssignmentItem:RoleAssignmentItem", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RoleAssignmentItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RoleAssignmentItem Get(string name, Input<string> id, RoleAssignmentItemState? state = null, CustomResourceOptions? options = null)
        {
            return new RoleAssignmentItem(name, id, state, options);
        }
    }

    public sealed class RoleAssignmentItemArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// the role UID onto which to assign an actor
        /// </summary>
        [Input("roleUid", required: true)]
        public Input<string> RoleUid { get; set; } = null!;

        /// <summary>
        /// the service account onto which the role is to be assigned
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        /// <summary>
        /// the team onto which the role is to be assigned
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// the user onto which the role is to be assigned
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public RoleAssignmentItemArgs()
        {
        }
        public static new RoleAssignmentItemArgs Empty => new RoleAssignmentItemArgs();
    }

    public sealed class RoleAssignmentItemState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// the role UID onto which to assign an actor
        /// </summary>
        [Input("roleUid")]
        public Input<string>? RoleUid { get; set; }

        /// <summary>
        /// the service account onto which the role is to be assigned
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        /// <summary>
        /// the team onto which the role is to be assigned
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// the user onto which the role is to be assigned
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public RoleAssignmentItemState()
        {
        }
        public static new RoleAssignmentItemState Empty => new RoleAssignmentItemState();
    }
}
