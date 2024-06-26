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
    [Obsolete(@"grafana.index/folderpermission.FolderPermission has been deprecated in favor of grafana.oss/folderpermission.FolderPermission")]
    [GrafanaResourceType("grafana:index/folderPermission:FolderPermission")]
    public partial class FolderPermission : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The UID of the folder.
        /// </summary>
        [Output("folderUid")]
        public Output<string> FolderUid { get; private set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        [Output("permissions")]
        public Output<ImmutableArray<Outputs.FolderPermissionPermission>> Permissions { get; private set; } = null!;


        /// <summary>
        /// Create a FolderPermission resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FolderPermission(string name, FolderPermissionArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/folderPermission:FolderPermission", name, args ?? new FolderPermissionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FolderPermission(string name, Input<string> id, FolderPermissionState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/folderPermission:FolderPermission", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "grafana:index/folderPermission:FolderPermission" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FolderPermission resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FolderPermission Get(string name, Input<string> id, FolderPermissionState? state = null, CustomResourceOptions? options = null)
        {
            return new FolderPermission(name, id, state, options);
        }
    }

    public sealed class FolderPermissionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The UID of the folder.
        /// </summary>
        [Input("folderUid", required: true)]
        public Input<string> FolderUid { get; set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("permissions")]
        private InputList<Inputs.FolderPermissionPermissionArgs>? _permissions;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        public InputList<Inputs.FolderPermissionPermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.FolderPermissionPermissionArgs>());
            set => _permissions = value;
        }

        public FolderPermissionArgs()
        {
        }
        public static new FolderPermissionArgs Empty => new FolderPermissionArgs();
    }

    public sealed class FolderPermissionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The UID of the folder.
        /// </summary>
        [Input("folderUid")]
        public Input<string>? FolderUid { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("permissions")]
        private InputList<Inputs.FolderPermissionPermissionGetArgs>? _permissions;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        public InputList<Inputs.FolderPermissionPermissionGetArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.FolderPermissionPermissionGetArgs>());
            set => _permissions = value;
        }

        public FolderPermissionState()
        {
        }
        public static new FolderPermissionState Empty => new FolderPermissionState();
    }
}
