// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Oss.Inputs
{

    public sealed class FolderPermissionPermissionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Permission to associate with item. Must be one of `View`, `Edit`, or `Admin`.
        /// </summary>
        [Input("permission", required: true)]
        public Input<string> Permission { get; set; } = null!;

        /// <summary>
        /// Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// ID of the team to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// ID of the user or service account to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public FolderPermissionPermissionArgs()
        {
        }
        public static new FolderPermissionPermissionArgs Empty => new FolderPermissionPermissionArgs();
    }
}
