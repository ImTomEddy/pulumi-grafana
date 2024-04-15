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
    [GrafanaResourceType("grafana:index/dataSource:DataSource")]
    public partial class DataSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The method by which Grafana will access the data source: `proxy` or `direct`.
        /// </summary>
        [Output("accessMode")]
        public Output<string?> AccessMode { get; private set; } = null!;

        /// <summary>
        /// Whether to enable basic auth for the data source.
        /// </summary>
        [Output("basicAuthEnabled")]
        public Output<bool?> BasicAuthEnabled { get; private set; } = null!;

        /// <summary>
        /// Basic auth username.
        /// </summary>
        [Output("basicAuthUsername")]
        public Output<string?> BasicAuthUsername { get; private set; } = null!;

        /// <summary>
        /// (Required by some data source types) The name of the database to use on the selected data source server.
        /// </summary>
        [Output("databaseName")]
        public Output<string?> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// Custom HTTP headers
        /// </summary>
        [Output("httpHeaders")]
        public Output<ImmutableDictionary<string, string>?> HttpHeaders { get; private set; } = null!;

        /// <summary>
        /// Whether to set the data source as default. This should only be `true` to a single data source.
        /// </summary>
        [Output("isDefault")]
        public Output<bool?> IsDefault { get; private set; } = null!;

        /// <summary>
        /// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
        /// source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
        /// from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        [Output("jsonDataEncoded")]
        public Output<string?> JsonDataEncoded { get; private set; } = null!;

        /// <summary>
        /// A unique name for the data source.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
        /// to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
        /// saving it from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        [Output("secureJsonDataEncoded")]
        public Output<string?> SecureJsonDataEncoded { get; private set; } = null!;

        /// <summary>
        /// The data source type. Must be one of the supported data source keywords.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        /// <summary>
        /// The URL for the data source. The type of URL required varies depending on the chosen data source type.
        /// </summary>
        [Output("url")]
        public Output<string?> Url { get; private set; } = null!;

        /// <summary>
        /// (Required by some data source types) The username to use to authenticate to the data source.
        /// </summary>
        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/dataSource:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/dataSource:DataSource", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "httpHeaders",
                    "secureJsonDataEncoded",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, state, options);
        }
    }

    public sealed class DataSourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The method by which Grafana will access the data source: `proxy` or `direct`.
        /// </summary>
        [Input("accessMode")]
        public Input<string>? AccessMode { get; set; }

        /// <summary>
        /// Whether to enable basic auth for the data source.
        /// </summary>
        [Input("basicAuthEnabled")]
        public Input<bool>? BasicAuthEnabled { get; set; }

        /// <summary>
        /// Basic auth username.
        /// </summary>
        [Input("basicAuthUsername")]
        public Input<string>? BasicAuthUsername { get; set; }

        /// <summary>
        /// (Required by some data source types) The name of the database to use on the selected data source server.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        [Input("httpHeaders")]
        private InputMap<string>? _httpHeaders;

        /// <summary>
        /// Custom HTTP headers
        /// </summary>
        public InputMap<string> HttpHeaders
        {
            get => _httpHeaders ?? (_httpHeaders = new InputMap<string>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, string>());
                _httpHeaders = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        /// <summary>
        /// Whether to set the data source as default. This should only be `true` to a single data source.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
        /// source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
        /// from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        [Input("jsonDataEncoded")]
        public Input<string>? JsonDataEncoded { get; set; }

        /// <summary>
        /// A unique name for the data source.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("secureJsonDataEncoded")]
        private Input<string>? _secureJsonDataEncoded;

        /// <summary>
        /// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
        /// to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
        /// saving it from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        public Input<string>? SecureJsonDataEncoded
        {
            get => _secureJsonDataEncoded;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secureJsonDataEncoded = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The data source type. Must be one of the supported data source keywords.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The URL for the data source. The type of URL required varies depending on the chosen data source type.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        /// <summary>
        /// (Required by some data source types) The username to use to authenticate to the data source.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public DataSourceArgs()
        {
        }
        public static new DataSourceArgs Empty => new DataSourceArgs();
    }

    public sealed class DataSourceState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The method by which Grafana will access the data source: `proxy` or `direct`.
        /// </summary>
        [Input("accessMode")]
        public Input<string>? AccessMode { get; set; }

        /// <summary>
        /// Whether to enable basic auth for the data source.
        /// </summary>
        [Input("basicAuthEnabled")]
        public Input<bool>? BasicAuthEnabled { get; set; }

        /// <summary>
        /// Basic auth username.
        /// </summary>
        [Input("basicAuthUsername")]
        public Input<string>? BasicAuthUsername { get; set; }

        /// <summary>
        /// (Required by some data source types) The name of the database to use on the selected data source server.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        [Input("httpHeaders")]
        private InputMap<string>? _httpHeaders;

        /// <summary>
        /// Custom HTTP headers
        /// </summary>
        public InputMap<string> HttpHeaders
        {
            get => _httpHeaders ?? (_httpHeaders = new InputMap<string>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, string>());
                _httpHeaders = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        /// <summary>
        /// Whether to set the data source as default. This should only be `true` to a single data source.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
        /// source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
        /// from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        [Input("jsonDataEncoded")]
        public Input<string>? JsonDataEncoded { get; set; }

        /// <summary>
        /// A unique name for the data source.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("secureJsonDataEncoded")]
        private Input<string>? _secureJsonDataEncoded;

        /// <summary>
        /// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
        /// to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
        /// saving it from the Grafana UI. Note that keys in this map are usually camelCased.
        /// </summary>
        public Input<string>? SecureJsonDataEncoded
        {
            get => _secureJsonDataEncoded;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secureJsonDataEncoded = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The data source type. Must be one of the supported data source keywords.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The URL for the data source. The type of URL required varies depending on the chosen data source type.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        /// <summary>
        /// (Required by some data source types) The username to use to authenticate to the data source.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public DataSourceState()
        {
        }
        public static new DataSourceState Empty => new DataSourceState();
    }
}
