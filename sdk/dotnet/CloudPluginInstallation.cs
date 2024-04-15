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
    [GrafanaResourceType("grafana:index/cloudPluginInstallation:CloudPluginInstallation")]
    public partial class CloudPluginInstallation : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Slug of the plugin to be installed.
        /// </summary>
        [Output("slug")]
        public Output<string> Slug { get; private set; } = null!;

        /// <summary>
        /// The stack id to which the plugin should be installed.
        /// </summary>
        [Output("stackSlug")]
        public Output<string> StackSlug { get; private set; } = null!;

        /// <summary>
        /// Version of the plugin to be installed.
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a CloudPluginInstallation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CloudPluginInstallation(string name, CloudPluginInstallationArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/cloudPluginInstallation:CloudPluginInstallation", name, args ?? new CloudPluginInstallationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CloudPluginInstallation(string name, Input<string> id, CloudPluginInstallationState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/cloudPluginInstallation:CloudPluginInstallation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CloudPluginInstallation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CloudPluginInstallation Get(string name, Input<string> id, CloudPluginInstallationState? state = null, CustomResourceOptions? options = null)
        {
            return new CloudPluginInstallation(name, id, state, options);
        }
    }

    public sealed class CloudPluginInstallationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Slug of the plugin to be installed.
        /// </summary>
        [Input("slug", required: true)]
        public Input<string> Slug { get; set; } = null!;

        /// <summary>
        /// The stack id to which the plugin should be installed.
        /// </summary>
        [Input("stackSlug", required: true)]
        public Input<string> StackSlug { get; set; } = null!;

        /// <summary>
        /// Version of the plugin to be installed.
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public CloudPluginInstallationArgs()
        {
        }
        public static new CloudPluginInstallationArgs Empty => new CloudPluginInstallationArgs();
    }

    public sealed class CloudPluginInstallationState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Slug of the plugin to be installed.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        /// <summary>
        /// The stack id to which the plugin should be installed.
        /// </summary>
        [Input("stackSlug")]
        public Input<string>? StackSlug { get; set; }

        /// <summary>
        /// Version of the plugin to be installed.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public CloudPluginInstallationState()
        {
        }
        public static new CloudPluginInstallationState Empty => new CloudPluginInstallationState();
    }
}
